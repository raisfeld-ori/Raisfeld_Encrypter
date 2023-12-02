from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os.path import normpath, exists, getsize
from typing import Optional

import fast_fs
import appdirs


def password_as_key(password: str):
    key = b""
    i = 0
    while len(key) != 16:
        if i == len(password):
            i = 0
        key += password[i].encode()
        i += 1
    return key


def estimate_time(file_dir: str) -> Optional[float]:
    if not exists(file_dir):
        return None
    else:
        """
        calculation:
        file size in gigabytes * average time to encrypt a gigabyte = estimated time
        the file size is in bytes, so i divide it so it'd be a gigabyte instead
        
        the average time is something i tested on 2 of my local machines
        (one linux with good specs, another one with windows and bad specs)
        until i'd like to make a good estimation, this should be enough.
        the time i got was 30 (on average) on the bad machine
        """
        size = getsize(file_dir) / 1073741824
        return size * 30


# the class for encryption and decryption
class Cipher:
    def __init__(self, password: str, key: bytes = None):
        # the key is just a PBKDF2 protocol key, but if there's no key then use the password as the key
        self.key = PBKDF2(password, key if key else password_as_key(password), dkLen=32)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv=get_random_bytes(16))

    # using pycryptodome, encryption is just 1 line
    def encrypt(self, data: bytes) -> Optional[bytes]:
        try:
            return self.cipher.encrypt(pad(data, AES.block_size)) + self.cipher.iv
        except MemoryError:
            return None

    # decryption is the same as encryption, but it's necessary to remove the IV before
    def decrypt(self, data: bytes) -> bytes:
        encrypted_data = data[:-16]
        iv = data[-16:]
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        return unpad(self.cipher.decrypt(encrypted_data), AES.block_size)


class User:

    def __init__(self, name: str, password: str, key: bytes = None):
        self.password = password
        if key:
            self.key = key
        else:
            self.key = password_as_key(password)
        self.vaults: list[Vault] = []
        self.name = name
        self.dir = normpath(appdirs.AppDirs().user_data_dir + '\\' + ".hidden" + "\\" + self.name)
        self.check = b"b7 18 85 32 12 41 60 fe 48 09 "

    def encrypt(self, data: bytes) -> Optional[bytes]:
        return Cipher(self.password, self.key).encrypt(data)

    def decrypt(self, val: bytes) -> bytes:
        return Cipher(self.password, self.key).decrypt(val)

    def create(self) -> Optional[Exception]:
        try:
            fast_fs.create_dir(self.dir)
            # some file is needed to make sure the account's password works before actually opening it,
            # so check.txt is just here for this
            cipher = Cipher(self.password, self.key)
            fast_fs.write_file(normpath(self.dir + "\\" + "check.txt"), cipher.encrypt(self.check))
        except Exception as e:
            return e
        return None

    def save(self):
        for file in fast_fs.read_dir(normpath(self.dir + "\\")):
            if file.name() == "check" and file.extension() == "txt":
                continue
            else:
                file.delete()

        for i, vault in enumerate(self.vaults):
            fast_fs.write_file(normpath(self.dir + "\\" + str(i) + ".f"), vault.data)
            fast_fs.write_file(normpath((self.dir + "\\" + str(i) + ".n")), vault.name.encode())

    def load(self) -> Optional[str]:
        self.vaults.clear()

        # make sure the username exists
        check = normpath(self.dir + "\\" + "check.txt")
        if not exists(check):
            return "no user with this username"
        check = fast_fs.read_file(check)

        # self.decrypt should fail by itself, but I added a failsafe just to be sure
        try:
            check = self.decrypt(check)
            if check != self.check:
                raise ValueError
        except ValueError:
            return "wrong password, please try again"

        files = {}

        data_extensions = ["n", "f"]
        for file in fast_fs.read_dir(normpath(self.dir + "\\")):
            extension = file.extension()
            if not files.get(file.name()) and file.extension() in data_extensions:
                files.update({file.name(): {}})

            try:
                match extension:
                    # the extension for a name
                    case "n":
                        files[file.name()]['name']: str = file.read().decode()
                    case "f":
                        files[file.name()]['data']: bytes = file.read()
                    case _:
                        continue
            except MemoryError:
                return "not enough memory for decryption"

        for vault in files.values():
            self.vaults.append(Vault(vault['name'], self, vault['data']))

    def get(self, item: int):
        return self[item]

    def __getitem__(self, item: int): return self.vaults[item].get()


class Vault:
    def __init__(self, name: str, user: User, data: bytes):
        self.name = name
        self.data = user.encrypt(data)
        self.user = user

    def get(self) -> bytes: return Cipher(self.user.password, self.user.key).decrypt(self.data)
