import operator
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox, QInputDialog, QComboBox
from PyQt5.uic.properties import QtGui
from nltk import sent_tokenize

from model import Constants
from model.AddWordLogic import AddWordLogic
from model.ControllerCreator import *
from gui.DictionaryView import Ui_Dictionary
import os

from model.DialogFormLogic import DialogFormLogic
from model.DialogWordInfoLogic import DialogWordInfoLogic
from model.GroupViewLogic import GroupViewLogic
from model.TextWorkLogic import TextWorkLogic


class Dictionary(QtWidgets.QMainWindow, Ui_Dictionary):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # shortcuts for easier working
        self.exitFromApplication.setShortcut("Ctrl+Q")
        self.openNewTextFile.setShortcut("Ctrl+O")
        self.openNewDictionaryFile.setShortcut("Shift+Ctrl+O")
        self.saveInCurrentDictionary.setShortcut("Ctrl+S")
        self.saveInNewDictionary.setShortcut("Shift+Ctrl+S")

        # fill box with dictionaries
        self.fillComboBox()

        # PAY ATTENTION!
        # menu points
        # just connect with methods
        self.exitFromApplication.triggered.connect(self.close)
        self.openNewTextFile.triggered.connect(self.loadNewTextFile)
        self.openNewDictionaryFile.triggered.connect(self.loadNewDictionary)
        self.saveInCurrentDictionary.triggered.connect(self.justSaveDictionary)
        self.saveInNewDictionary.triggered.connect(self.saveInNewDictionaryFILENAME)
        self.actionDelete_all_words.triggered.connect(self.cleanDictionary)

        self.addNewWordInDictBtn.clicked.connect(self.addNewWordInDictionary)

        # methods for sorting buttons
        self.sortByWordButton.clicked.connect(self.sortByWord)
        self.sortByFreqButton.clicked.connect(self.sortByFrequency)
        self.sortByFormButton.clicked.connect(self.sortByBelongingToGroup)

        self.serachWordButton.clicked.connect(self.searchWordInTable)

        self.clearSearchLine.clicked.connect(self.clear_search_line)
        # sorted columns in tags table
        # just click on header
        self.tableOfTags.horizontalHeader().sectionClicked.connect(self.sortTags)

        self.refreshTable.clicked.connect(self.updateWordsTable)
        # default name of dictionary
        self.currentFilename = "untitled.txt"

        self.pushButton.clicked.connect(self.annotateText)
        self.pushButton_2.clicked.connect(self.clearInputText)
        self.dictionaryStatisticsButton.clicked.connect(self.showStatistics)
        self.groups = {}
        self.addNewGroupInDict.clicked.connect(self.showGroupsInDictionary)
        # current dictionary
        self.dictionary = {}
        self.tags = self.displayTagsInfo()
        self.tagReversed = False
        self.groupsDictionary = {}


        self.allWords = 0
        self.uniqueWords = 0

        # labels
        self.inDictiionaryLabel.setStyleSheet("color:'darkGreen'")
        self.notInDictionaryLabel.setStyleSheet("color:'red'")
        self.severalTagsLAbel.setStyleSheet("color:'magenta'")
        # for combo box with tags in edit window
        self.tags_list = []
        for i in self.tags:
            self.tags_list.append(i)
        self.tags_list.sort()

        self.tableWords.doubleClicked.connect(self.doubleClickChecked)

        self.show()

    newInfoWordWindow = None

    thisWord = ""

    groupsWindowDialog = None

    def updateStatistics(self):
        self.uniqueWords = 0
        self.allWords = 0


    def showStatistics(self):
        self.textEditStatistics.setText("")
        self.textEditStatistics.setEnabled(True)
        self.textEditStatistics.append("Unique words: " + str(self.uniqueWords))
        self.textEditStatistics.append("All words: " + str(self.allWords))


    strings = {}
    def deleteGroup(self):
        row = self.groupsWindowDialog.tableOfGroups.currentRow()
        col = self.groupsWindowDialog.tableOfGroups.currentColumn()
        beginForm = self.groupsWindowDialog.tableOfGroups.item(row, col)
        beginForm = beginForm.text()

        del self.strings[beginForm]
        self.updateGroupTable()

    def updateGroupTable(self):
        self.groupsWindowDialog.tableOfGroups.setRowCount(len(self.strings))
        row = 0
        for i in self.strings:
            self.groupsWindowDialog.tableOfGroups.setItem(row, 0, QTableWidgetItem(i))  # word
            self.groupsWindowDialog.tableOfGroups.setItem(row, 1, QTableWidgetItem(str(self.strings[i])))
            row += 1
    flag = 0

    def showGroupsInDictionary(self):

        if self.flag > 0:
            self.updateGroupTable()
        else:
            self.groupsWindowDialog = GroupViewLogic()
            self.groupsWindowDialog.deleteGroup.clicked.connect(self.deleteGroup)
            spisok = []
            for word in self.dictionary:
                initForm = self.dictionary[word][2]
                spisok.append(initForm)
            initFormDict =  {i:spisok.count(i) for i in spisok}
            s = initFormDict.keys()
            for k in s:
                str1 = "| "
                for word in self.dictionary:
                    init = self.dictionary[word][2]
                    if k == init:
                        str1 += word
                        str1 += " | "
                self.strings[k] = str1
            self.updateGroupTable()
            self.flag += 1

        self.groupsWindowDialog.okButtonInGroupDialog.clicked.connect(self.okBtnDialogGroup)
        self.groupsWindowDialog.exec_()

    def okBtnDialogGroup(self):
        self.groupsWindowDialog.close()

    def clear_search_line(self):
        self.searchingWordLine.setText("")

    def printSelectedText(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        print(textSelected)

    def searchWordInTable(self):
        current_word = self.searchingWordLine.text()
        if current_word == "":
            self.notFoundWordLabel.setStyleSheet("color: 'red'")
            self.notFoundWordLabel.setText("Please, enter word!")
            self.notFoundWordLabel.adjustSize()
            return

        else:
            if current_word in self.dictionary:
                self.notFoundWordLabel.setText("")
                self.showSearchingWordInTable(current_word)
            else:
                self.notFoundWordLabel.setStyleSheet("color: 'red'")
                self.notFoundWordLabel.setText("No such word!")




    def showSearchingWordInTable(self, current_word):
        self.tableWords.setRowCount(1)
        self.tableWords.setItem(0, 0, QTableWidgetItem(current_word))  # word
        self.tableWords.setItem(0, 1, QTableWidgetItem(str(self.dictionary[current_word][2])))  # initial form
        self.tableWords.setItem(0, 2, QTableWidgetItem(str(self.dictionary[current_word][0])))
        self.tableWords.setItem(0, 3, QTableWidgetItem(str(self.dictionary[current_word][1])))

    def infoWordWindow(self, col):
        row = self.tableWords.currentRow()
        item = self.tableWords.item(row, col)
        self.thisWord = item.text()

        self.newInfoWordWindow = DialogWordInfoLogic()
        self.newInfoWordWindow.setWindowTitle("Description")
        self.initDialogForm(self.thisWord, self.newInfoWordWindow)

        self.newInfoWordWindow.tags.addItems(self.tags_list)
        self.newInfoWordWindow.tags.adjustSize()
        self.newInfoWordWindow.tags.activated[str].connect(self.onActivatedTag)
        self.newInfoWordWindow.deleteWordButton.clicked.connect(self.deleteWordFromDictionary)

        tag_str = self.dictionary[self.thisWord][1]
        if len(tag_str) > 0:
            splitted_tags = self.getSpliettedTags(self.thisWord)
            self.newInfoWordWindow.wordDescriptionTable.setRowCount(len(splitted_tags))
            rowCounter = 0
            for spl_tag in splitted_tags:
                self.newInfoWordWindow.wordDescriptionTable.setItem(rowCounter, 0, QTableWidgetItem(spl_tag))
                self.newInfoWordWindow.wordDescriptionTable.setItem(rowCounter, 1, QTableWidgetItem(self.tags[spl_tag]))
                rowCounter += 1
        else:
            self.newInfoWordWindow.wordDescriptionTable.setRowCount(0)

        self.newInfoWordWindow.editInitialFormBtn.clicked.connect(self.setNewInitForm)
        self.newInfoWordWindow.deleteSelectedTag.clicked.connect(self.deleteSelectedTag)

        self.newInfoWordWindow.exec_()
        if self.newInfoWordWindow.Accepted:
            self.updateWordsTable()
            self.newInfoWordWindow.close()

    groupInfoWindow = None


    def grouInfoWindow(self, col):
        row = self.tableWords.currentRow()
        item = self.tableWords.item(row, col)
        text = item.text()
        self.groupInfoWindow = DialogFormLogic()
        self.groupInfoWindow.setWindowTitle("Group")
        self.groupInfoWindow.deleteWordFromGroup.clicked.connect(self.deleteWordFromGroup)
        rowCounter = 0
        for key in self.dictionary:
            if self.dictionary[key][2] == key:
                continue
            if self.dictionary[key][2] == text:
                self.groupInfoWindow.setWindowTitle("Group: " + text.upper())
                self.groupInfoWindow.wordsTableByInitForm.insertRow(rowCounter)
                self.groupInfoWindow.wordsTableByInitForm.setItem(rowCounter, 0, QTableWidgetItem(key))  # word
                self.groupInfoWindow.wordsTableByInitForm.setItem(rowCounter, 1, QTableWidgetItem(
                    str(self.dictionary[key][2])))  # initial form
                self.groupInfoWindow.wordsTableByInitForm.setItem(rowCounter, 2,
                                                                  QTableWidgetItem(str(self.dictionary[key][0])))
                self.groupInfoWindow.wordsTableByInitForm.setItem(rowCounter, 3,
                                                                  QTableWidgetItem(str(self.dictionary[key][1])))
                rowCounter += 1

        self.groupInfoWindow.exec_()
        if self.groupInfoWindow.Accepted:
            self.groupInfoWindow.close()

    @pyqtSlot()
    def deleteWordFromGroup(self):
        col = self.groupInfoWindow.wordsTableByInitForm.currentColumn()
        if col == 0:
            row = self.groupInfoWindow.wordsTableByInitForm.currentRow()
            item = self.groupInfoWindow.wordsTableByInitForm.item(row, col)
            word = item.text()
            self.dictionary[word] = [self.dictionary[word][0], self.dictionary[word][1], word]

            col_ = self.tableWords.currentColumn()
            row_ = self.tableWords.currentRow()
            item_ = self.tableWords.item(row_, col_)
            text_ = item_.text()
            rowCounter = 0
            self.groupInfoWindow.wordsTableByInitForm.setRowCount(0)
            for key in self.dictionary:
                if self.dictionary[key][2] == text_:
                    self.groupInfoWindow.wordsTableByInitForm.insertRow(rowCounter)
                    self.groupInfoWindow.wordsTableByInitForm.setItem(rowCounter, 0, QTableWidgetItem(key))  # word
                    self.groupInfoWindow.wordsTableByInitForm.setItem(rowCounter, 1, QTableWidgetItem(
                        str(self.dictionary[key][2])))  # initial form
                    self.groupInfoWindow.wordsTableByInitForm.setItem(rowCounter, 2,
                                                                      QTableWidgetItem(str(self.dictionary[key][0])))
                    self.groupInfoWindow.wordsTableByInitForm.setItem(rowCounter, 3,
                                                                      QTableWidgetItem(str(self.dictionary[key][1])))
                    rowCounter += 1

            self.updateWordsTable()
    # create new window for editing words
    def doubleClickChecked(self):
        col = self.tableWords.currentColumn()
        if col == 0:
            self.infoWordWindow(col)

        elif col == 1:
            self.grouInfoWindow(col)

    addNewWordInDictionaryDialog = None
    @pyqtSlot()
    def addNewWordInDictionary(self):
        self.addNewWordInDictionaryDialog = AddWordLogic()
        self.addNewWordInDictionaryDialog.newTAG.hide()
        self.addNewWordInDictionaryDialog.tagInAddingFialog.addItems(self.tags_list)
        self.addNewWordInDictionaryDialog.tagInAddingFialog.adjustSize()
        self.addNewWordInDictionaryDialog.tagInAddingFialog.activated[str].connect(self.onActivateAdding)

        self.addNewWordInDictionaryDialog.addWordPushButton.clicked.connect(self.addd)
        self.addNewWordInDictionaryDialog.cancelPushButton.clicked.connect(self.cancelThisAction)

        self.addNewWordInDictionaryDialog.exec_()
    @pyqtSlot()
    def addd(self):
            if self.addNewWordInDictionaryDialog.newAddLine.text() == "":
                print("what???")
                print(self.addNewWordInDictionaryDialog.newTAG.text())
                self.addNewWordInDictionaryDialog.close()
            else:
                word = self.addNewWordInDictionaryDialog.newAddLine.text()
                if word in self.dictionary:
                    freq = self.dictionary[word][0]
                    tags = self.dictionary[word][1]
                    initForm = self.dictionary[word][2]
                    tagArray = tags.split(" ")
                    print(tagArray)
                    newTagString1 = tags
                    newtag = self.addNewWordInDictionaryDialog.newTAG.text()
                    if newtag not in tagArray:
                        newTagString1 += " "
                        newTagString1 += newtag
                        self.dictionary[word]=[freq,newTagString1, initForm]

                else:
                    self.dictionary[self.addNewWordInDictionaryDialog.newAddLine.text()] = [1, self.addNewWordInDictionaryDialog.newTAG.text(), self.addNewWordInDictionaryDialog.newAddLine.text()]

                self.updateWordsTable()

    @pyqtSlot()
    def cancelThisAction(self):
            self.addNewWordInDictionaryDialog.close()

    def onActivateAdding(self, text):
        self.addNewWordInDictionaryDialog.newTAG.setText(text)

    @pyqtSlot()
    def deleteSelectedTag(self):
        tag_row = self.newInfoWordWindow.wordDescriptionTable.currentRow()
        tag_col = self.newInfoWordWindow.wordDescriptionTable.currentColumn()
        tag_item = self.newInfoWordWindow.wordDescriptionTable.item(tag_row, tag_col)
        tag_text = tag_item.text()

        current_frequency = self.dictionary[self.thisWord][0]
        current_tags = self.dictionary[self.thisWord][1]
        current_initial_form = self.dictionary[self.thisWord][2]
        tag_list = current_tags.split(" ")
        tag_list.remove(tag_text)
        new_Tag_string = " ".join(tag_list)
        self.dictionary[self.thisWord] = [current_frequency, new_Tag_string, current_initial_form]
        current_print_tag_str = self.dictionary[self.thisWord][1]
        if len(current_print_tag_str) > 0:
            current_print_tag_list = current_print_tag_str.split(" ")
            self.newInfoWordWindow.wordDescriptionTable.setRowCount(len(current_print_tag_list))
            print(len(current_print_tag_list))
            rowCounter = 0
            for tag in current_print_tag_list:
                self.newInfoWordWindow.wordDescriptionTable.setItem(rowCounter, 0, QTableWidgetItem(tag))
                self.newInfoWordWindow.wordDescriptionTable.setItem(rowCounter, 1, QTableWidgetItem(self.tags[tag]))
                rowCounter += 1
        else:
            self.newInfoWordWindow.wordDescriptionTable.setRowCount(0)

    def onActivatedTag(self, text):
        current_frequency = self.dictionary[self.thisWord][0]
        current_tags = self.dictionary[self.thisWord][1]
        current_initialForm = self.dictionary[self.thisWord][2]

        if len(current_tags) > 0:
            currenttags = current_tags.split(" ")
            if text not in currenttags:
                current_tags += " "
                current_tags += text
                currenttags.append(text)

            self.dictionary[self.thisWord] = [current_frequency, current_tags, current_initialForm]
            self.newInfoWordWindow.wordDescriptionTable.setRowCount(len(currenttags))
            rowCounter = 0
            for spl_tag in currenttags:
                self.newInfoWordWindow.wordDescriptionTable.setItem(rowCounter, 0, QTableWidgetItem(spl_tag))
                self.newInfoWordWindow.wordDescriptionTable.setItem(rowCounter, 1, QTableWidgetItem(self.tags[spl_tag]))
                rowCounter += 1
        else:
            self.dictionary[self.thisWord] = [current_frequency, text, current_initialForm]
            self.newInfoWordWindow.wordDescriptionTable.setRowCount(1)
            self.newInfoWordWindow.wordDescriptionTable.setItem(0, 0, QTableWidgetItem(text))
            self.newInfoWordWindow.wordDescriptionTable.setItem(0, 1, QTableWidgetItem(self.tags[text]))

    # по слову, а не по тэгу
    def getSpliettedTags(self, word):
        tagString = self.dictionary[word][1]
        splitted = tagString.split(" ")
        return splitted

    # WORD: [ freq, tag, initial_form ]
    @pyqtSlot()
    def setNewInitForm(self):
        newInitForm = self.newInfoWordWindow.lineEdit.text()
        current_frequency = self.dictionary[self.thisWord][0]
        current_tags = self.dictionary[self.thisWord][1]
        self.dictionary[self.thisWord] = [current_frequency, current_tags, newInitForm]
        self.initDialogForm(self.thisWord, self.newInfoWordWindow)

    def initDialogForm(self, word, widget):
        widget.wordAndInitialFormTable.setRowCount(1)
        widget.wordAndInitialFormTable.setItem(0, 0, QTableWidgetItem(str(word)))
        widget.wordAndInitialFormTable.setItem(0, 1, QTableWidgetItem(str(self.dictionary[word][2])))
        widget.wordAndInitialFormTable.setItem(0, 2, QTableWidgetItem(str(self.dictionary[word][0])))

    @pyqtSlot()
    def deleteWordFromDictionary(self):
        msg = QMessageBox.question(self, "Pay attention!", "Are you sure? All words which have"
                                                           " this canonical form will be deleted.",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if msg == QMessageBox.Yes:
            del self.dictionary[self.thisWord]
            for key in self.dictionary.keys():
                if self.dictionary[key][2] == self.thisWord:
                    del self.dictionary[key]
            self.updateWordsTable()
            self.newInfoWordWindow.close()

    # очистка словаря
    def cleanDictionary(self):
        self.dictionary.clear()
        self.updateWordsTable()

    # Display Tags information
    def displayTagsInfo(self):
        tagdict = nltk.load('help/tagsets/upenn_tagset.pickle')
        filteredTagDict = {}
        for key in tagdict:
            filteredTagDict[key] = tagdict[key][0]  # only tags without current WORDS!

        self.tableOfTags.setRowCount(len(filteredTagDict.keys()))
        rowNumber = 0
        for tag in filteredTagDict:
            self.tableOfTags.setItem(rowNumber, 0, QTableWidgetItem(tag))
            self.tableOfTags.setItem(rowNumber, 1, QTableWidgetItem(filteredTagDict[tag]))
            rowNumber += 1

        return filteredTagDict

    # sort tags
    def sortTags(self):
        self.tableOfTags.setRowCount(len(self.tags.keys()))
        sortedTags = None
        if not self.tagReversed:
            sortedTags = sorted(self.tags.items(), key=operator.itemgetter(0))
            self.tagReversed = True
        else:
            sortedTags = sorted(self.tags.items(), key=operator.itemgetter(0), reverse=True)
            self.tagReversed = False

        rowNumber = 0
        for tag, info in sortedTags:
            self.tableOfTags.setItem(rowNumber, 0, QTableWidgetItem(tag))
            self.tableOfTags.setItem(rowNumber, 1, QTableWidgetItem(info))
            rowNumber += 1

    # Which dictionary is choosen in COMBO BOX
    def onActivated(self, text):
        self.updateStatistics()
        self.currentFilename = text
        self.dictionary = deserialization(Constants.DICTIONARY_PATH + self.currentFilename)
        self.uniqueWords = len(self.dictionary)
        for word in self.dictionary:
            self.allWords += self.dictionary[word][0]
        self.updateWordsTable()

    # fill combo box
    def fillComboBox(self):
        listOfDirectories = os.listdir("/home/pixl/Документы/Projects/PycharmProjects/Lingvistika/dictionaries/")
        self.existingDictionaries.addItems(listOfDirectories)
        self.existingDictionaries.adjustSize()
        self.existingDictionaries.setCurrentText("")
        self.existingDictionaries.activated[str].connect(self.onActivated)

    editTextWin = None

    # current_dict = create_small_dictionary(new_text_file)
    # self.dictionary = addTextInDictionary(self.dictionary, current_dict)
    # self.updateWordsTable()


    currentTextDictionary = {}
    textTagsStatistics = {}
    textTagToTagStat = {} # or list
    # wordTagStatisticsDict = {}
    # wordTagStat = []
    tagging = []
    comboboxes = []
    words = []


    def tagToTag(self):
        tags = []
        n = len(self.tagging)
        str = ""
        for i in range(0, n - 1):
            str = self.tagging[i]
            str +=  "/"
            str += self.tagging[i + 1]
            tags.append(str)

        self.textTagToTagStat = {i:tags.count(i) for i in tags}


    def saveChanges(self):
        self.editTextWin.loadTagAndTag.setEnabled(True)
        self.editTextWin.wordTagButton.setEnabled(True)
        self.editTextWin.tagFreqButton.setEnabled(True)
        self.editTextWin.wordFrequencyButton.setEnabled(True)

        self.editTextWin.workWithText.setRowCount(0)
        self.editTextWin.workWithText.setRowCount(len(self.words))
        row_number = 0
        for i in range(0, len(self.words)):
            self.editTextWin.workWithText.setItem(row_number, 0, QTableWidgetItem(self.words[i]))
            self.editTextWin.workWithText.setItem(row_number, 1, QTableWidgetItem(self.tagging[i]))
            self.editTextWin.workWithText.setItem(row_number, 2, QTableWidgetItem(self.tags[self.tagging[i]]))
            row_number += 1

            tagStr = self.currentTextDictionary[self.words[i].lower()][1]
            tags = tagStr.split(" ")
            if self.tagging[i] not in tags:
                tagStr += " "
                tagStr += self.tagging[i]
                self.currentTextDictionary[self.words[i].lower()] = [self.currentTextDictionary[self.words[i].lower()][0], tagStr, self.currentTextDictionary[self.words[i].lower()][2]]

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Text saved")
        msg.setWindowTitle("Finished!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def tagAndTagLoad(self):
        self.tagToTag()
        self.editTextWin.tagAndTag.setRowCount(len(self.textTagToTagStat))
        row_number = 0
        for key in self.textTagToTagStat:
            self.editTextWin.tagAndTag.setItem(row_number, 0, QTableWidgetItem(key))
            self.editTextWin.tagAndTag.setItem(row_number, 1, QTableWidgetItem(str(self.textTagToTagStat[key])))
            row_number += 1

    def addInDictionary(self):
        self.dictionary = addTextInDictionary(self.currentTextDictionary, self.dictionary)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Text added")
        msg.setWindowTitle("Finished!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    def ok(self):
        text = self.textEdit.toPlainText()
        self.textEdit.setTextColor(Qt.darkGreen)
        self.textEdit.setText(text)
        self.currentTextDictionary.clear()
        self.comboboxes.clear()
        self.words.clear()
        self.tagging.clear()
        self.editTextWin.close()

    def chooseTag(self, tag):
        row = self.editTextWin.workWithText.currentRow()
        self.tagging[row] = tag

    def showWordAndTagTable(self):
        n = len(self.words)
        wordTagStatList = []
        for i in range(n):
            tag = self.tagging[i]
            word = self.words[i].lower()
            result = word + "/" + tag
            wordTagStatList.append(result)

        wordAndTagDict = {i: wordTagStatList.count(i) for i in wordTagStatList}

        self.editTextWin.wordTag.setRowCount(len(wordAndTagDict))
        row_number = 0
        for word_tag in wordAndTagDict:
            self.editTextWin.wordTag.setItem(row_number, 0, QTableWidgetItem(word_tag))
            self.editTextWin.wordTag.setItem(row_number, 1, QTableWidgetItem(str(wordAndTagDict[word_tag])))
            row_number += 1

    def showTagFrequencyTable(self):
        tag_dict = {i: self.tagging.count(i) for i in self.tagging}
        self.editTextWin.tagFrequency.setRowCount(len(tag_dict))
        row_number = 0
        for tag in tag_dict:
            self.editTextWin.tagFrequency.setItem(row_number, 0, QTableWidgetItem(tag))
            self.editTextWin.tagFrequency.setItem(row_number, 1, QTableWidgetItem(str(tag_dict[tag])))
            self.editTextWin.tagFrequency.setItem(row_number, 2, QTableWidgetItem(self.tags[tag]))
            row_number += 1

    def showWordFrequencyStatistics(self):
        self.editTextWin.wordFreqTable.setRowCount(len(self.currentTextDictionary))
        row_number = 0
        for word in self.currentTextDictionary:
            self.editTextWin.wordFreqTable.setItem(row_number, 0, QTableWidgetItem(word))
            self.editTextWin.wordFreqTable.setItem(row_number, 1, QTableWidgetItem(str(self.currentTextDictionary[word][0])))
            row_number += 1

    def tagForWord(self, tag):
        row = self.editTextWin.workWithText.currentRow()
        self.tagging[row] = tag
        self.editTextWin.workWithText.setItem(row, 1, QTableWidgetItem(tag))

    def setNewTag(self):
        self.editTextWin.comboBox.activated[str].connect(self.tagForWord)
        self.editTextWin.comboBox.setVisible(True)

    def annotateText(self):
        self.editTextWin = TextWorkLogic()
        self.editTextWin.comboBox.setVisible(False)
        self.editTextWin.saveChangesAboutText.clicked.connect(self.saveChanges)
        self.editTextWin.addInDictionary.clicked.connect(self.addInDictionary)
        self.editTextWin.loadTagAndTag.clicked.connect(self.tagAndTagLoad)
        self.editTextWin.OK.clicked.connect(self.ok)
        self.editTextWin.wordTagButton.clicked.connect(self.showWordAndTagTable)
        self.editTextWin.tagFreqButton.clicked.connect(self.showTagFrequencyTable)
        self.editTextWin.wordFrequencyButton.clicked.connect(self.showWordFrequencyStatistics)
        text = self.textEdit.toPlainText()
        self.editTextWin.comboBox.addItems(self.tags_list)
        self.editTextWin.workWithText.doubleClicked.connect(self.setNewTag)
        #
        self.currentTextDictionary = create_small_dictionary_text(text)
        self.words = word_tokenize(text)
        self.editTextWin.workWithText.setRowCount(len( self.words ))
        row_number = 0
        self.tagging = [""] * len(self.words)
        word_number = 0
        for word in  self.words :
            if word.lower() in self.dictionary:
                self.editTextWin.workWithText.setItem(row_number, 0, QTableWidgetItem(word))
                tagStr = self.dictionary[word.lower()][1]
                tagg = tagStr.split(" ")
                if len(tagg) > 1:
                    comboBox = QComboBox()
                    for t in tagg:
                        comboBox.addItem(t)
                    comboBox.activated[str].connect(self.chooseTag)
                    self.comboboxes.append(comboBox)
                    self.editTextWin.workWithText.setCellWidget(row_number, 1, comboBox)
                    self.editTextWin.workWithText.setItem(row_number, 2, QTableWidgetItem("..."))
                    self.tagging[word_number] = tagg[1]

                else:
                    self.editTextWin.workWithText.setItem(row_number, 1,
                                                          QTableWidgetItem(self.dictionary[word.lower()][1]))
                    tag = tagg[0]
                    self.editTextWin.workWithText.setItem(row_number, 2, QTableWidgetItem(self.tags[tag]))
                    self.tagging[word_number] = tag

            else:
                self.editTextWin.workWithText.setItem(row_number, 0, QTableWidgetItem(word))
                noname_tag = nltk.tag.pos_tag([word])[0][1]
                self.editTextWin.workWithText.setItem(row_number, 1, QTableWidgetItem(noname_tag))
                self.editTextWin.workWithText.setItem(row_number, 2, QTableWidgetItem(self.tags[noname_tag]))
                self.tagging[word_number] = noname_tag
            row_number += 1
            word_number+=1



        self.editTextWin.exec_()

    def clearInputText(self):
        self.textEdit.setText("")

    # menu button
    # loads new text file, makes dictionary and adding it in current dictionary
    def loadNewTextFile(self):
        new_text_file = QFileDialog.getOpenFileName(self, "Choose new text file",
                                                    '/home/pixl/Документы/Projects/PycharmProjects/Lingvistika/resources')[
            0]
        if new_text_file == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Choose any file!")
            msg.setWindowTitle("ERROR!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        textFile = open(new_text_file, 'r')
        text = textFile.read()
        punctuats = list(string.punctuation)
        sentences = sent_tokenize(text)

        for sent in sentences:
            words = word_tokenize(sent)

            for word in words:
                if word.lower() in self.dictionary:
                    tags = self.dictionary[word.lower()][1]
                    strTag = tags.split(" ")
                    if len(strTag) > 1:
                        self.textEdit.setTextColor(Qt.magenta)
                    else:
                        self.textEdit.setTextColor(Qt.darkGreen)
                    if word in punctuats:
                        self.textEdit.insertPlainText(word)
                    else:
                        self.textEdit.insertPlainText(" ")
                        self.textEdit.insertPlainText(word)

                else:
                    self.textEdit.setTextColor(Qt.red)
                    if word in punctuats:
                        self.textEdit.insertPlainText(word)
                    else:
                        self.textEdit.insertPlainText(" ")
                        self.textEdit.insertPlainText(word)

        textFile.close()


    # def saveChangesFromText(self):
        """small_dictionary = create_small_dictionary(new_text_file)
        addTextInDictionary(small_dictionary, self.dictionary)
        self.updateWordsTable()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Adding of new text in dictionary was completed")
        msg.setWindowTitle("FINISHED!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()"""

    # loads new dictionary
    def loadNewDictionary(self):
        self.updateStatistics()
        fname = \
            QFileDialog.getOpenFileName(self, 'Open dictionary',
                                        '/home/Документы/Projects/PycharmProjects/Lingvistika/')[0]
        if fname == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Choose any file!")
            msg.setWindowTitle("ERROR!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        filepath = str(fname)
        splitted = filepath.split('/')
        self.currentFilename = splitted[-1]
        self.dictionary = deserialization(fname)
        self.updateWordsTable()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Load of dictionary completed.")
        msg.setWindowTitle("Success!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # CTRL S Saving of dictionary
    def justSaveDictionary(self):
        path = Constants.DICTIONARY_PATH + self.currentFilename
        serialization(self.dictionary, path)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Saving of dictionary in file: " + path)
        msg.setWindowTitle("FINISHED!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # creates new dictionary in which we will save our current dictionary
    def saveInNewDictionaryFILENAME(self):
        newOutputFile, ok = QInputDialog.getText(self, 'Save dictionary in new file', "Enter filename:")
        if newOutputFile != "" and ok:
            path = Constants.DICTIONARY_PATH + newOutputFile
            serialization(self.dictionary, path)
            self.currentFilename = newOutputFile
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Saving of dictionary in new file: " + path)
            msg.setWindowTitle("FINISHED!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Choose any file!")
            msg.setWindowTitle("ERROR!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

    # WORD: [ freq, tag, initial_form ]
    def updateWordsTable(self):
        if len(self.dictionary.keys()) == 0:
            self.tableWords.setRowCount(0)
        else:
            self.tableWords.setRowCount(len(self.dictionary.keys()))
            row_number = 0
            for word in self.dictionary:
                self.tableWords.setItem(row_number, 0, QTableWidgetItem(word))  # word
                self.tableWords.setItem(row_number, 1, QTableWidgetItem(str(self.dictionary[word][2])))  # initial form
                self.tableWords.setItem(row_number, 2, QTableWidgetItem(str(self.dictionary[word][0])))
                self.tableWords.setItem(row_number, 3, QTableWidgetItem(str(self.dictionary[word][1])))

                row_number += 1

    # SORT
    @pyqtSlot()
    def sortByWord(self):
        sortedByWord = sorted(self.dictionary.items(), key=operator.itemgetter(0))
        counter = 0
        length = len(self.dictionary.keys())
        self.tableWords.setRowCount(length)
        for word, value in sortedByWord:
            self.tableWords.setItem(counter, 0, QTableWidgetItem(word))
            self.tableWords.setItem(counter, 1, QTableWidgetItem(str(value[2])))
            self.tableWords.setItem(counter, 2, QTableWidgetItem(str(value[0])))
            self.tableWords.setItem(counter, 3, QTableWidgetItem(str(value[1])))

            counter += 1

    @pyqtSlot()
    def sortByFrequency(self):
        sortedByFrequency = sorted(self.dictionary.items(), key=operator.itemgetter(1), reverse=True)
        counter = 0
        length = len(self.dictionary.keys())
        self.tableWords.setRowCount(length)
        for word, value in sortedByFrequency:
            self.tableWords.setItem(counter, 0, QTableWidgetItem(word))
            self.tableWords.setItem(counter, 1, QTableWidgetItem(str(value[2])))
            self.tableWords.setItem(counter, 2, QTableWidgetItem(str(value[0])))
            self.tableWords.setItem(counter, 3, QTableWidgetItem(str(value[1])))
            counter += 1

    def getInitialFormsOfWords(self):
        initialForms = {}
        for word in self.dictionary:
            initialForms[word] = self.dictionary[word][2]
        sortedDict = sorted(initialForms.items(), key=operator.itemgetter(1))
        return sortedDict

    @pyqtSlot()
    def sortByBelongingToGroup(self):
        counter = 0
        length = len(self.dictionary.keys())
        self.tableWords.setRowCount(length)
        forms = self.getInitialFormsOfWords()
        for key, value in forms:
            self.tableWords.setItem(counter, 0, QTableWidgetItem(key))
            self.tableWords.setItem(counter, 1, QTableWidgetItem(value))
            self.tableWords.setItem(counter, 2, QTableWidgetItem(str(self.dictionary[key][0])))
            self.tableWords.setItem(counter, 3, QTableWidgetItem(self.dictionary[key][1]))
            counter += 1
