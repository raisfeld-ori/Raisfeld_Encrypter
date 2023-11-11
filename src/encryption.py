from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def create_key(len: int) -> bytes: return get_random_bytes(len)

class Cipher:
    def __init__(self, password: bytes, key: bytes):
        self.password = password
        self.key = key
        self.cipher = AES.new(password+key, AES.MODE_CBC)



