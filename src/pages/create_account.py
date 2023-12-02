import os.path

from gui.create_account import Ui_Form
from PyQt6.QtWidgets import QWidget, QFileDialog
from User import User, get_random_bytes
from os.path import normpath
from pages.main_page import MainPage
from typing import Optional
import logging
import fast_fs


# implements Ui_MainWindow from sec.gui.create_account and adds functionality
class CreateAccount(Ui_Form, QWidget):
    def __init__(self, login_page):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.Cancel.clicked.connect(self.cancel)
        self.Create_account.clicked.connect(self.create_user)
        self.login_page = login_page
        self.main_page = None

    # return to previous page
    def cancel(self):
        self.login_page.show()
        self.login_page.showMaximized()
        self.close()

    def create_user(self):

        # checks for invalid accounts
        self.Error.setText("")
        if len(self.Name.text()) == 0:
            self.Error.setText("Name must be more than 1 character long")
            return
        elif len(self.Password.text()) == 0:
            self.Error.setText("Password must be more than 1 character long")
            return

        # if there's no key, then just create a user
        if not self.Key.isChecked():
            user = User(self.Name.text(), self.Password.text())
        # if there is a key, also save that key
        else:
            key = get_random_bytes(16)
            user = User(self.Name.text(), self.Password.text(), key)

            file_dir, _ = QFileDialog.getSaveFileName(
                parent=self,
                caption="select where to hide the key",
            )
            if not file_dir:
                return
            file_dir = normpath(file_dir)
            if not file_dir:
                return
            try:
                fast_fs.write_file(file_dir, key)
            except Exception as e:
                logging.log(logging.ERROR, e)
                self.Error.setText(f"unexpected error, could not create the account")

        if os.path.exists(user.dir):
            self.Error.setText("a user with that name already exists")
            return

        # user.create() could return an error, so e is not user, it's Exception
        e: Optional[Exception] = user.create()
        if e:
            logging.log(logging.ERROR, e)
            self.Error.setText(f"unexpected error, could not create the account")

        # next page
        self.main_page = MainPage(user, True)
        self.main_page.show()
        self.close()
