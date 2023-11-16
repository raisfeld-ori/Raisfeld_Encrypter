from src.gui import main_page
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QModelIndex
from src.User import User
from src.pages.vault_creation import VaultCreation


class MainPage(main_page.Ui_MainWindow, QMainWindow):
    def __init__(self, user: User, just_created: bool):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.user = user
        self.new_vault = None
        self.List.doubleClicked.connect(self.open_vault)

        # if the user was just made, then saying "Welcome back!" doesn't make any sense
        if just_created:
            self.Name.setText(f"Hi {user.name}!")
        else:
            self.Name.setText(f"Welcome back {user.name}!")

        self.New.clicked.connect(self.create_vault)

    def closeEvent(self, a0):
        self.close()
        self.user.save()

    def open_vault(self, item: QModelIndex):
        data = self.user.vaults[item.row()].get()
        print(data)

    # open the "VaultCreation" window, and hide this window
    # after getting a response from VaultCreation, the function ret_vault will run
    def create_vault(self):
        self.new_vault = VaultCreation(self, self.user)
        self.new_vault.show()
        self.hide()

    # this is the function that happens after creating a new vault
    def update_user(self, new: User):
        self.user = new
        try:
            self.List.clear()
            for item in self.user.vaults:
                self.List.addItem(item.name)
        except Exception as e:
            print(e)