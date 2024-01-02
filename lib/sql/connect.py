import sqlite3

CONN = sqlite3.connect('./lib/sql/rooms.db', timeout=10)

CURSOR = CONN.cursor()
