#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('../flask/users.db')
cursor = conn.cursor()

try:
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('CREATE TABLE users (name TEXT, password TEXT)')
    cursor.execute('INSERT INTO users VALUES (?, ?)', ('admin', 'SRyZ4iGAUy68Px6X'))
    conn.commit()
finally:
    cursor.close()
    conn.close()