import fast_fs

from src.gui import main_page
from PyQt6.QtWidgets import QMainWindow, QFileDialog
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

        # if the user was just made, then saying "Welcome back!" doesn't make any sense
        if just_created:
            self.Name.setText(f"Hi {user.name}!")
        else:
            self.Name.setText(f"Welcome back {user.name}!")

        self.New.clicked.connect(self.create_vault)
        self.List.doubleClicked.connect(self.open_vault)
        self.Delete.clicked.connect(self.delete_vault)

        self.update_user(self.user)

    def closeEvent(self, a0):
        self.close()
        self.user.save()

    def open_vault(self, item: QModelIndex):
        data = self.user[item.row()]
        file_selection, _ = QFileDialog.getSaveFileName(parent=self, caption="select where to save")
        if not file_selection:
            return
        else:
            fast_fs.write_file(file_selection, data)

    # open the "VaultCreation" window, and hide this window
    # after getting a response from VaultCreation, the function ret_vault will run
    def create_vault(self):
        self.new_vault = VaultCreation(self, self.user)
        self.new_vault.show()
        self.hide()

    def delete_vault(self):
        self.user.vaults.pop(self.List.currentRow())
        self.update_user(self.user)

    # this is the function that happens after creating a new vault
    def update_user(self, new: User):
        self.user = new
        self.List.clear()
        for item in self.user.vaults:
            self.List.addItem(item.name)
