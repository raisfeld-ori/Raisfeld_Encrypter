from src.gui.login_page import Ui_MainWindow
from src.pages.create_account import CreateAccount
from src.pages.main_page import MainPage
from src.pages.loading import Loading
from src.User import User
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtCore import pyqtSignal
from typing import Optional
import fast_fs


# implements Ui_MainWindow from sec.gui.login_page and adds functionality
class LoginPage(Ui_MainWindow, QMainWindow):
    Error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.next_window = None
        self.key: Optional[bytes] = None

        self.Create.clicked.connect(self.create_account)
        self.Error_signal.connect(self.set_error)
        self.Open_key.clicked.connect(self.add_key)
        self.Login.clicked.connect(self.login)

    def add_key(self):
        file, _ = QFileDialog.getOpenFileName(parent=self, caption="select the key file")
        if not file:
            return
        self.key = fast_fs.read_file(file)
        self.Key_name.setText(file)

    def login(self):
        self.Error.setText("")
        if self.Password.text() == "":
            self.Error.setText("password cannot be empty")
            return
        user = User(self.Name.text(), self.Password.text(), self.key)

        def load_user(task_signal: pyqtSignal, end_signal: pyqtSignal):
            err = user.load()
            if type(err) is str:
                print(err)
                self.Error_signal.emit(err)
                end_signal.emit()
            self.next_window.next_window.update_user(user)
            task_signal.emit("done")
        self.next_window = MainPage(user, just_created=False)
        self.next_window = Loading(self, self.next_window, "loading the user", 0, load_user, 2, True, "making sure a user exists")
        self.next_window.show()
        self.next_window.showMaximized()
        self.hide()

    def set_error(self, err: str):
        self.Error.setText(err)

    # opens the CreateAccount page and closes this page
    def create_account(self):
        self.next_window = CreateAccount(self)
        self.next_window.show()
        self.next_window.showMaximized()
        self.close()
