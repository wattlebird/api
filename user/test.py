from model import *
from fast_query import *

uid = []
breakpoint = []
namestr = ''
for q in session.query(User.name, User.uid).order_by(User.uid):
    if q.name.isdigit(): continue;
    breakpoint.append(len(namestr))
    uid.append(int(q.uid))
    namestr+=(q.name+'$')

queryer = SuffixArrayInterface(namestr)
queryer.build()
queryer.query('abc')

