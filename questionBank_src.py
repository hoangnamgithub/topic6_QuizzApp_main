#  Name: Nguyen Hoang Nam
#  StudentID: 20227247
#  Class: 738657 - MI3310
#  Project: Final Project - Topic 6

import sqlite3


def createDatabase():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('QuestionBank.db')

    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            quesID TEXT PRIMARY KEY,
            Question TEXT,
            AnswerA TEXT,
            AnswerB TEXT,
            AnswerC TEXT,
            AnswerD TEXT,
            CorrectAnswer CHAR(1)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS userResult (
            resID INTEGER PRIMARY KEY AUTOINCREMENT,
            result TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultsDetail (
            resID INTEGER,
            quesID TEXT,
            urAns CHAR(1),
            FOREIGN KEY(resID) REFERENCES userResult(resID),
            FOREIGN KEY(quesID) REFERENCES questions(quesID)
        )
    ''')

    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()


createDatabase()
