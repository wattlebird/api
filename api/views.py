# -*- coding: utf-8 -*-
from flask import jsonify, request
from ranker import retrive
from query import queryuser
from api import app

@app.route('/search')
def search():
    query = request.args.get('q', default=u'')
    limit = request.args.get('limit', default=None, type=int)
    return jsonify({'search':"user",
                    'query':query,
                    'result':queryuser(q, limit)})


@app.route('/rank')
def rank():
    method = request.args.get('by', default='normal')
    b = request.args.get('start', default=1, type=int)
    r = request.args.get('range', default=None, type=int)
    id = request.args.get('id', default=None, type=int)
    if id is None:
        s = retrive(method, bg=b-1, rg=r)
    else:
        s = retrive(method, bg=id-1, rg=1)
    return jsonify({'rank':method,
                    'date':"2016-07-03",
                    'list':s})