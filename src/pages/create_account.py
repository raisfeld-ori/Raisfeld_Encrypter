from src.gui.create_account import Ui_Form
from PyQt6.QtWidgets import QWidget, QFileDialog
from src.User import User, get_random_bytes
from os.path import normpath
import logging
import fs


# implements Ui_MainWindow from sec.gui.create_account and adds functionality
class CreateAccount(Ui_Form, QWidget):
    def __init__(self, login_page):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.Cancel.clicked.connect(self.cancel)
        self.Create_account.clicked.connect(self.create_user)
        self.login_page = login_page

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
        if self.Key.isChecked():
            key = get_random_bytes(16)
            user = User(self.Name.text(), self.Password.text(), key)
        else:
            key = None
            user = User(self.Name.text(), self.Password.text())

        # if there's a key, save it
        if key:
            file_dir, _ = QFileDialog.getSaveFileName(
                parent=self,
                caption="select where to hide the key",
            )
            file_dir = normpath(file_dir)
            if not file_dir:
                return
            try:
                fs.write_file(file_dir, key)
            except Exception as e:
                logging.log(logging.ERROR, e)
                self.Error.setText(f"unexpected error, could not create the account")
        e = user.create()
        if e:
            logging.log(logging.ERROR, e)
            self.Error.setText(f"unexpected error, could not create the account")