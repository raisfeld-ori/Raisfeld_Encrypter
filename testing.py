"""
this is the testing directory,
just import the class you want to test,
create a class that inherits TestCase,
and then add your tests as class functions
"""
from unittest import TestCase

# testing the rust_src.fs directory
class TestFS(TestCase):
    def test_directory(self):
        import fs
        fs.create_dir("example")
        fs.write_file("example\\example.txt", b"test")
        fs.write_file("example\\examplee.txt", b"this works!!")
        print(fs.read_file("example\\example.txt"))