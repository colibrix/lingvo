# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WordsByInitialForm(object):
    def setupUi(self, WordsByInitialForm):
        WordsByInitialForm.setObjectName("WordsByInitialForm")
        WordsByInitialForm.resize(593, 473)
        self.okButton = QtWidgets.QDialogButtonBox(WordsByInitialForm)
        self.okButton.setGeometry(QtCore.QRect(480, 430, 91, 32))
        self.okButton.setOrientation(QtCore.Qt.Horizontal)
        self.okButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.okButton.setObjectName("okButton")
        self.wordsTableByInitForm = QtWidgets.QTableWidget(WordsByInitialForm)
        self.wordsTableByInitForm.setGeometry(QtCore.QRect(10, 20, 561, 401))
        self.wordsTableByInitForm.setObjectName("wordsTableByInitForm")
        self.wordsTableByInitForm.setColumnCount(4)
        self.wordsTableByInitForm.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTableByInitForm.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTableByInitForm.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTableByInitForm.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTableByInitForm.setHorizontalHeaderItem(3, item)
        self.wordsTableByInitForm.horizontalHeader().setDefaultSectionSize(139)
        self.deleteWordFromGroup = QtWidgets.QPushButton(WordsByInitialForm)
        self.deleteWordFromGroup.setGeometry(QtCore.QRect(260, 430, 191, 26))
        self.deleteWordFromGroup.setObjectName("deleteWordFromGroup")

        self.retranslateUi(WordsByInitialForm)
        self.okButton.accepted.connect(WordsByInitialForm.accept)
        self.okButton.rejected.connect(WordsByInitialForm.reject)
        QtCore.QMetaObject.connectSlotsByName(WordsByInitialForm)

    def retranslateUi(self, WordsByInitialForm):
        _translate = QtCore.QCoreApplication.translate
        WordsByInitialForm.setWindowTitle(_translate("WordsByInitialForm", "Dialog"))
        item = self.wordsTableByInitForm.horizontalHeaderItem(0)
        item.setText(_translate("WordsByInitialForm", "Word"))
        item = self.wordsTableByInitForm.horizontalHeaderItem(1)
        item.setText(_translate("WordsByInitialForm", "Initial form"))
        item = self.wordsTableByInitForm.horizontalHeaderItem(2)
        item.setText(_translate("WordsByInitialForm", "Frequency"))
        item = self.wordsTableByInitForm.horizontalHeaderItem(3)
        item.setText(_translate("WordsByInitialForm", "Tags"))
        self.deleteWordFromGroup.setText(_translate("WordsByInitialForm", "Delete word from group"))
