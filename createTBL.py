from connect import *


# Insert records into the table
conn.execute(
    "INSERT INTO tblfilms VALUES(1, 'The Godfather', 1972, 'R', 175, 'Crime')")
conn.execute(
    "INSERT INTO tblfilms VALUES(2, 'The Shawshank Redemption', 1994, 'R', 142, 'Drama')")
conn.execute(
    "INSERT INTO tblfilms VALUES(3, 'Schindler's List', 1993, 'R', 195, 'Biography')")
conn.execute(
    "INSERT INTO tblfilms VALUES(4, 'Raging Bull', 1980, 'R', 129, 'Biography')")
conn.execute(
    "INSERT INTO tblf VALUES(5, 'Casablanca', 1942, 'PG', 102, 'Romance')")
conn.execute(
    "INSERT INTO tblfilms VALUES(6, 'Citizen Kane', 1941, 'PG', 119, 'Drama')")

# Save changes
conn.commit()

# Close the connection
conn.close()


"""
# Create the table
conn.execute('''CREATE TABLE tblfilms
			(filmID integer,
			title text,
			yearReleased integer,
			rating text,
			duration integer,
			genre text)''')

# Insert records into the table
conn.execute(
    "INSERT INTO tblfilms VALUES(1, 'The Godfather', 1972, 'R', 175, 'Crime')")
conn.execute(
    "INSERT INTO tblfilms VALUES(2, 'The Shawshank Redemption', 1994, 'R', 142, 'Drama')")
conn.execute(
    "INSERT INTO tblfilms VALUES(3, 'Schindler's List', 1993, 'R', 195, 'Biography')")
conn.execute(
    "INSERT INTO tblfilms VALUES(4, 'Raging Bull', 1980, 'R', 129, 'Biography')")
conn.execute(
    "INSERT INTO tblf VALUES(5, 'Casablanca', 1942, 'PG', 102, 'Romance')")
conn.execute(
    "INSERT INTO tblfilms VALUES(6, 'Citizen Kane', 1941, 'PG', 119, 'Drama')")

# Save changes
conn.commit()

# Close the connection
conn.close()

"""
