from PyQt5.QtWidgets import QDialog

from gui.DialogFormInfo import Ui_WordsByInitialForm


class DialogFormLogic(QDialog, Ui_WordsByInitialForm):
    def __init__(self, parent=None):
        super(DialogFormLogic, self).__init__(parent)
        self.setupUi(self)
