# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newview.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dictionary(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1166, 871)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 971, 801))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWords = QtWidgets.QTableWidget(self.tab)
        self.tableWords.setGeometry(QtCore.QRect(10, 50, 751, 711))
        self.tableWords.setAutoScrollMargin(16)
        self.tableWords.setIconSize(QtCore.QSize(0, 0))
        self.tableWords.setObjectName("tableWords")
        self.tableWords.setColumnCount(4)
        self.tableWords.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWords.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWords.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWords.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWords.setHorizontalHeaderItem(3, item)
        self.tableWords.horizontalHeader().setDefaultSectionSize(187)
        self.sortByWordButton = QtWidgets.QPushButton(self.tab)
        self.sortByWordButton.setGeometry(QtCore.QRect(780, 121, 161, 27))
        self.sortByWordButton.setObjectName("sortByWordButton")
        self.sortByFormButton = QtWidgets.QPushButton(self.tab)
        self.sortByFormButton.setGeometry(QtCore.QRect(780, 151, 161, 26))
        self.sortByFormButton.setObjectName("sortByFormButton")
        self.sortByFreqButton = QtWidgets.QPushButton(self.tab)
        self.sortByFreqButton.setGeometry(QtCore.QRect(780, 180, 161, 27))
        self.sortByFreqButton.setObjectName("sortByFreqButton")
        self.searchingWordLine = QtWidgets.QLineEdit(self.tab)
        self.searchingWordLine.setGeometry(QtCore.QRect(70, 10, 191, 27))
        self.searchingWordLine.setObjectName("searchingWordLine")
        self.serachWordButton = QtWidgets.QPushButton(self.tab)
        self.serachWordButton.setGeometry(QtCore.QRect(270, 10, 97, 26))
        self.serachWordButton.setObjectName("serachWordButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(810, 240, 131, 17))
        self.label.setObjectName("label")
        self.existingDictionaries = QtWidgets.QComboBox(self.tab)
        self.existingDictionaries.setGeometry(QtCore.QRect(780, 260, 161, 25))
        self.existingDictionaries.setObjectName("existingDictionaries")
        self.addNewWordInDictBtn = QtWidgets.QPushButton(self.tab)
        self.addNewWordInDictBtn.setGeometry(QtCore.QRect(780, 340, 161, 26))
        self.addNewWordInDictBtn.setObjectName("addNewWordInDictBtn")
        self.addNewGroupInDict = QtWidgets.QPushButton(self.tab)
        self.addNewGroupInDict.setGeometry(QtCore.QRect(780, 370, 161, 26))
        self.addNewGroupInDict.setObjectName("addNewGroupInDict")
        self.notFoundWordLabel = QtWidgets.QLabel(self.tab)
        self.notFoundWordLabel.setGeometry(QtCore.QRect(380, 10, 101, 17))
        self.notFoundWordLabel.setText("")
        self.notFoundWordLabel.setObjectName("notFoundWordLabel")
        self.dictionaryStatisticsButton = QtWidgets.QPushButton(self.tab)
        self.dictionaryStatisticsButton.setGeometry(QtCore.QRect(780, 430, 161, 51))
        self.dictionaryStatisticsButton.setObjectName("dictionaryStatisticsButton")
        self.refreshTable = QtWidgets.QPushButton(self.tab)
        self.refreshTable.setGeometry(QtCore.QRect(780, 50, 161, 26))
        self.refreshTable.setObjectName("refreshTable")
        self.clearSearchLine = QtWidgets.QPushButton(self.tab)
        self.clearSearchLine.setGeometry(QtCore.QRect(10, 10, 51, 26))
        self.clearSearchLine.setObjectName("clearSearchLine")
        self.textEditStatistics = QtWidgets.QTextEdit(self.tab)
        self.textEditStatistics.setEnabled(False)
        self.textEditStatistics.setGeometry(QtCore.QRect(780, 490, 161, 191))
        self.textEditStatistics.setObjectName("textEditStatistics")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 761, 741))
        self.textEdit.setObjectName("textEdit")
        self.inDictiionaryLabel = QtWidgets.QLabel(self.tab_2)
        self.inDictiionaryLabel.setGeometry(QtCore.QRect(790, 300, 91, 20))
        self.inDictiionaryLabel.setObjectName("inDictiionaryLabel")
        self.notInDictionaryLabel = QtWidgets.QLabel(self.tab_2)
        self.notInDictionaryLabel.setGeometry(QtCore.QRect(790, 330, 121, 17))
        self.notInDictionaryLabel.setObjectName("notInDictionaryLabel")
        self.severalTagsLAbel = QtWidgets.QLabel(self.tab_2)
        self.severalTagsLAbel.setGeometry(QtCore.QRect(790, 360, 81, 17))
        self.severalTagsLAbel.setObjectName("severalTagsLAbel")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 170, 141, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(790, 210, 141, 26))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableOfTags = QtWidgets.QTableWidget(self.tab_3)
        self.tableOfTags.setEnabled(True)
        self.tableOfTags.setGeometry(QtCore.QRect(130, 50, 721, 701))
        self.tableOfTags.setObjectName("tableOfTags")
        self.tableOfTags.setColumnCount(2)
        self.tableOfTags.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableOfTags.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableOfTags.setHorizontalHeaderItem(1, item)
        self.tableOfTags.horizontalHeader().setDefaultSectionSize(357)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1166, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.openNewTextFile = QtWidgets.QAction(MainWindow)
        self.openNewTextFile.setObjectName("openNewTextFile")
        self.saveInCurrentDictionary = QtWidgets.QAction(MainWindow)
        self.saveInCurrentDictionary.setObjectName("saveInCurrentDictionary")
        self.tagsInfo = QtWidgets.QAction(MainWindow)
        self.tagsInfo.setObjectName("tagsInfo")
        self.helpMenu = QtWidgets.QAction(MainWindow)
        self.helpMenu.setObjectName("helpMenu")
        self.saveInNewDictionary = QtWidgets.QAction(MainWindow)
        self.saveInNewDictionary.setObjectName("saveInNewDictionary")
        self.exitFromApplication = QtWidgets.QAction(MainWindow)
        self.exitFromApplication.setObjectName("exitFromApplication")
        self.showInfoAboutTags = QtWidgets.QAction(MainWindow)
        self.showInfoAboutTags.setObjectName("showInfoAboutTags")
        self.openNewDictionaryFile = QtWidgets.QAction(MainWindow)
        self.openNewDictionaryFile.setObjectName("openNewDictionaryFile")
        self.actionCreate_new_dictionary = QtWidgets.QAction(MainWindow)
        self.actionCreate_new_dictionary.setObjectName("actionCreate_new_dictionary")
        self.addNewTag = QtWidgets.QAction(MainWindow)
        self.addNewTag.setObjectName("addNewTag")
        self.addNewWord = QtWidgets.QAction(MainWindow)
        self.addNewWord.setObjectName("addNewWord")
        self.addNewWordAndTag = QtWidgets.QAction(MainWindow)
        self.addNewWordAndTag.setObjectName("addNewWordAndTag")
        self.actionAdd_new_word = QtWidgets.QAction(MainWindow)
        self.actionAdd_new_word.setObjectName("actionAdd_new_word")
        self.actionDelete_word_from_dictionary = QtWidgets.QAction(MainWindow)
        self.actionDelete_word_from_dictionary.setObjectName("actionDelete_word_from_dictionary")
        self.actionDelete_all_words = QtWidgets.QAction(MainWindow)
        self.actionDelete_all_words.setObjectName("actionDelete_all_words")
        self.menuFile.addAction(self.openNewTextFile)
        self.menuFile.addAction(self.openNewDictionaryFile)
        self.menuFile.addAction(self.saveInCurrentDictionary)
        self.menuFile.addAction(self.saveInNewDictionary)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exitFromApplication)
        self.menuAbout.addAction(self.helpMenu)
        self.menuSettings.addAction(self.actionDelete_all_words)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dictionary"))
        item = self.tableWords.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Word"))
        item = self.tableWords.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Initial form"))
        item = self.tableWords.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Frequency"))
        item = self.tableWords.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tags"))
        self.sortByWordButton.setText(_translate("MainWindow", "Sort by word"))
        self.sortByFormButton.setText(_translate("MainWindow", "Sort by form"))
        self.sortByFreqButton.setText(_translate("MainWindow", "Sort by frequency"))
        self.searchingWordLine.setPlaceholderText(_translate("MainWindow", "Enter searching word"))
        self.serachWordButton.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "List of dictionaries:"))
        self.addNewWordInDictBtn.setText(_translate("MainWindow", "Add new word"))
        self.addNewGroupInDict.setText(_translate("MainWindow", "Show all groups"))
        self.dictionaryStatisticsButton.setText(_translate("MainWindow", "Show dictionary\n"
"statistics"))
        self.refreshTable.setText(_translate("MainWindow", "Refresh table"))
        self.clearSearchLine.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Dictionary"))
        self.inDictiionaryLabel.setText(_translate("MainWindow", "In dictionary"))
        self.notInDictionaryLabel.setText(_translate("MainWindow", "Not in dictionary"))
        self.severalTagsLAbel.setText(_translate("MainWindow", "Several tags"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear input"))
        self.pushButton.setText(_translate("MainWindow", "Anotate text"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Text"))
        item = self.tableOfTags.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tag"))
        item = self.tableOfTags.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tags information"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuSettings.setTitle(_translate("MainWindow", "Options"))
        self.openNewTextFile.setText(_translate("MainWindow", "Open file..."))
        self.saveInCurrentDictionary.setText(_translate("MainWindow", "Save"))
        self.tagsInfo.setText(_translate("MainWindow", "Tags"))
        self.helpMenu.setText(_translate("MainWindow", "Help"))
        self.saveInNewDictionary.setText(_translate("MainWindow", "Save dictionary in new..."))
        self.exitFromApplication.setText(_translate("MainWindow", "Exit"))
        self.showInfoAboutTags.setText(_translate("MainWindow", "Info about tags"))
        self.openNewDictionaryFile.setText(_translate("MainWindow", "Open dictionary..."))
        self.actionCreate_new_dictionary.setText(_translate("MainWindow", "Create new dictionary..."))
        self.addNewTag.setText(_translate("MainWindow", "Add new tag"))
        self.addNewWord.setText(_translate("MainWindow", "Add new word"))
        self.addNewWordAndTag.setText(_translate("MainWindow", "Add word and tag"))
        self.actionAdd_new_word.setText(_translate("MainWindow", "Add new word"))
        self.actionDelete_word_from_dictionary.setText(_translate("MainWindow", "Delete word from dictionary"))
        self.actionDelete_all_words.setText(_translate("MainWindow", "Clean dictionary"))
