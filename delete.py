from connect import *
from read import *
import time


def deleteFilms():

 # use the filmID (unique key) to delete a record in the films table
    idField = int(input("Enter the filmID of the record to be deleted: "))
    cursor.execute(f"DELETE FROM films WHERE FilmID = {idField} ")
    conn.commit()
    print(f"Record {idField} deleted in the songs table")
    time.sleep(3)

    readFilms()  # call readSongs subroutine


if __name__ == "__main__":
    deleteFilms()

"""
# Delete a record
def delete_record():
	filmID = int(input("Enter filmID to delete"))
	conn.execute("DELETE FROM tblfilms WHERE filmID = ?", (filmID,))
	conn.commit()
"""
