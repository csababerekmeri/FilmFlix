from connect import *


def readFilms():
    cursor.execute("SELECT * FROM films")
    row = cursor.fetchall()

    for record in row:
        print(record)


if __name__ == "__main__":

    readFilms()

"""
    # Print all records in the tblfilms table
def print_all_records():
        cursor = conn.execute("SELECT * FROM tblfilms")
        for row in cursor:
                print("FilmID = ", row[0])
                print("Title = ", row[1])
                print("YearReleased = ", row[2])
                print("Rating = ", row[3])
                print("Duration = ", row[4])
                print("Genre = ", row[5])
                print()
    """
