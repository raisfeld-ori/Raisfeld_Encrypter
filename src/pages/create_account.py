from src.gui.create_account import Ui_Form
from PyQt6.QtWidgets import QWidget


# implements Ui_MainWindow from sec.gui.create_account and adds functionality
class CreateAccount(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)