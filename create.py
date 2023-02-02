from connect import *
from read import *
import time


def insertFilms():

    films = []

    filmID = int(input("Enter filmID"))
    title = input("Enter title")
    yearReleased = int(input("Enter yearReleased"))
    rating = input("Enter rating")
    duration = int(input("Enter duration"))
    genre = input("Enter genre")
    conn.execute("INSERT INTO tblfilmsVALUES(?, ?, ?, ?, ?, ?)",
                 (filmID, title, yearReleased, rating, duration, genre))

    cursor.execute("INSERT INTO films VALUES ( NULL,?, ?, ?)", films)

    """
     films.append(filmID)
    films.append(title)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)
    
    """

    conn.commit()

    print(f"Title {title} added to the films table")
    time.sleep(3)

    readFilms()


if __name__ == "__main__":

    insertFilms()

    """
    # Add a record
def add_record():
	filmID = int(input("Enter filmID"))
	title = input("Enter title")
	yearReleased = int(input("Enter yearReleased"))
	rating = input("Enter rating")
	duration = int(input("Enter duration"))
	genre = input("Enter genre")
	conn.execute("INSERT INTO tblfilmsVALUES(?, ?, ?, ?, ?, ?)", (filmID, title, yearReleased, rating, duration, genre))
	conn.commit()

    
    
    """
