from src.gui import main_page
from PyQt6.QtWidgets import QMainWindow
from src.User import User


class MainPage(main_page.Ui_MainWindow, QMainWindow):
    def __init__(self, user: User, just_created: bool):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.user = user

        # if the user was just made, then saying "Welcome back!" doesn't make any sense
        if just_created:
            self.Name.setText(f"Hi {user.name}!")
        else:
            self.Name.setText(f"Welcome back {user.name}!")

    def create_vault(self):
        vault_name = self.user.dir
