#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def login():
    name = ''
    password = ''
    error = ''
    
    if request.method == 'POST':
        error = 'Login failed!'
        name = request.form['Name']
        password = request.form['Password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        query = 'SELECT * FROM users WHERE name=\'{name}\' AND password=\'{password}\''.format(name=name, password=password)
        try:
            cursor.execute(query)
            users = cursor.fetchone()
        finally:
            cursor.close()
            conn.close()
        if users:
            return render_template('congras.html', users=users)
    
    return render_template('sqli.html', error=error)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)