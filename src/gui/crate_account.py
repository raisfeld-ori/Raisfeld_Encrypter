# Form implementation generated from reading ui file 'create_account.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1091, 774)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../raisfeld-encrypter-website/static/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#centralwidget {background-color:rgba(20, 20, 20, 250);}\n"
"#Form {background-color:rgba(20, 20, 20, 250);}\n"
"QMainWindow{background-color:rgba(20, 20, 20, 250);}\n"
"\n"
"QWidget{\n"
"    color:rgba(249, 249, 249, 240);\n"
"}\n"
"\n"
"QMenuBar{background-color:rgba(20, 20, 20, 250);}\n"
"QMenu{background-color:rgba(20, 20, 20, 250);}\n"
"QMenu::item:selected{background-color:rgba(229, 229, 229, 100);}\n"
"QMenuBar::item:selected{background-color:rgba(229, 229, 229, 100);}\n"
"QListWidget{background-color:rgba(20, 20, 20, 250);}\n"
"QSpinBox{background-color:rgba(20, 20, 20, 250);}\n"
"\n"
"QMenu::separator{height:5px; background-color:rgba(191, 191, 191, 100);}\n"
"\n"
"QComboBox {\n"
"    color:rgba(193, 193, 193, 250);\n"
"    background-color:rgba(29, 29, 29, 250);\n"
"    border:none;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    color:rgba(193, 193, 193, 250);\n"
"    background-color:rgba(29, 29, 29, 250);\n"
"    border:none;\n"
"}\n"
"QLineEdit {\n"
"    color:rgba(193, 193, 193, 250);\n"
"    background-color:rgba(29, 29, 29, 250);\n"
"    border:none;\n"
"}\n"
"QTextEdit {\n"
"    color:rgba(193, 193, 193, 250);\n"
"    background-color:rgba(29, 29, 29, 250);\n"
"    border:none;\n"
"}\n"
"QProgressBar {\n"
"     border: 0px solid grey;\n"
"     border-radius: 0px;\n"
"     background-color:rgba(255, 255, 255, 0);\n"
"    color:rgba(255, 255, 255, 0);\n"
" }\n"
"QProgressBar::chunk\n"
"{\n"
"background-color: rgb(208, 46, 213);\n"
"}\n"
"QTableWidget {\n"
"    background-color: rgba(29, 29, 29, 250);\n"
"    color: rgba(193, 193, 193, 250);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(50, 50, 50, 250);\n"
"}\n"
"\n"
"QTableWidget::item:focus {\n"
"    background-color: rgba(70, 70, 70, 250);\n"
"    outline: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(50, 50, 50, 250);\n"
"    color: rgba(193, 193, 193, 250);\n"
"    padding: 4px;\n"
"    border: none;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: rgba(50, 50, 50, 250);\n"
"    color: rgba(193, 193, 193, 250);\n"
"    padding: 4px;\n"
"    border: none;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"    background-color: rgba(70, 70, 70, 250);\n"
"}\n"
" QTableView QTableCornerButton::section {\n"
"    background-color: rgba(50, 50, 50, 250);\n"
" }\n"
"\n"
"QPushButton{background-color:rgba(59, 59, 59, 250);}\n"
"QPushButton:hover{background-color:rgba(107, 107, 107, 250);}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("qproperty-alignment: \'AlignLeft\';")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.Name = QtWidgets.QLineEdit(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(18)
        self.Name.setFont(font)
        self.Name.setStyleSheet("qproperty-alignment: \'AlignLeft\';")
        self.Name.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading)
        self.Name.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.Name.setObjectName("Name")
        self.verticalLayout.addWidget(self.Name)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("qproperty-alignment: \'AlignLeft\';")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Password = QtWidgets.QLineEdit(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(18)
        self.Password.setFont(font)
        self.Password.setStyleSheet("qproperty-alignment: \'AlignLeft\';")
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.Password.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading)
        self.Password.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.Password.setObjectName("Password")
        self.verticalLayout.addWidget(self.Password)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.Key = QtWidgets.QCheckBox(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.Key.setFont(font)
        self.Key.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Key.setObjectName("Key")
        self.verticalLayout.addWidget(self.Key)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.Create_account = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.Create_account.setFont(font)
        self.Create_account.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Create_account.setObjectName("Create_account")
        self.verticalLayout.addWidget(self.Create_account)
        self.Error = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(16)
        self.Error.setFont(font)
        self.Error.setStyleSheet("color:red;")
        self.Error.setText("")
        self.Error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Error.setObjectName("Error")
        self.verticalLayout.addWidget(self.Error)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.Cancel = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.Cancel.setFont(font)
        self.Cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Cancel.setObjectName("Cancel")
        self.verticalLayout_2.addWidget(self.Cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Raisfeld encrypter"))
        self.label.setText(_translate("Form", "Create a new account"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label_3.setText(_translate("Form", "Password"))
        self.label_4.setText(_translate("Form", "additional security:"))
        self.Key.setText(_translate("Form", "add an account key"))
        self.Create_account.setText(_translate("Form", "create the account"))
        self.Cancel.setText(_translate("Form", "cancel"))
