import pandas as pd
import cPickle
import fast_query

userlist = pd.read_hdf("search.hdf", 'user')
with open("search.pkl", 'rb') as fr:
    idquery = cPickle.load(fr)
    nicknamequery = cPickle.load(fr)


def queryuser(q, limit=10):
    """return a list of dicted queries.
    """
    _, idx1 = idquery.query(q)
    _, idx2 = nicknamequery.query(q)
    idx = list(set(idx1+idx2))
    ans = userlist.ix[idx].sort_values(by=['score', 'active'], ascending=[False, True])
    if limit is None:
        return [{'id':itm[1]['id'], 'name':itm[1]['nickname']} for itm in ans.iterrows()]
    else:
        return [{'id':itm[1]['id'], 'name':itm[1]['nickname']} for itm in ans[:limit].iterrows()]
