from src.gui.vault_creation import Ui_Raisfeld_security
from src.pages.loading import Loading
from PyQt6.QtWidgets import QWidget, QFileDialog
from PyQt6.QtCore import pyqtSignal
from src.User import Vault, User, estimate_time
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

        self.next_window = None
        self.Create_vault.clicked.connect(self.create_vault)
        self.Select_dir.clicked.connect(self.select_dir)

    def closeEvent(self, a0): self.previous_page.show()

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

        def vault_creation(task_signal: pyqtSignal, err_signal: pyqtSignal):
            try:
                self.vault_name = self.Vault_name.text()
                task_signal.emit("reading the file")
                try:
                    self.data = fast_fs.read_file(self.vault_dir)
                except Exception as e:
                    print(e)
                    err_signal.emit("failed to read the file")
                    return
                task_signal.emit("creating the vault")
                vault = Vault(self.vault_name, self.user, self.data)
                task_signal.emit("adding the vault to the user's vaults")
                self.user.vaults.append(vault)
                task_signal.emit("updating the main page")
                self.previous_page.update_user(self.user)
            except Exception as e:
                print(e)
        duration = estimate_time(self.vault_dir)
        if not duration:
            self.Error.setText("failed to locate the file in the vault")
            return

        self.next_window = Loading(self, self.previous_page, "creating the vault",
                                   int(duration),
                                   vault_creation,
                                   5,
                                   True,
                                   "reading vault name")
        self.next_window.show()
        self.hide()
