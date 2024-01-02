import sqlite3

CONN = sqlite3.connect('./lib/data.db', timeout=10)

CURSOR = CONN.cursor()
