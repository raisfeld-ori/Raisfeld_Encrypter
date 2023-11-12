from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def create_key(len: int) -> bytes: return get_random_bytes(len)


class Cipher:
    def __init__(self, password: str, key: bytes = None):
        self.key = PBKDF2(password, key if key else password[:16].encode(), dkLen=32)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv=create_key(16))

    def encrypt(self, data: bytes) -> bytes: return self.cipher.encrypt(pad(data, AES.block_size)) + self.cipher.iv
    def decrypt(self, data: bytes) -> bytes: return unpad(self.cipher.decrypt(data), AES.block_size)


