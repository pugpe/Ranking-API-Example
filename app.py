#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import default_app, request, route, response, get, post, abort, template

bottle.debug(True)

db = {'brunno':{'nome':'brunno', 'rank':5, 'level':'awesome!' }}

@get('/')
def index():
    return 'You should be using me as an API!'

@post('/players')
def post_player():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    player = eval(data)
    i = player.keys().pop()
    db[i] = player[i]
    return db[i]
    
@get('/players/:name')
def get_player(name):
    if not db.has_key(name):
        abort(404, 'Player %s not found' % id)
    return db[name]

bottle.run(host='0.0.0.0', port=argv[1])
