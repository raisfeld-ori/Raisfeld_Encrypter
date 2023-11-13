from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os.path import normpath
from typing import Optional
from base64 import b64encode
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


# the class for encryption and decryption
class Cipher:
    def __init__(self, password: str, key: bytes = None):
        # the key is just a PBKDF2 protocol key, but if there's no key then use the password as the key
        self.key = PBKDF2(password, key if key else password_as_key(password), dkLen=32)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv=get_random_bytes(16))

    def encrypt_to_str(self, data: str) -> str:
        data = self.encrypt(data.encode())
        data = b64encode(data).decode()
        return data

    # using pycryptodome, encryption is just 1 line
    def encrypt(self, data: bytes) -> bytes: return self.cipher.encrypt(pad(data, AES.block_size)) + self.cipher.iv

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
        self.data: list[bytes] = []
        self.name = name
        self.dir = normpath(appdirs.AppDirs().user_data_dir + '\\' + ".hidden" + "\\" + self.name)

    def encrypt(self, val: bytes) -> bytes: return Cipher(self.password, self.key).encrypt(val)

    def decrypt(self, val: bytes) -> bytes: return Cipher(self.password, self.key).decrypt(val)

    def create(self) -> Optional[Exception]:
        try:
            fast_fs.create_dir(self.dir)
            # some file is needed to make sure the account's password works before actually opening it,
            # so check.txt is just here for this
            fast_fs.write_file(normpath(self.dir + "\\" + "check.txt"), b"abst")
        except Exception as e:
            return e
        return None
