# Form implementation generated from reading ui file 'login_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 789)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../raisfeld-encrypter-website/static/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#centralwidget {background-color:rgba(20, 20, 20, 250);}\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(48)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("qproperty-alignment: \'AlignLeft\';")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Name = QtWidgets.QLineEdit(parent=self.centralwidget)
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
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
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
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.Password = QtWidgets.QLineEdit(parent=self.centralwidget)
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
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Open_key = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Open_key.sizePolicy().hasHeightForWidth())
        self.Open_key.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(18)
        self.Open_key.setFont(font)
        self.Open_key.setObjectName("Open_key")
        self.horizontalLayout_2.addWidget(self.Open_key)
        self.Key_name = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Key_name.sizePolicy().hasHeightForWidth())
        self.Key_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(16)
        self.Key_name.setFont(font)
        self.Key_name.setAutoFillBackground(False)
        self.Key_name.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.Key_name.setText("")
        self.Key_name.setObjectName("Key_name")
        self.horizontalLayout_2.addWidget(self.Key_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.Login = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.Login.setFont(font)
        self.Login.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Login.setObjectName("Login")
        self.verticalLayout.addWidget(self.Login)
        self.Error = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.Error.setFont(font)
        self.Error.setStyleSheet("color:red;")
        self.Error.setText("")
        self.Error.setObjectName("Error")
        self.verticalLayout.addWidget(self.Error, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.Create = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(16)
        self.Create.setFont(font)
        self.Create.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Create.setObjectName("Create")
        self.horizontalLayout.addWidget(self.Create)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Raisfeld encrypter"))
        self.label_3.setText(_translate("MainWindow", "Welcome!"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_6.setText(_translate("MainWindow", "add a security key"))
        self.Open_key.setText(_translate("MainWindow", "open"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.label_4.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.Create.setText(_translate("MainWindow", "create a new account"))
