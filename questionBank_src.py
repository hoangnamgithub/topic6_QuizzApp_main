#  Name: Nguyen Hoang Nam
#  StudentID: 20227247
#  Class: 738657 - MI3310
#  Project: Final Project - Topic 6

import pyodbc


def createDatabase():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=HOANGNAM\\SQLEXPRESS;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM master.sys.databases WHERE name = 'QuestionBank'")
    if not cursor.fetchone():
        cursor.close()
        conn.close()

        # Reconnect to the server
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=HOANGNAM\\SQLEXPRESS;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('CREATE DATABASE QuestionBank')
        conn.commit()

    cursor.close()
    conn.close()


def createTables():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=HOANGNAM\\SQLEXPRESS;'
                          'Database=QuestionBank;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    # Check for table 'questions' existent
    cursor.execute(
        "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'questions'")
    if not cursor.fetchone():
        cursor.execute('''
        CREATE TABLE questions (
            quesID VARCHAR(255) PRIMARY KEY,
            Question VARCHAR(255),
            AnswerA VARCHAR(255),
            AnswerB VARCHAR(255),
            AnswerC VARCHAR(255),
            AnswerD VARCHAR(255),
            CorrectAnswer CHAR(1),
        )
        ''')

    # Check for table 'userResult' existent
    cursor.execute(
        "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'userResult'")
    if not cursor.fetchone():
        cursor.execute('''
        CREATE TABLE userResult (
            resID INT IDENTITY(1,1) PRIMARY KEY,
            result VARCHAR(255)
        )
        ''')

    # Check for table 'resultsDetail' existent
    cursor.execute(
            "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'resultsDetail'")
    if not cursor.fetchone():
        cursor.execute('''
        CREATE TABLE resultsDetail (
            resID INT,
            quesID VARCHAR(255),
            urAns CHAR(1),
            FOREIGN KEY(resID) REFERENCES userResult(resID),
            FOREIGN KEY(quesID) REFERENCES questions(quesID)
        )
        ''')

    conn.commit()
    conn.close()
