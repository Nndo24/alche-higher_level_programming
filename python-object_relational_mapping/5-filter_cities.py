#!/usr/bin/python3
"""
Lists all cities of a state given as an argument from hbtn_0e_4_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s ORDER BY cities.id ASC",
        (state_name,)
    )
    rows = cursor.fetchall()

    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cursor.close()
    db.close()
