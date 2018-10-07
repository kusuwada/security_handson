#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request

app = Flask(__name__)


class SiteInfo:
    title = 'Hello Application'


@app.route('/',  methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        name = request.form['Name']
        return render_template('hello.html',
                               title=SiteInfo.title,
                               name=name)
    else:
        return render_template('hello.html',
                               title=SiteInfo.title,
                               name='ゲスト')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)