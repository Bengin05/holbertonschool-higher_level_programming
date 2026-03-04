#!/usr/bin/python3
"""List all cities of a given state from the database."""

import MySQLdb
import sys


def main():
    """Connect to MySQL and print all cities of the given state."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
