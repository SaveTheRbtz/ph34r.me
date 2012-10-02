#!/usr/bin/env python

import os
import random
from flask import Flask, Response

app = Flask(__name__)
quotes = tuple(open('quotes.txt'))

@app.route('/<path:filename>')
@app.route('/')
def index(filename='/'):
    return Response(random.choice(quotes), mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
