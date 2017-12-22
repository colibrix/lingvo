# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addNewWord.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddNewWordDialog(object):
    def setupUi(self, AddNewWordDialog):
        AddNewWordDialog.setObjectName("AddNewWordDialog")
        AddNewWordDialog.resize(363, 247)
        self.newAddLine = QtWidgets.QLineEdit(AddNewWordDialog)
        self.newAddLine.setGeometry(QtCore.QRect(140, 50, 121, 31))
        self.newAddLine.setObjectName("newAddLine")
        self.label = QtWidgets.QLabel(AddNewWordDialog)
        self.label.setGeometry(QtCore.QRect(90, 60, 41, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddNewWordDialog)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 91, 17))
        self.label_2.setObjectName("label_2")
        self.tagInAddingFialog = QtWidgets.QComboBox(AddNewWordDialog)
        self.tagInAddingFialog.setGeometry(QtCore.QRect(140, 106, 85, 31))
        self.tagInAddingFialog.setObjectName("tagInAddingFialog")
        self.newTAG = QtWidgets.QLabel(AddNewWordDialog)
        self.newTAG.setGeometry(QtCore.QRect(60, 160, 67, 17))
        self.newTAG.setObjectName("newTAG")
        self.addWordPushButton = QtWidgets.QPushButton(AddNewWordDialog)
        self.addWordPushButton.setGeometry(QtCore.QRect(276, 210, 71, 26))
        self.addWordPushButton.setObjectName("addWordPushButton")
        self.cancelPushButton = QtWidgets.QPushButton(AddNewWordDialog)
        self.cancelPushButton.setGeometry(QtCore.QRect(190, 210, 71, 26))
        self.cancelPushButton.setObjectName("cancelPushButton")

        self.retranslateUi(AddNewWordDialog)
        QtCore.QMetaObject.connectSlotsByName(AddNewWordDialog)

    def retranslateUi(self, AddNewWordDialog):
        _translate = QtCore.QCoreApplication.translate
        AddNewWordDialog.setWindowTitle(_translate("AddNewWordDialog", "Add new word"))
        self.label.setText(_translate("AddNewWordDialog", "Word:"))
        self.label_2.setText(_translate("AddNewWordDialog", "Choose tag:"))
        self.newTAG.setText(_translate("AddNewWordDialog", "TextLabel"))
        self.addWordPushButton.setText(_translate("AddNewWordDialog", "Add"))
        self.cancelPushButton.setText(_translate("AddNewWordDialog", "Cancel"))
