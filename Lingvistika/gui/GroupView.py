# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GroupsDialog(object):
    def setupUi(self, GroupsDialog):
        GroupsDialog.setObjectName("GroupsDialog")
        GroupsDialog.resize(781, 551)
        self.tableOfGroups = QtWidgets.QTableWidget(GroupsDialog)
        self.tableOfGroups.setGeometry(QtCore.QRect(10, 10, 761, 491))
        self.tableOfGroups.setObjectName("tableOfGroups")
        self.tableOfGroups.setColumnCount(2)
        self.tableOfGroups.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableOfGroups.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableOfGroups.setHorizontalHeaderItem(1, item)
        self.tableOfGroups.horizontalHeader().setDefaultSectionSize(378)
        self.okButtonInGroupDialog = QtWidgets.QPushButton(GroupsDialog)
        self.okButtonInGroupDialog.setGeometry(QtCore.QRect(680, 510, 97, 26))
        self.okButtonInGroupDialog.setObjectName("okButtonInGroupDialog")
        self.deleteGroup = QtWidgets.QPushButton(GroupsDialog)
        self.deleteGroup.setGeometry(QtCore.QRect(570, 510, 97, 26))
        self.deleteGroup.setObjectName("deleteGroup")

        self.retranslateUi(GroupsDialog)
        QtCore.QMetaObject.connectSlotsByName(GroupsDialog)

    def retranslateUi(self, GroupsDialog):
        _translate = QtCore.QCoreApplication.translate
        GroupsDialog.setWindowTitle(_translate("GroupsDialog", "All groups"))
        item = self.tableOfGroups.horizontalHeaderItem(0)
        item.setText(_translate("GroupsDialog", "Begin form"))
        item = self.tableOfGroups.horizontalHeaderItem(1)
        item.setText(_translate("GroupsDialog", "Words in group"))
        self.okButtonInGroupDialog.setText(_translate("GroupsDialog", "OK"))
        self.deleteGroup.setText(_translate("GroupsDialog", "Delete group"))
