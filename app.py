#!/usr/bin/env python

import os
import random
from flask import Flask, Response, abort

app = Flask(__name__)
quotes = tuple(open('quotes.txt'))

@app.route('/_keys/<path:key_id>.pub.asc')
def keys(key_id):
    try:
        key_str = hex(int(key_id, base=16))
    except ValueError:
        return abort(403)
    filename = '_keys/{0}.pub.asc'.format(key_str)
    try:
        with open(filename) as fp:
            return Response(fp.read(), mimetype='text/plain')
    except (IOError, OSError):
        return abort(404)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return Response(random.choice(quotes), mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
