import random

class SuffixArrayInterface(object):
    def __init__(self, namestr):
        if namestr:
            self.breakchar = namestr[-1]
        else:
            self.breakchar = '$'
            namestr='$'
        self.namestr = namestr

        strptr = []
        idxtable = []
        idx = 0
        for i in xrange(len(namestr)):
            if namestr[i]!=self.breakchar:
                strptr.append(i)
                idxtable.append(idx)
            else:
                idxtable.append(-1)
                idx=i+1
        self.strptr = strptr
        self.idxtable = idxtable
        self.sorted = False

    def _strcomp(self, i, j):
        """
        return 0: equal
        1: str_j is lexicographically bigger than str_i
        -1: str_j is lexicographically smaller than str_i
        """
        while self.namestr[i]!=self.breakchar and self.namestr[j]!=self.breakchar:
            if self.namestr[i]==self.namestr[j]:
                i+=1
                j+=1
            elif self.namestr[i]<self.namestr[j]:
                return 1
            else:
                return -1

        if self.namestr[i]==self.breakchar and self.namestr[i]==self.namestr[j]:
            return 0
        elif self.namestr[j]==self.breakchar:
            return -1
        elif self.namestr[i]==self.breakchar:
            return 1
        else:
            raise

    def _externalstrcmp(self, i, s):
        """
        s must be ended with self.breakchar
        return 0: equal
        1: s is lexicographically bigger than str_i
        -1: s is lexicographically smaller than str_i
        """
        j=0
        while self.namestr[i]!=self.breakchar and s[j]!=self.breakchar:
            if self.namestr[i]==s[j]:
                i+=1
                j+=1
            elif self.namestr[i]<s[j]:
                return 1
            else:
                return -1

        if self.namestr[i]==self.breakchar and self.namestr[i]==s[j]:
            return 0
        elif s[j]==self.breakchar:
            return -1
        elif self.namestr[i]==self.breakchar:
            return 1
        else:
            raise

    def _qsort(self, x):
        if len(x)<=1: return
        # choose a pivit
        i = random.choice(xrange(len(x)))
        x[0], x[i] = x[i], x[0]

        q = len(x)
        r = len(x)
        p = len(x)-1
        while p>=0:
            rst = self._strcomp(x[0], x[p])
            if rst>0:
                r-=1;
                q-=1
                x[q], x[p] = x[p], x[q]
                x[q], x[r] = x[r], x[q]
            elif rst==0:
                q-=1
                x[q], x[p] = x[p], x[q]
            p-=1
        t1=x[:q]
        t2=x[r:]
        self._qsort(t1)
        self._qsort(t2)
        x[:q]=t1
        x[r:]=t2


    def _lower_bound(self, q):
        "return the left most position that no less than query"
        b = 0
        e = len(self.strptr)
        while e-b>1:
            m = b+(e-b)/2
            if self._externalstrcmp(self.strptr[m], q)==1:
                b=m
            else:
                e=m
        return e

    def _upper_bound(self, q):
        "Returns first element in the range which compares greater than q."
        b = 0
        e = len(self.strptr)
        while e-b>1:
            m = b+(e-b)/2
            if self._externalstrcmp(self.strptr[m], q)>=0:
                b=m
            else:
                e=m
        return e

    def query(self, q):
        if self.sorted == False:
            raise Exception("Suffix array not sorted first. Please call build before this.")
        b = self._lower_bound(q+self.breakchar)
        e = self._upper_bound(q+self.breakchar)
        if e<=b:
            return []

        rtn = [self.idxtable[self.strptr[i]] for i in xrange(b, e)]
        rtn = list(set(rtn))
        return rtn

    def build(self):
        x = self.strptr
        self._qsort(x)
        self.strptr = x
        self.sorted = True
