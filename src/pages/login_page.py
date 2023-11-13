from src.gui.login_page import Ui_MainWindow
from src.pages.create_account import CreateAccount
from PyQt6.QtWidgets import QMainWindow


# implements Ui_MainWindow from sec.gui.login_page and adds functionality
class LoginPage(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.next_window = None

        self.Create.clicked.connect(self.create_account)

    # opens the CreateAccount page and closes this page
    def create_account(self):
        self.next_window = CreateAccount(self)
        self.next_window.show()
        self.next_window.showMaximized()
        self.close()
