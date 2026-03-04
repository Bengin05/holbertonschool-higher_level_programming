#!/usr/bin/python3
"""List all states from the database, ordered by states.id ascending."""

import MySQLdb
import sys


def main():
    """Connect to MySQL and print all rows from the states table."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
