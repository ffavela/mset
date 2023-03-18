import sys
import numpy as np
from mset_lib.miscellaneous import *

def tOp(xStr, LL):
    return [[xStr] + e for e in LL]

def tOpV(v, LV):
    return [v + lv for lv in LV]

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
def wL(L):
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
            return tOp(S[i],g(k-1,wL(L),i+1))
        return tOp(S[i],g(k-1,wL(L),i+1))+g(k,L[1:],i+L[0])
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
        return tOp(S[i],g(k-1,wL(L),i+1))+g(k,L[1:],i+L[0])
    return g(k,L)

#trying out a version without sorting
def nMG(M,k):
    L=[len(m) for m in M]
    N=sum(L)
    S=[e for sublist in M for e in sublist]
    def g(k,L,i=0):
        if i > N-k:
            return [ ]
        if k == 0:
            return [[ ]]
        return tOp(S[i],g(k-1,wL(L),i+1))+g(k,L[1:],i+L[0])
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


#A special vector list generator, pretty useful B-)
def V0(L,k):
    L.sort(reverse=True)
    N=sum(L)
    e=np.identity(len(L), dtype=int)
    z=np.zeros(len(L), dtype=int)

    def J(i):
        s=0
        for j,l in enumerate(L):
            s+=l
            if i < s:
                return j

    def v(k,L,i=0):
        if i > N-k:
            return [ ]
        if k == 0:
            return [z]
        return tOpV(e[J(i)],v(k-1,wL(L),i+1))+v(k,L[1:],i+L[0])

    return v(k,L)

#Optimizing it
def V1(L,k):
    L.sort(reverse=True)
    N=sum(L)
    e=np.identity(len(L), dtype=int)
    z=np.zeros(len(L), dtype=int)
    dictV={}

    def J(i):
        s=0
        for j,l in enumerate(L):
            s+=l
            if i < s:
                return j

    def v(k,L,i=0):
        if (tuple(L), k) in dictV:
            return dictV[(tuple(L), k)]
        if i > N-k:
            dictV[(tuple(L), k)] = []
            return dictV[(tuple(L), k)]
        if k == 0:
            dictV[(tuple(L), k)] = [z]
            return dictV[(tuple(L), k)]
        dictV[(tuple(L), k)] = tOpV(e[J(i)],v(k-1,wL(L),i+1))+v(k,L[1:],i+L[0])
        return dictV[(tuple(L), k)]

    return v(k,L)


#Getting the combinatorial coeficients for each possibility.  This may
#need to be optimized.
def getCombCoefAL(L, k):
    vL=V0(L,k)
    ccAL=[]
    for v in vL:
        ccAL.append(np.array([nck(l,e)\
                              for l, e in zip(L, v)], dtype=np.ulonglong))
    return ccAL

def getCombCoefL(L, k):
    vL=V0(L,k)
    ccL=[]
    for v in vL:
        ccL.append(np.array([nck(l,e)\
                             for l, e in zip(L, v)], dtype=np.ulonglong).prod())
    return ccL

#Some counting functions
def C0(L,k):
    L.sort(reverse=True)
    N=sum(L)
    def c(L,k,i=0):
        if i > N-k:
            return 0
        if k == 0:
            return 1
        return c(wL(L),k-1,i+1)+c(L[1:],k,i+L[0])
    return c(L,k)

def C1(L,k):
    L.sort(reverse=True)
    N=sum(L)
    def c(L,k,i=0):
        if i > N-k:
            return 0
        if k == 0:
            return 1
        if k <= min(L):
            return nck(len(L)+k-1,k)
        return c(wL(L),k-1,i+1)+c(L[1:],k,i+L[0])
    return c(L,k)

#The memoized version
def C2(L,k):
    L.sort(reverse=True)
    N=sum(L)
    mDict={}
    def c(L,k,i=0):
        if (tuple(L), k) in mDict:
            return mDict[(tuple(L), k)]
        elif i > N-k:
            mDict[(tuple(L), k)] = 0
            return mDict[(tuple(L), k)]
        elif k == 0:
            mDict[(tuple(L), k)] = 1
            return mDict[(tuple(L), k)]
        elif  k <= min(L):
            mDict[(tuple(L), k)] = nck(len(L)+k-1,k)
            return mDict[(tuple(L), k)]
        mDict[(tuple(L), k)] = c(wL(L),k-1,i+1)+c(L[1:],k,i+L[0])
        return mDict[(tuple(L), k)]
    return c(L,k)

#Testing out a version without the sorting preprocessing.
def nC2(L,k):
    # L.sort(reverse=True)
    N=sum(L)
    mDict={}
    def c(L,k,i=0):
        if (tuple(L), k) in mDict:
            return mDict[(tuple(L), k)]
        elif i > N-k:
            mDict[(tuple(L), k)] = 0
            return mDict[(tuple(L), k)]
        elif k == 0:
            mDict[(tuple(L), k)] = 1
            return mDict[(tuple(L), k)]
        elif  k <= min(L):
            mDict[(tuple(L), k)] = nck(len(L)+k-1,k)
            return mDict[(tuple(L), k)]
        mDict[(tuple(L), k)] = c(wL(L),k-1,i+1)+c(L[1:],k,i+L[0])
        return mDict[(tuple(L), k)]
    return c(L,k)


#Profiting from the k, N-k symmetry. Usage is not recomended I wont go
#into it, C2 seems better.
def C3(L,k):
    L.sort(reverse=True)
    N=sum(L)
    mDict={}
    def c(L,k,i=0):
        if (tuple(L), k) in mDict:
            if (tuple(L), sum(L)-k) not in mDict:
                mDict[(tuple(L), sum(L) - k)] = mDict[(tuple(L), k)]
            return mDict[(tuple(L), k)]
        elif i > N-k:
            mDict[(tuple(L), k)] = 0
            return mDict[(tuple(L), k)]
        elif k == 0:
            mDict[(tuple(L), k)] = 1
            return mDict[(tuple(L), k)]
        elif  k <= min(L):
            mDict[(tuple(L), k)] = nck(len(L)+k-1,k)
            return mDict[(tuple(L), k)]
        mDict[(tuple(L), k)] = c(wL(L),k-1,i+1)+c(L[1:],k,i+L[0])
        return mDict[(tuple(L), k)]
    return c(L,k)
