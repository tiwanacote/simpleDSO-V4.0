# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zmatkar/projekty/moje/python/simpleDSO/UI/simpleUI.ui'
#
# Created: Sat Apr 24 20:41:40 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 692)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon2/icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gwScreen = QtGui.QGraphicsView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gwScreen.sizePolicy().hasHeightForWidth())
        self.gwScreen.setSizePolicy(sizePolicy)
        self.gwScreen.setMinimumSize(QtCore.QSize(640, 480))
        self.gwScreen.setMaximumSize(QtCore.QSize(640, 480))
        self.gwScreen.setInteractive(True)
        self.gwScreen.setObjectName("gwScreen")
        self.verticalLayout_2.addWidget(self.gwScreen)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.updateValue = QtGui.QSpinBox(self.groupBox_2)
        self.updateValue.setMinimum(50)
        self.updateValue.setMaximum(9999)
        self.updateValue.setProperty("value", 1000)
        self.updateValue.setObjectName("updateValue")
        self.horizontalLayout_2.addWidget(self.updateValue)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 25))
        self.menubar.setObjectName("menubar")
        self.menuAction = QtGui.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAction.addAction(self.actionAbout)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionExit)
        self.menubar.addAction(self.menuAction.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.menubar, QtCore.SIGNAL("triggered(QAction*)"), MainWindow.processAction)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), MainWindow.loadDataFromDso)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), MainWindow.loadScreenFromDso)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), MainWindow.saveProgramScreen)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), MainWindow.setAutoUpdate)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("clicked(bool)"), self.updateValue.setEnabled)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked(bool)"), self.checkBox.setOn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "DSO screenshoter", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Loads data from DSO and paint wave by yourselves", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Load data from DSO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Save data to CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setToolTip(QtGui.QApplication.translate("MainWindow", "Load screen data from DSO and paint them to program view", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Screenshot from DSO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setToolTip(QtGui.QApplication.translate("MainWindow", "Save programs view to file", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Save program screen", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Auto load data from DSO", None, QtGui.QApplication.UnicodeUTF8))
        self.updateValue.setSuffix(QtGui.QApplication.translate("MainWindow", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAction.setTitle(QtGui.QApplication.translate("MainWindow", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

