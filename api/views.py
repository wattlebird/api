# -*- coding: utf-8 -*-
from flask import jsonify, request
from ranker import retrive
from query import queryuser
from api import app, cache

def search_make_key():
    return u"{0}q{1}limit{2}".format(request.path, 
    request.args.get('q', default=u''),
    request.args.get('limit', default=-1, type=int))

@app.route('/search')
@cache.cached(timeout=3600, key_prefix=search_make_key)
def search():
    query = request.args.get('q', default=u'')
    limit = request.args.get('limit', default=None, type=int)
    return jsonify({'search':"user",
                    'query':query,
                    'result':queryuser(query, limit)})

def rank_make_key():
    id = request.args.get('id', default=None, type=int)
    if id is None:
        return u"{0}start{1}offset{2}method{3}".format(
            request.path,
            request.args.get('start', default=1, type=int),
            request.args.get('range', default=None, type=int),
            request.args.get('by', default='normal')
        )
    else:
        return u"{0}start{1}offset{2}method{3}".format(
            request.path,
            request.args.get('id', type=int),
            1,
            request.args.get('by', default='normal')
        )


@app.route('/rank')
@cache.cached(timeout=3600, key_prefix=rank_make_key)
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