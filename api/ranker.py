from db import db_session
from model import Rank

def retrive(sort, bg = 0, rg = 1):
    """Get the rank result.
    Return formatted json string.
    """
    if sort == 'normal':
        rank = Rank.rank.asc()
    elif sort == 'bangumi':
        rank = Rank.bangumi_rank.asc()

    if bg<0 or rg<=0:
        return []

    rst = db_session.query(Rank.id, Rank.title, Rank.rank, Rank.bangumi_rank).order_by(rank).offset(bg).limit(rg)

    return [{'id':itm[0],
             'title':itm[1],
             'rank':itm[2],
             'bangumi_rank':itm[3]
            } for itm in rst]