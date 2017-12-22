from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from gui.DialogWordInfo import Ui_Description


class DialogWordInfoLogic(QDialog, Ui_Description):
    def __init__(self, parent=None):
        super(DialogWordInfoLogic, self).__init__(parent)
        self.setupUi(self)








