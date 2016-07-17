import pandas as pd


def retrive(sort = 'rank', range_begin = 0, range_end = -1):
    """Get the rank result.
    Return formatted json string.
    """
    if sort!='rank':
        rst = result.sort_value(by=sort)
    else:
        rst = result

    if range_end==-1:
        range_end = result.shape[0]

    return [{'id':itm[1]['id'], 
             'title':itm[1]['title'], 
             'rank':itm[1]['rank'], 
             'bangumi_rank':itm[1]['bangumi_rank']
            } for itm in rst.iterrows()]