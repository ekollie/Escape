import sqlite3

CONN = sqlite3.connect('./lib/sql/keys.db', timeout=10)

CURSOR = CONN.cursor()
