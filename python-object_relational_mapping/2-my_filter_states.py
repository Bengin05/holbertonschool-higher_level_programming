#!/usr/bin/python3
"""List all states from the database with names starting with 'N'."""
import MySQLdb
import sys


def main():
    """Connect to MySQL and print states with names starting with 'N'."""

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
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY states.id ASC"
    ).format(state_name)
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
