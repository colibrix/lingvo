from PyQt5.QtWidgets import QDialog

from gui.AddWord import Ui_AddNewWordDialog


class AddWordLogic(QDialog, Ui_AddNewWordDialog):
    def __init__(self, parent=None):
        super(AddWordLogic, self).__init__(parent)
        self.setupUi(self)
