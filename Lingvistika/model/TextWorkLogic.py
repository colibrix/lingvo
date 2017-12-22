from PyQt5.QtWidgets import QDialog

from gui.TextWorkView import Ui_WorkWithText


class TextWorkLogic(QDialog, Ui_WorkWithText):
    def __init__(self, parent=None):
        super(TextWorkLogic, self).__init__(parent)
        self.setupUi(self)
