import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('QuestionBank.db')
cursor = conn.cursor()

# Version, Server check
cursor.execute("SELECT sqlite_version()")
print("SQLite version:", cursor.fetchone())

# Describe table
cursor.execute("PRAGMA table_info(questions)")
print("Table 'questions':", cursor.fetchall())

cursor.execute("PRAGMA table_info(userResult)")
print("Table 'userResult':", cursor.fetchall())

cursor.execute("PRAGMA table_info(resultsDetail)")
print("Table 'resultsDetail':", cursor.fetchall())

# Select all data from tables
cursor.execute("SELECT * FROM questions")
print("Data in 'questions':", cursor.fetchall())

cursor.execute("SELECT * FROM userResult")
print("Data in 'userResult':", cursor.fetchall())

cursor.execute("SELECT * FROM resultsDetail")
print("Data in 'resultsDetail':", cursor.fetchall())

# Delete data
cursor.execute("DELETE FROM questions")
cursor.execute("DELETE FROM userResult")
cursor.execute("DELETE FROM resultsDetail")

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
