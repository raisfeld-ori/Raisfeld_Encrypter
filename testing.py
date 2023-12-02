"""
this is the testing directory,
just import the class you want to test,
create a class that inherits TestCase,
and then add your tests as class functions
"""
from unittest import TestCase
import src.User
import fast_fs
import time
from src.User import User, Vault
from src.pages.loading import Loading
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import pyqtSignal
from os.path import getsize

# testing the rust_src.fast_fs directory
class TestFS(TestCase):
    def test_directory(self):
        fast_fs.create_dir("example")
        fast_fs.write_file("example\\example.txt", b"test")
        fast_fs.write_file("example\\not_example.txt", b"this works!!")
        print(fast_fs.read_file("example\\example.txt"))

    def test_estimation(self):
        file = r"C:\Users\raisf\Desktop\projects\large"
        print((getsize(file) / 1073741824) * 20)

class TestEncryption(TestCase):
    def test_key(self):
        src.User.get_random_bytes(16)

    def test_encryption(self):
        try:
            value = fast_fs.read_file("large")
            before = time.time()
            password = "1234"
            cipher = src.User.Cipher(password)
            encrypted_data = cipher.encrypt(value)
            if not encrypted_data:
                raise "failed due to memory issues"
            after = time.time() - before
            print(f"time taken: {after}")
        except Exception as e:
            print(e)

    def test_decryption(self):
        value = fast_fs.read_file("large")
        password = "1234"
        cipher = src.User.Cipher(password)
        encrypted = cipher.encrypt(value)
        if not encrypted:
            raise "failed due to memory issues"
        cipher = src.User.Cipher(password)
        print(cipher.decrypt(encrypted))


class TestUser(TestCase):
    def test_creation(self):
        usr = User("example", "example")
        usr.create()

    def test_save(self):
        usr = User("example", "example")
        usr.create()
        usr.vaults.append(Vault("example", usr, b"example"))
        usr.save()

    def test_loading(self):
        usr = User("example", "example")
        usr.create()
        usr.load()
        print(usr[0])


class TestLoading(TestCase):
    def test_task(self):
        self.err_signal = pyqtSignal(str)

        def foo(signal: pyqtSignal, _):
            time.sleep(2)
            signal.emit("")

        app = QApplication([])
        self.loader = Loading(None, None,"doing something", 2, foo, 2, None,"testing")
        self.loader.show()
        app.exec()

    def on_error(self, err: str):
        print("error: ", err)



"""
def average_time(amount: int = 10):
    result: list[float] = []
    for i in range(amount):
        start = time.time()
        cipher = src.User.Cipher("12345")
        file = fast_fs.read_file("large")
        file = cipher.encrypt(file)
        cipher = src.User.Cipher("12345")
        cipher.decrypt(file)
        end = time.time()-start
        result.append(end)
        print(f"{i}: time taken: {end}, current average: {sum(result) / len(result)}")
    print(f"final average time: {sum(result) / len(result)}")

average_time()
# estimated by: 10 times of reading and encrypting a file
# average for 2gb: 34 seconds
# average for 4gb: 61 seconds

# estimated by: 10 times of reading, encrypting and decrypting
# average for 2gb: 52 seconds
# average for 4gb: 100 seconds
"""