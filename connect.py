import sqlite3 as sql

# Create a connection object  that represent the database you want to create and/or use  in order  to
# use the SQLite module imported above
# connect() = connection method creates db and connect to it , if it does not exists. Otherwise it just connect
# to the existing db

conn = sql.connect("filmflix.db")

# T0 ensure that we can perform various database operations.
# # Now create a cursor object after establishing a connection above
# # and call its execute() method to perform SQL commands
# # cursor object

cursor = conn.cursor()

"""
import sqlite3

# Create the database
conn = sqlite3.connect('filmflix.db')

"""
