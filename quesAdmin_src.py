#  Name: Nguyen Hoang Nam
#  StudentID: 20227247
#  Class: 738657 - MI3310
#  Project: Final Project - Topic 6

import pyodbc
import pickle
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt6.QtWidgets import QMessageBox
from examAdmin_src import create_connection


class QuestionAdmin:
    def __init__(self, ui):
        self.ui = ui

    def insertQues(self):
        # Create a QMessageBox for confirmation
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setText("Are you sure you want to add this question?")
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    
        # Show the message box and get the user's response
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.StandardButton.Yes:
            # Get the text from the QLineEdit widgets
            quesID = self.ui.IDEditWidget.text()
            question = self.ui.quesBoxEditWidget.text()
            ansA = self.ui.ansAEditWidget.text()
            ansB = self.ui.ansBEditWidget.text()
            ansC = self.ui.ansCEditWidget.text()
            ansD = self.ui.ansDEditWidget.text()
    
            # Get the current text from the QComboBox
            corrAns = self.ui.corrAnscomboBox.currentText()
    
            # Check if all QLineEdit widgets have been filled out
            if not all([quesID, question, ansA, ansB, ansC, ansD, corrAns]):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setText("Please fill out all fields before submitting.")
                msgBox.setWindowTitle("Warning")
                msgBox.exec()
                return
    
            conn = create_connection()
            cursor = conn.cursor()
    
            # Check if quesID already exists in the database
            cursor.execute('SELECT quesID FROM questions WHERE quesID = ?', (quesID,))
            if cursor.fetchone():
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setText("Question ID already exists.")
                msgBox.setWindowTitle("Warning")
                msgBox.exec()
                return
    
            # Insert the new question into the database
            cursor.execute('''
                INSERT INTO questions (quesID, Question, AnswerA, AnswerB, AnswerC, AnswerD, CorrectAnswer)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (quesID, question, ansA, ansB, ansC, ansD, corrAns))
    
            conn.commit()
            conn.close()
    
            # Success message box
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("Question added successfully.")
            msgBox.setWindowTitle("Success")
            msgBox.exec()
    
            # Reload the QTableWidget
            loadData(self.ui.tableWidget)
            self.ui.quesBoxEditWidget.setText("")
            self.ui.ansAEditWidget.setText("")
            self.ui.ansBEditWidget.setText("")
            self.ui.ansCEditWidget.setText("")
            self.ui.ansDEditWidget.setText("")
            self.ui.IDEditWidget.setText("")
            self.ui.corrAnscomboBox.setCurrentIndex(0)
            self.ui.addQuesWidget_2.hide()
            dbToBinFile()


    def delQues(self):
        # Create a QMessageBox
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setText("Are you sure you want to delete this question?")
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msgBox.setDefaultButton(QMessageBox.StandardButton.No)
        # Show the message box and get the user's response
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.StandardButton.Yes:
            row = self.ui.tableWidget.currentRow()
            quesID = self.ui.tableWidget.item(row, 0).text()

            conn = create_connection()
            cursor = conn.cursor()

            # Delete the question from the 'resultsDetail' table
            cursor.execute(
                'DELETE FROM resultsDetail WHERE quesID = ?', (quesID,))

            # Delete the question from the 'questions' table
            cursor.execute('DELETE FROM questions WHERE quesID = ?', (quesID,))

            conn.commit()
            conn.close()

            # Reload the QTableWidget
            ReloadQTableWidget(self.ui)
        loadData(self.ui.tableWidget)
        dbToBinFile()

    def updateQues(self):
        # Create a QMessageBox
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setText("Are you sure you want to update this question?")
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msgBox.setDefaultButton(QMessageBox.StandardButton.No)
        # Show the message box and get the user's response
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.StandardButton.Yes:
            conn = create_connection()
            cursor = conn.cursor()

            # Get the updated values from QLineEdit widgets
            quesID = self.ui.IDtxtbox.text()
            question = self.ui.questiontxtbox.text()
            ansA = self.ui.ansAtxtbox.text()
            ansB = self.ui.ansBtxtbox.text()
            ansC = self.ui.ansCtxtbox.text()
            ansD = self.ui.ansDtxtbox.text()
            corrAns = self.ui.corrAnstxtbox.text()

            # Check if all fields are filled out
            if not all([quesID, question, ansA, ansB, ansC, ansD, corrAns]):
                QMessageBox.warning(
                    self.ui, 'Warning', 'Please fill out all fields before submitting.')
                return

            # Check if the correct answer is one of 'A', 'B', 'C', or 'D'
            if corrAns not in {'A', 'B', 'C', 'D'}:
                QMessageBox.warning(
                    self.ui, 'Warning', 'The correct answer must be one of A, B, C, or D.')
                return

            # Update the question in the database
            cursor.execute('''
                UPDATE questions
                SET Question = ?, AnswerA = ?, AnswerB = ?, AnswerC = ?, AnswerD = ?, CorrectAnswer = ?
                WHERE quesID = ?
            ''', (question, ansA, ansB, ansC, ansD, corrAns, quesID))

            conn.commit()
            conn.close()
            dbToBinFile()
            loadData(self.ui.tableWidget)


def displayInFormulaBar(ui, row):
    ui.delQuesbutton.setDisabled(False)
    ui.IDtxtbox.setText(ui.tableWidget.item(row, 0).text())
    ui.questiontxtbox.setText(ui.tableWidget.item(row, 1).text())
    ui.ansAtxtbox.setText(ui.tableWidget.item(row, 2).text())
    ui.ansBtxtbox.setText(ui.tableWidget.item(row, 3).text())
    ui.ansCtxtbox.setText(ui.tableWidget.item(row, 4).text())
    ui.ansDtxtbox.setText(ui.tableWidget.item(row, 5).text())
    ui.corrAnstxtbox.setText(ui.tableWidget.item(row, 6).text())
    ui.delQuesbutton.setDisabled(False)


def resetFormulaBar(ui):
    ui.IDtxtbox.setText("")
    ui.questiontxtbox.setText("")
    ui.ansAtxtbox.setText("")
    ui.ansBtxtbox.setText("")
    ui.ansCtxtbox.setText("")
    ui.ansDtxtbox.setText("")
    ui.corrAnstxtbox.setText("")


def loadData(table_widget):
    conn = create_connection()
    cursor = conn.cursor()
    # Execute the query
    cursor.execute("SELECT * FROM questions ORDER BY quesID")
    # Get all rows
    rows = cursor.fetchall()
    # Set the number of rows in the table
    table_widget.setRowCount(len(rows))
    # Loop through each row
    for i, row in enumerate(rows):
        # Loop through each column
        for j, value in enumerate(row):
            # Add the item to the table
            table_widget.setItem(i, j, QTableWidgetItem(str(value)))
    conn.close()


def dbToBinFile():
    conn = create_connection()
    cursor = conn.cursor()
    # Execute the query
    cursor.execute("SELECT * FROM questions")
    # Get all rows
    rows = cursor.fetchall()
    # Convert the data to a binary file
    with open('questions.bin', 'wb') as binFile:
        pickle.dump(rows, binFile)
    conn.close()


def BinFileTodb():
    conn = create_connection()
    cursor = conn.cursor()
    # Load the data from the binary file
    with open('questions.bin', 'rb') as binFile:
        rows = pickle.load(binFile)
    # Insert the data back into the database
    for row in rows:
        quesID = row[0]
        cursor.execute(
            'SELECT quesID FROM questions WHERE quesID = ?', (quesID,))
        if not cursor.fetchone():
            cursor.execute('''
            INSERT INTO questions (quesID, Question, AnswerA, AnswerB, AnswerC, AnswerD, CorrectAnswer)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', row)
    conn.commit()
    conn.close()


def ReloadQTableWidget(ui):
    ui.IDtxtbox.setText("")
    ui.questiontxtbox.setText("")
    ui.ansAtxtbox.setText("")
    ui.ansBtxtbox.setText("")
    ui.ansCtxtbox.setText("")
    ui.ansDtxtbox.setText("")
    ui.corrAnstxtbox.setText("")
