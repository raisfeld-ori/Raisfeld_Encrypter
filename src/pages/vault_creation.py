from src.gui.vault_creation import Ui_Raisfeld_security
from PyQt6.QtWidgets import QWidget, QFileDialog
from src.User import Vault, User
import fast_fs


class VaultCreation(Ui_Raisfeld_security, QWidget):

    # including the previous page causes an import error
    # the type for previous_page is src.pages.create_account.MainPage
    def __init__(self, previous_page, user: User):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.previous_page = previous_page
        self.user = user
        self.vault_name = ""
        self.vault_dir = ""
        self.data = b""

        self.Create_vault.clicked.connect(self.create_vault)
        self.Select_dir.clicked.connect(self.select_dir)

    def select_dir(self):
        file_selection, _ = QFileDialog().getOpenFileName(parent=self, caption="select the file for the vault")
        if file_selection == "":
            return
        self.vault_dir = file_selection
        self.Vault_dir.setText(file_selection)

    def create_vault(self):
        self.Error.setText("")
        if self.vault_dir == "":
            self.Error.setText("No file selected, please select a file")
            return
        self.vault_name = self.Vault_name.text()
        self.data = fast_fs.read_file(self.vault_dir)
        vault = Vault(self.vault_name, self.user, self.data)
        self.previous_page.show()
        self.user.vaults.append(vault)
        self.previous_page.update_user(self.user)
        self.close()

