from math import factorial
import operator as op
from functools import reduce
import sys

def tOp(xStr, LL):
    return [[xStr] + e for e in LL]

def G(S,k):
    N=len(S)
    def g(k,i=0):
        if k == 0:
            return [[]]
        nList=[]
        for j in range(i,N-k+1):
            nList += tOp(S[j],g(k-1,j+1))
        return nList
    return g(k)

def memoG(S,k):
    N=len(S)
    mD={}
    def g(k,i=0):
        if (k,i) in mD:
            return mD[(k,i)]
        if k == 0:
            mD[(k,i)] = [[]]
            return mD[(k,i)]
        nList=[]
        for j in range(i,N-k+1):
            nList += tOp(S[j],g(k-1,j+1))
        mD[(k,i)] = nList
        return mD[(k,i)]
    return g(k)

#Using left and right terms
def nG(S,k):
    N=len(S)
    def g(k,i=0):
        if k == 0:
            return [[]]
        nList=tOp(S[i],g(k-1,i+1))
        for j in range(i+1,N-k+1):
            nList += tOp(S[j],g(k-1,j+1))
        return nList
    return g(k)

#Using another form, notice the condition with "i" and not using the
#for loop.
def NG(S,k):
    N=len(S)
    def g(k,i=0):
        if k == 0:
            return [[]]
        if i == N-k:
            return tOp(S[i],g(k-1,i+1))
        return tOp(S[i],g(k-1,i+1))+g(k,i+1)
    return g(k)

#Using a "zero" value.
def zG(S,k):
    N=len(S)
    def g(k,i=0):
        if i > N-k:
            return []
        if k == 0:
            return [[]]
        return tOp(S[i],g(k-1,i+1))+g(k,i+1)
    return g(k)

#Helper function for the multiset generator
def nL(L):
    if L[0] == 1:
        return L[1:]
    return [L[0]-1]+L[1:]

#Making a multiset generator
def mG(M,k):
    M.sort(key=len, reverse=True)
    L=[len(m) for m in M]
    N=sum(L)
    S=[e for sublist in M for e in sublist]
    def g(k,L,i=0):
        if i > N-k:
            return [ ]
        if k == 0:
            return [[ ]]
        if i == N-k:
            return tOp(S[i],g(k-1,nL(L),i+1))
        return tOp(S[i],g(k-1,nL(L),i+1))+g(k,L[1:],i+L[0])
    return g(k,L)

#A simplified version, a nicer one.
def MG(M,k):
    M.sort(key=len, reverse=True)
    L=[len(m) for m in M]
    N=sum(L)
    S=[e for sublist in M for e in sublist]
    def g(k,L,i=0):
        if i > N-k:
            return [ ]
        if k == 0:
            return [[ ]]
        return tOp(S[i],g(k-1,nL(L),i+1))+g(k,L[1:],i+L[0])
    return g(k,L)

#Some helper functions for generating strings and putting in on the
#slides.
def getSet(bStr, N):
    return [bStr + "_{" + str(i) + "}" for i in range(N)]

def getLOfStr(LL):
    lOStr=[]
    for l in LL:
        newS="".join(l)
        lOStr.append(newS)
    return lOStr

#Some counting functions
def C(L,k):
    L.sort(reverse=True)
    N=sum(L)
    def c(L,k,i=0):
        if i > N-k:
            return 0
        if k == 0:
            return 1
        return c(nL(L),k-1,i+1)+c(L[1:],k,i+L[0])
    return c(L,k)

#############HELPER FUNCTIONS######################

def ncr(r,n):
    #Important condition
    if r > n or n < 0:
        return 0
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def myComb(k,N):
    if k > N or N < 0:
        return 0
    return int(factorial(N)/(factorial(k)*factorial(N-k)))
