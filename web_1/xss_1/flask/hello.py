#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask, make_response, render_template, request

app = Flask(__name__)
secret = os.environ['secret']


@app.route('/',  methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['Name']
    else:
        name = 'ゲスト'
    res = make_response(render_template('xss_form.html', name=name, secret=secret))
    res.headers.set('X-XSS-Protection', '0')
    res.set_cookie('secret', secret)
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)