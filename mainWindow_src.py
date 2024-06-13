#  Name: Nguyen Hoang Nam
#  StudentID: 20227247
#  Class: 738657 - MI3310
#  Project: Final Project - Topic 6

#  This is TRYusingSQLite branch hi it me
import sys
import pickle
import random
import sqlite3
from questionBank_src import createDatabase
from examAdmin_src import ExamAdmin
from quesAdmin_src import QuestionAdmin, BinFileTodb, dbToBinFIle, loadData, displayInFormulaBar, resetFormulaBar

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QMessageBox,
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6 import uic, QtWidgets


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # Load .ui file
        self.ui = uic.loadUi("form.ui", self)

        # setup mainWindow
        self.ui.setWindowTitle("TOPIC6_20227247_NguyenHoangNam")
        self.ui.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tableWidget.setColumnWidth(0, 40)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.resultTableWidget.setColumnWidth(0, 40)
        self.ui.resultTableWidget.setColumnWidth(1, 48)
        self.ui.resultTableWidget.setColumnWidth(4, 120)
        self.ui.ansApushButton.setDisabled(True)
        self.ui.ansBpushButton.setDisabled(True)
        self.ui.ansCpushButton.setDisabled(True)
        self.ui.ansDpushButton.setDisabled(True)
        self.ui.delQuesbutton.setDisabled(True)
        self.ui.IDtxtbox.setDisabled(True)
        self.ui.addQuesWidget_2.hide()
    # Initial state setup
        # create Database and Table
        self.examAdmin = ExamAdmin(self.ui)
        self.questionAdmin = QuestionAdmin(self.ui)
        createDatabase()
        BinFileTodb()
        # load data from DB to QTableWidget
        loadData(self.ui.tableWidget)
        self.examAdmin.displayResultsInList()
        self.examAdmin.displayResult()
        self.examAdmin.displayAllResults()

    # Button setup
        # setup for "PLAY" tab
        self.ui.ansApushButton.clicked.connect(
            lambda: self.examAdmin.checkCorrAns('A'))
        self.ui.ansBpushButton.clicked.connect(
            lambda: self.examAdmin.checkCorrAns('B'))
        self.ui.ansCpushButton.clicked.connect(
            lambda: self.examAdmin.checkCorrAns('C'))
        self.ui.ansDpushButton.clicked.connect(
            lambda: self.examAdmin.checkCorrAns('D'))
        self.ui.reStartButton.clicked.connect(
            self.examAdmin.resetToInitialState)
        self.ui.listExamWidget.itemClicked.connect(
            self.examAdmin.displaySelectedResultFromList)
        self.ui.resetBoard.clicked.connect(self.examAdmin.resetResultBoard)
        self.ui.startButton.clicked.connect(self.examAdmin.startQuiz)
        self.ui.listExamWidget.itemDoubleClicked.connect(self.deselectItem)
        self.ui.tableWidget.cellDoubleClicked.connect(self.deselectCell)
        # setup for "EDIT" tab
        self.ui.confirmEditButton.clicked.connect(
            self.questionAdmin.updateQues)
        self.ui.delQuesbutton.clicked.connect(self.questionAdmin.delQues)
        self.ui.tableWidget.cellClicked.connect(
            lambda row, column: displayInFormulaBar(self.ui, row))
        self.ui.addQuesbutton.clicked.connect(self.switchToAddquesWidget)
        self.ui.submitButton.clicked.connect(self.questionAdmin.insertQues)
        self.ui.cancelButton.clicked.connect(self.closeAddQuesWidget)
        self.show()

    def switchToAddquesWidget(self):
        self.ui.addQuesWidget_2.show()

    def closeAddQuesWidget(self):
        self.ui.quesBoxEditWidget.setText("")
        self.ui.ansAEditWidget.setText("")
        self.ui.ansBEditWidget.setText("")
        self.ui.ansCEditWidget.setText("")
        self.ui.ansDEditWidget.setText("")
        self.ui.addQuesWidget_2.hide()

    def deselectItem(self):
        self.ui.listExamWidget.clearSelection()
        self.ui.resultTableWidget.setRowCount(0)  # Clear the QTableWidget
        self.examAdmin.displayAllResults()

    def deselectCell(self):
        self.ui.tableWidget.clearSelection()  # Deselect all cells in the QTableWidget
        self.ui.delQuesbutton.setDisabled(True)
        resetFormulaBar(self.ui)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
