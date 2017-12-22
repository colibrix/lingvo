# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Description(object):
    def setupUi(self, Description):
        Description.setObjectName("Description")
        Description.resize(645, 393)
        self.okCancelButton = QtWidgets.QDialogButtonBox(Description)
        self.okCancelButton.setGeometry(QtCore.QRect(450, 350, 181, 32))
        self.okCancelButton.setOrientation(QtCore.Qt.Horizontal)
        self.okCancelButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okCancelButton.setObjectName("okCancelButton")
        self.wordDescriptionTable = QtWidgets.QTableWidget(Description)
        self.wordDescriptionTable.setGeometry(QtCore.QRect(10, 140, 581, 171))
        self.wordDescriptionTable.setObjectName("wordDescriptionTable")
        self.wordDescriptionTable.setColumnCount(2)
        self.wordDescriptionTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.wordDescriptionTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordDescriptionTable.setHorizontalHeaderItem(1, item)
        self.wordDescriptionTable.horizontalHeader().setDefaultSectionSize(289)
        self.tags = QtWidgets.QComboBox(Description)
        self.tags.setGeometry(QtCore.QRect(490, 10, 91, 27))
        self.tags.setObjectName("tags")
        self.wordAndInitialFormTable = QtWidgets.QTableWidget(Description)
        self.wordAndInitialFormTable.setGeometry(QtCore.QRect(10, 10, 361, 111))
        self.wordAndInitialFormTable.setObjectName("wordAndInitialFormTable")
        self.wordAndInitialFormTable.setColumnCount(3)
        self.wordAndInitialFormTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.wordAndInitialFormTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordAndInitialFormTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordAndInitialFormTable.setHorizontalHeaderItem(2, item)
        self.wordAndInitialFormTable.horizontalHeader().setDefaultSectionSize(119)
        self.editInitialFormBtn = QtWidgets.QPushButton(Description)
        self.editInitialFormBtn.setGeometry(QtCore.QRect(390, 90, 201, 31))
        self.editInitialFormBtn.setCheckable(False)
        self.editInitialFormBtn.setChecked(False)
        self.editInitialFormBtn.setObjectName("editInitialFormBtn")
        self.lineEdit = QtWidgets.QLineEdit(Description)
        self.lineEdit.setGeometry(QtCore.QRect(390, 60, 201, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.deleteWordButton = QtWidgets.QPushButton(Description)
        self.deleteWordButton.setGeometry(QtCore.QRect(10, 350, 211, 31))
        self.deleteWordButton.setObjectName("deleteWordButton")
        self.label = QtWidgets.QLabel(Description)
        self.label.setGeometry(QtCore.QRect(400, 6, 81, 31))
        self.label.setObjectName("label")
        self.deleteSelectedTag = QtWidgets.QPushButton(Description)
        self.deleteSelectedTag.setGeometry(QtCore.QRect(230, 350, 151, 31))
        self.deleteSelectedTag.setObjectName("deleteSelectedTag")

        self.retranslateUi(Description)
        self.okCancelButton.accepted.connect(Description.accept)
        self.okCancelButton.rejected.connect(Description.reject)
        QtCore.QMetaObject.connectSlotsByName(Description)

    def retranslateUi(self, Description):
        _translate = QtCore.QCoreApplication.translate
        Description.setWindowTitle(_translate("Description", "Dialog"))
        item = self.wordDescriptionTable.horizontalHeaderItem(0)
        item.setText(_translate("Description", "Tag"))
        item = self.wordDescriptionTable.horizontalHeaderItem(1)
        item.setText(_translate("Description", "Tag Description"))
        item = self.wordAndInitialFormTable.horizontalHeaderItem(0)
        item.setText(_translate("Description", "Word"))
        item = self.wordAndInitialFormTable.horizontalHeaderItem(1)
        item.setText(_translate("Description", "Initial form"))
        item = self.wordAndInitialFormTable.horizontalHeaderItem(2)
        item.setText(_translate("Description", "Frequency"))
        self.editInitialFormBtn.setText(_translate("Description", "Edit initial form"))
        self.deleteWordButton.setText(_translate("Description", "Delete word from dictionary"))
        self.label.setText(_translate("Description", "Choose tag:"))
        self.deleteSelectedTag.setText(_translate("Description", "Delete selected tag"))
