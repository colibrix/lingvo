from PyQt5.QtWidgets import QApplication
import sys
from model.Dictionary import Dictionary


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainDictionary = Dictionary()
    sys.exit(app.exec_())