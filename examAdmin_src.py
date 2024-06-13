#  Name: Nguyen Hoang Nam
#  StudentID: 20227247
#  Class: 738657 - MI3310
#  Project: Final Project - Topic 6

import sqlite3
import random
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox


def create_connection():
    return sqlite3.connect('QuestionBank.db')


class ExamAdmin:
    def __init__(self, ui):
        self.ui = ui
        self.scoreTrack = 0
        self.quesCount = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkTimeLeft)

    def startQuiz(self):
        cleanUpResultsDetail()
        self.scoreTrack = 0
        self.quesCount = 1
        numOfQues = self.ui.numofQuesInputbox.text().strip()
        amouOfTime = self.ui.amountofTimeInputbox.text().strip()

        # Check condition for user input
        if not numOfQues.isdigit() or not amouOfTime.isdigit():
            QMessageBox.warning(self.ui, "Input Error",
                                "Please enter integer values.")
            self.ui.numofQuesInputbox.setText("")
            self.ui.amountofTimeInputbox.setText("")
            return
        if int(numOfQues) < 1 or int(numOfQues) > self.ui.tableWidget.rowCount():
            QMessageBox.warning(self.ui, "Input Error",
                                "Invalid question number.")
            self.ui.numofQuesInputbox.setText("")
            self.ui.amountofTimeInputbox.setText("")
            return
        if not numOfQues or not amouOfTime:
            QMessageBox.warning(
                self.ui, 'Warning', 'Please enter the number of questions and time.')
            return

        # Get a random question and display it
        self.curQues = chooseRandomQues()
        self.insertQuesIDToDB(self.curQues[0])
        displayQues(self.curQues, self.ui.questionDisplaybox,
                    self.ui.ansAlabel, self.ui.ansBlabel, self.ui.ansClabel, self.ui.ansDlabel)

        # Enable the answer buttons
        enableAnsButton(self)

        self.ui.quesCountlabel.setText(f"{self.quesCount}/{numOfQues}")
        amouOfTime = int(self.ui.amountofTimeInputbox.text().strip())
        self.ui.progressBar.setMaximum(amouOfTime)
        self.ui.progressBar.setValue(0)
        self.timer.start(1000)

        self.ui.quesCountlabel.setText(
            f"{self.quesCount}/{self.ui.numofQuesInputbox.text().strip()}")

    def checkCorrAns(self, answer):
        # Insert user's answer into 'urAns'
        self.insertUserAnswerToDB(answer)

        # Check if the selected answer is correct
        if answer == self.curQues[6]:
            self.scoreTrack += 1
        self.quesCount += 1

        self.ui.quesCountlabel.setText(
            f"{self.quesCount}/{self.ui.numofQuesInputbox.text().strip()}")

        # Check if there are more questions
        if self.quesCount <= int(self.ui.numofQuesInputbox.text().strip()):
            # Proceed to the next question
            self.curQues = chooseRandomQues()
            # Insert 'quesID' into 'resultsDetail'
            self.insertQuesIDToDB(self.curQues[0])
            displayQues(self.curQues, self.ui.questionDisplaybox,
                        self.ui.ansAlabel, self.ui.ansBlabel, self.ui.ansClabel, self.ui.ansDlabel)
        else:
            # Display final score
            self.timer.stop()
            score_text = f"{
                self.scoreTrack}/{self.ui.numofQuesInputbox.text().strip()}"
            self.ui.scoretlabel.setText(score_text)
            self.saveResultToDB()
            self.saveDetailResultToDB()
            self.displayResult()
            self.resetToInitialState()
            self.displayResultsInList()
            self.displayAllResults()
            QMessageBox.information(
                self.ui, "Quiz Finished", "You have answered all questions.")

    def insertQuesIDToDB(self, quesID):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO resultsDetail (quesID) VALUES (?)", (quesID,))
        conn.commit()
        conn.close()

    def insertUserAnswerToDB(self, answer):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE resultsDetail SET urAns = ? WHERE quesID = ?", (answer, self.curQues[0]))
        conn.commit()
        conn.close()

    def saveDetailResultToDB(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT resID FROM userResult ORDER BY resID DESC LIMIT 1")
        resID = cursor.fetchone()[0]
        cursor.execute(
            "UPDATE resultsDetail SET resID = ? WHERE resID IS NULL", (resID,))
        conn.commit()
        conn.close()

    def checkTimeLeft(self):
        curValue = self.ui.progressBar.value()
        if curValue < self.ui.progressBar.maximum():
            self.ui.progressBar.setValue(curValue + 1)
        else:
            self.timer.stop()
            score_text = f"{
                self.scoreTrack}/{self.ui.numofQuesInputbox.text().strip()}"
            self.ui.scoretlabel.setText(score_text)
            self.saveResultToDB()
            self.saveDetailResultToDB()
            self.displayResult()
            self.resetToInitialState()
            self.displayResultsInList()
            self.displayAllResults()
            QMessageBox.information(self.ui, "Time's up!", "Time has ended.")

    def saveResultToDB(self):
        conn = create_connection()
        cursor = conn.cursor()

        score_text = f"{
            self.scoreTrack}/{self.ui.numofQuesInputbox.text().strip()}"
        cursor.execute(
            "INSERT INTO userResult (result) VALUES (?)", (score_text,))

        conn.commit()
        conn.close()

    def displayResult(self):
        conn = create_connection()
        cursor = conn.cursor()

        # Retrieve the last 5 scores from the 'userResult' table
        cursor.execute(
            "SELECT result FROM userResult ORDER BY resID DESC LIMIT 5")
        results = cursor.fetchall()

        # Display the results in the QLabel widgets
        labels = [self.ui.result1displaylabel, self.ui.result2displaylabel,
                  self.ui.result3displaylabel, self.ui.result4displaylabel, self.ui.result5displaylabel]
        for i, result in enumerate(results):
            labels[i].setText(result[0])

        conn.close()

    def resetToInitialState(self):
        self.timer.stop()
        self.quesCount = 1
        self.scoreTrack = 0
        self.ui.ansApushButton.setDisabled(True)
        self.ui.ansBpushButton.setDisabled(True)
        self.ui.ansCpushButton.setDisabled(True)
        self.ui.ansDpushButton.setDisabled(True)
        self.ui.numofQuesInputbox.setDisabled(False)
        self.ui.amountofTimeInputbox.setDisabled(False)
        self.ui.quesCountlabel.setText("/")
        self.ui.ansAlabel.setText("Answer A")
        self.ui.ansBlabel.setText("Answer B")
        self.ui.ansClabel.setText("Answer C")
        self.ui.ansDlabel.setText("Answer D")
        self.ui.numofQuesInputbox.setText("")
        self.ui.amountofTimeInputbox.setText("")
        self.ui.questionDisplaybox.setText(
            "| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |"
        )
        self.ui.progressBar.setValue(0)

    def resetResultBoard(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setText("Are you sure you want to reset the board?")
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.StandardButton.Yes:
            conn = create_connection()
            cursor = conn.cursor()
            # Clear 'resultsDetail' table
            cursor.execute('DELETE FROM resultsDetail')
            # Clear 'userResult' table
            cursor.execute('DELETE FROM userResult')
            conn.commit()
            conn.close()
            self.ui.result1displaylabel.setText("/")
            self.ui.result2displaylabel.setText("/")
            self.ui.result3displaylabel.setText("/")
            self.ui.result4displaylabel.setText("/")
            self.ui.result5displaylabel.setText("/")
            self.ui.listExamWidget.clear()
        self.displayAllResults()
        self.displayResult()

    def displayResultsInList(self):
        # Connect to the database
        conn = create_connection()
        cursor = conn.cursor()

        # Execute the query
        cursor.execute("SELECT resID, result FROM userResult")

        # Fetch all rows from the last executed statement
        results = cursor.fetchall()

        # Clear the QListWidget
        self.ui.listExamWidget.clear()

        # Add items to the QListWidget
        for result in results:
            item_text = f"{result[0]} - {result[1]}"
            self.ui.listExamWidget.addItem(item_text)

        # Close the connection
        conn.close()

    def displaySelectedResultFromList(self):
        # Get the selected item from the QListWidget
        selected_item = self.ui.listExamWidget.currentItem()

        if selected_item is not None:
            # Connect to the database
            conn = create_connection()
            cursor = conn.cursor()

            # Get the resID from the selected item's text
            resID = selected_item.text().split(' - ')[0]

            # Execute the query
            cursor.execute("""
                SELECT q.quesID, rd.resID, q.CorrectAnswer, rd.urAns, q.Question, q.AnswerA, q.AnswerB, q.AnswerC, q.AnswerD
                FROM resultsDetail rd
                INNER JOIN questions q ON rd.quesID = q.quesID
                WHERE rd.resID = ?
            """, (resID,))

            # Fetch all rows from the last executed statement
            results = cursor.fetchall()

            # Clear the QTableWidget
            self.ui.resultTableWidget.setRowCount(0)

            # Add items to the QTableWidget
            for row_number, row_data in enumerate(results):
                self.ui.resultTableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.resultTableWidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

            # Close the connection
            conn.close()

    def displayAllResults(self):
        # Connect to the database
        conn = create_connection()
        cursor = conn.cursor()

        # Execute a query to select all data
        cursor.execute("""
            SELECT q.quesID, rd.resID, q.CorrectAnswer, rd.urAns, q.Question, q.AnswerA, q.AnswerB, q.AnswerC, q.AnswerD
            FROM resultsDetail rd
            INNER JOIN questions q ON rd.quesID = q.quesID
        """)

        # Fetch all rows from the last executed statement
        results = cursor.fetchall()

        # Clear the QTableWidget
        self.ui.resultTableWidget.setRowCount(0)

        # Add items to the QTableWidget
        for row_number, row_data in enumerate(results):
            self.ui.resultTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.resultTableWidget.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))

        # Close the connection
        conn.close()


def cleanUpResultsDetail():
    conn = create_connection()
    cursor = conn.cursor()
    # Delete rows where 'resID' is null
    cursor.execute("DELETE FROM resultsDetail WHERE resID IS NULL")
    conn.commit()
    conn.close()


def chooseRandomQues():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()
    # Randomly select a question
    selectedQues = random.choice(rows)
    conn.close()
    return selectedQues


def displayQues(question, question_label, ansA_label, ansB_label, ansC_label, ansD_label):
    # Display the question and its answers
    question_label.setText(question[1])
    ansA_label.setText(question[2])
    ansB_label.setText(question[3])
    ansC_label.setText(question[4])
    ansD_label.setText(question[5])


def startTimer(amouOfTime, progress_bar):
    timer = QTimer()
    timer.timeout.connect(lambda: updateProgressBar(progress_bar))
    timer.start(1000)
    # Initialize progress bar
    progress_bar.setMaximum(amouOfTime)
    progress_bar.setValue(amouOfTime)


def updateProgressBar(progress_bar):
    curValue = progress_bar.value()

    if curValue > 0:
        progress_bar.setValue(curValue - 1)
    else:
        progress_bar.setValue(0)


def enableAnsButton(self):
    self.ui.ansApushButton.setDisabled(False)
    self.ui.ansBpushButton.setDisabled(False)
    self.ui.ansCpushButton.setDisabled(False)
    self.ui.ansDpushButton.setDisabled(False)
