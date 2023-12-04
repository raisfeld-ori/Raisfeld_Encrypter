import fast_fs

from src.gui import main_page
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtCore import QModelIndex, pyqtSignal
from src.User import User
from src.pages.vault_creation import VaultCreation
from src.pages.loading import Loading

class MainPage(main_page.Ui_Raisfeld_encrypter, QMainWindow):
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
        self.Save.clicked.connect(self.save_user)

        self.update_user(self.user)

    def closeEvent(self, a0):
        self.save_user(True)
        self.close()

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

    def save_user(self, final: bool = False):
        def save_user(task: pyqtSignal, close: pyqtSignal):
            try:
                self.user.save()
            except:
                self.Error.setText("failed to save the new vaults")
                close.emit()
            task.emit("done")

        final = None if final else self
        # rough estimation
        vaults_time = int((sum([len(vault.data) for vault in self.user.vaults]) / 1073741824) * 10)
        self.next_window = Loading(self, final, "saving the vaults",
                                   vaults_time,
                                   save_user,
                                   2,
                                   True,
                                   "saving the vaults on the disk"
                                   )
        self.next_window.show()
        self.hide()
