from PyQt5.QtWidgets import QDialog

from gui.GroupView import Ui_GroupsDialog


class GroupViewLogic(QDialog, Ui_GroupsDialog):
    def __init__(self, parent=None):
        super(GroupViewLogic, self).__init__(parent)
        self.setupUi(self)
