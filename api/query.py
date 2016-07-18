import cPickle

from db import db_session
from model import User

with open("search.pkl", 'rb') as fr:
    idquery = cPickle.load(fr)
    nicknamequery = cPickle.load(fr)


def queryuser(q, limit=10):
    """return a list of dicted queries.
    """
    _, idx1 = idquery.query(q)
    _, idx2 = nicknamequery.query(q)
    idx = list(set(idx1 + idx2))
    rst = db_session.query(User.id, User.nickname).filter(User.index.in_(idx)).\
          order_by(User.score.desc(), User.active.asc()).limit(limit).all()
    return [{'id':itm[0], 'name':itm[1]} for itm in rst]
