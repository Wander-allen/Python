# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'merge.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_btnMerge(object):
    def setupUi(self, btnMerge):
        btnMerge.setObjectName("btnMerge")
        btnMerge.resize(395, 243)
        self.centralwidget = QtWidgets.QWidget(btnMerge)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        btnMerge.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(btnMerge)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 26))
        self.menubar.setObjectName("menubar")
        btnMerge.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(btnMerge)
        self.statusbar.setObjectName("statusbar")
        btnMerge.setStatusBar(self.statusbar)

        self.retranslateUi(btnMerge)
        QtCore.QMetaObject.connectSlotsByName(btnMerge)

    def retranslateUi(self, btnMerge):
        _translate = QtCore.QCoreApplication.translate
        btnMerge.setWindowTitle(_translate("btnMerge", "MainWindow"))
        self.label.setText(_translate("btnMerge", "Boot-hex"))
        self.label_2.setText(_translate("btnMerge", "App-Hex"))
        self.pushButton.setText(_translate("btnMerge", "合并合成码"))