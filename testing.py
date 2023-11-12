"""
this is the testing directory,
just import the class you want to test,
create a class that inherits TestCase,
and then add your tests as class functions
"""
from unittest import TestCase

import src.encryption
import fs


# testing the rust_src.fs directory
class TestFS(TestCase):
    # noinspection PyUnresolvedReferences
    def test_directory(self):
        fs.create_dir("example")
        fs.write_file("example\\example.txt", b"test")
        fs.write_file("example\\examplee.txt", b"this works!!")
        print(fs.read_file("example\\example.txt"))


class TestEncryption(TestCase):
    def test_key(self):
        key = src.encryption.create_key(16)

    def test_encryption(self):
        value = b"important data"
        password = "1234"
        cipher = src.encryption.Cipher(password)
        print(cipher.encrypt(value))

    def test_decryption(self):
        value = b"important data"
        password = "1234"
        cipher = src.encryption.Cipher(password)
        encrypted = cipher.encrypt(value)
        cipher = src.encryption.Cipher(password)
        print(cipher.decrypt(encrypted))
