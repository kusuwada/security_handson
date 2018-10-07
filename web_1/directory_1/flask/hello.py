#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, send_file, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('directory.html', name='ゲスト')


@app.route('/image')
def image():
    image = request.args.get('image')
    if not image:
        abort(404)
    return send_file(os.path.join(os.getcwd(), 'static', image))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)