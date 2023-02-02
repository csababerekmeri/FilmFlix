from connect import *
from read import *
import time


def updateFilms():
    # use the filmID (unique key) to update a record in the films table
    idField = input("Enter the filmID of the record to be updated: ")
    fieldName = input(
        "Which field would you like to update (Title/yearReleased/Rating/Duration/Genre)?: ").title()

    newFieldValue = input(f"Enter the new value for: {fieldName}: ")
    print(newFieldValue)
    # # add single quotes to newFieldValue o match the data in the songs table
    newFieldValue = "'" + newFieldValue + "'"
    print(newFieldValue)
    #  update songs table
    # UPDATE songs SET TitlE/Artist/Genre = Titel=dance/Artist=MJ/Genre=pop WHERE songID = 1/2/3/4/5/6....

    cursor.execute(
        f"UPDATE films SET {fieldName} = {newFieldValue} WHERE FilmID = {idField} ")
    conn.commit()
    print(f"Record {idField} updated in the films table")
    time.sleep(3)
    readFilms()


    # call readSongs subroutine
if __name__ == "__main__":
    updateFilms()

    """
    # Amend a record
def amend_record():
	filmID = int(input("Enter filmID to amend"))
	title = input("Enter title")
	yearReleased = int(input("Enter yearReleased"))
	rating = input("Enter rating")
	duration = int(input("Enter duration"))
	genre = input("Enter genre")
	conn.execute("UPDATE tblfilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ?", (title, yearReleased, rating, duration, genre, filmID))
	conn.commit()

    """
