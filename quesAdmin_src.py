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

    def insert_question(ui):
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
            quesID = ui.IDEditWidget.text()
            question = ui.quesBoxEditWidget.text()
            ansA = ui.ansAEditWidget.text()
            ansB = ui.ansBEditWidget.text()
            ansC = ui.ansCEditWidget.text()
            ansD = ui.ansDEditWidget.text()

            # Get the current text from the QComboBox
            corrAns = ui.corrAnscomboBox.currentText()

            # Check if all QLineEdit widgets have been filled out
            if not all([quesID, question, ansA, ansB, ansC, ansD, corrAns]):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setText("Please fill out all fields before submitting.")
                msgBox.setWindowTitle("Warning")
                msgBox.exec()
                return

            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=HOANGNAM\\SQLEXPRESS;'
                                  'Database=QuestionBank;'
                                  'Trusted_Connection=yes;')
            cursor = conn.cursor()

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
            ui.loadData(ui.tableWidget)
            ui.quesBoxEditWidget.setText("")
            ui.ansAEditWidget.setText("")
            ui.ansBEditWidget.setText("")
            ui.ansCEditWidget.setText("")
            ui.ansDEditWidget.setText("")
            ui.corrAnscomboBox.setCurrentIndex(0)
            ui.addQuesWidget_2.hide()
            ui.dbToBinFIle()

    def delete_question(ui):
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
            row = ui.tableWidget.currentRow()
            quesID = ui.tableWidget.item(row, 0).text()

            conn = create_connection()
            cursor = conn.cursor()

            # Delete the question from the database
            cursor.execute('DELETE FROM questions WHERE quesID = ?', quesID)

            conn.commit()
            conn.close()

            # Reload the QTableWidget
            ui.ReloadQTableWidget(ui)
        ui.loadData(ui.tableWidget)
        ui.dbToBinFIle()

    def updateQues(ui):
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
            quesID = ui.IDtxtbox.text()
        question = ui.questiontxtbox.text()
        ansA = ui.ansAtxtbox.text()
        ansB = ui.ansBtxtbox.text()
        ansC = ui.ansCtxtbox.text()
        ansD = ui.ansDtxtbox.text()
        corrAns = ui.corrAnstxtbox.text()

        # Update the question in the database
        cursor.execute('''
            UPDATE questions
            SET Question = ?, AnswerA = ?, AnswerB = ?, AnswerC = ?, AnswerD = ?, CorrectAnswer = ?
            WHERE quesID = ?
        ''', (question, ansA, ansB, ansC, ansD, corrAns, quesID))

        conn.commit()
        conn.close()
        ui.dbToBinFIle()
        ui.loadData(ui.tableWidget)

    def displayInFormulaBar(ui, row):
        ui.IDtxtbox.setText(ui.tableWidget.item(row, 0).text())
        ui.questiontxtbox.setText(ui.tableWidget.item(row, 1).text())
        ui.ansAtxtbox.setText(ui.tableWidget.item(row, 2).text())
        ui.ansBtxtbox.setText(ui.tableWidget.item(row, 3).text())
        ui.ansCtxtbox.setText(ui.tableWidget.item(row, 4).text())
        ui.ansDtxtbox.setText(ui.tableWidget.item(row, 5).text())
        ui.corrAnstxtbox.setText(ui.tableWidget.item(row, 6).text())
        ui.delQuesbutton.setDisabled(False)
        ui.addQuesbutton.setDisabled(False)

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


def dbToBinFIle():
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
        cursor.execute('SELECT quesID FROM questions WHERE quesID = ?', quesID)
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
