# -*- coding: utf-8 -*-
from flask import jsonify, request
from rank import retrive
from user import queryuser
from api import app

@app.route('/search')
def search():
    query = request.args.get('q', default=u'')
    limit = request.args.get('limit', default=None, type=int)
    return jsonify({'search':'anime',
                    'query':query,
                    'result':queryuser(query, limit)})


@app.route('/rank')
def rank():
    sort = request.args.get('by', default='id')
    if sort=='bangumi':
        sort = 'bangumi_rank'
    b = request.args.get('start', default=0, type=int)
    e = request.args.get('end', default=-1, type=int)
    id = request.args.get('id', default=None, type=int)
    if id is not None:
        s = retrive(rank=rank, range_begin=b-1, range_end=e)
    else:
        s = retrive(rank=rank, range_begin=id-1, range_end=id)
    return jsonify({'rank':'anime',
                    'date':2016-07-03,
                    'list':s})