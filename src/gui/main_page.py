# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 823)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(12)
        MainWindow.setFont(font)
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
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Save = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.verticalLayout.addWidget(self.Save)
        self.New = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.New.setFont(font)
        self.New.setObjectName("New")
        self.verticalLayout.addWidget(self.New)
        self.Open = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.Open.setFont(font)
        self.Open.setObjectName("Open")
        self.verticalLayout.addWidget(self.Open)
        self.Delete = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(20)
        self.Delete.setFont(font)
        self.Delete.setObjectName("Delete")
        self.verticalLayout.addWidget(self.Delete)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 4, 1, 1, 2)
        self.Name = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(26)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.gridLayout.addWidget(self.Name, 1, 0, 1, 3, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.Search = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(18)
        self.Search.setFont(font)
        self.Search.setObjectName("Search")
        self.gridLayout.addWidget(self.Search, 3, 0, 1, 3)
        self.List = QtWidgets.QListWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(18)
        self.List.setFont(font)
        self.List.setObjectName("List")
        self.gridLayout.addWidget(self.List, 4, 0, 1, 1)
        self.Error = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(12)
        self.Error.setFont(font)
        self.Error.setStyleSheet("color:red;")
        self.Error.setText("")
        self.Error.setObjectName("Error")
        self.gridLayout.addWidget(self.Error, 5, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1097, 46))
        font = QtGui.QFont()
        font.setFamily("Secular One")
        font.setPointSize(16)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.actionauto_save = QtGui.QAction(parent=MainWindow)
        self.actionauto_save.setObjectName("actionauto_save")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Save.setText(_translate("MainWindow", "save vaults"))
        self.New.setText(_translate("MainWindow", "New vault"))
        self.Open.setText(_translate("MainWindow", "Open vault"))
        self.Delete.setText(_translate("MainWindow", "Delete vault"))
        self.Name.setText(_translate("MainWindow", "welcome back (name)!"))
        self.actionauto_save.setText(_translate("MainWindow", "auto save"))
