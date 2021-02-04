from math import factorial
import operator as op
from functools import reduce
import random

def nck(n,k):
    #Important condition
    if k > n or n < 0:
        return 0
    k = min(k, n-k)
    numer = reduce(op.mul, range(n, n-k, -1), 1)
    denom = reduce(op.mul, range(1, k+1), 1)
    return numer // denom

def myComb(k,N):
    if k > N or N < 0:
        return 0
    return int(factorial(N)/(factorial(k)*factorial(N-k)))

def dumbCompare(x,y):
    """ Surely there is a better way but it furfills the intended purpose"""
    for ex in x:
        if ex not in y:
            print("ex", ex)
            return False
    for ey in y:
        if ey not in x:
            print("ey", ey)
            return False
    return True

def getMsetForm2(L):
    d={}
    for e in L:
        if e not in d:
            d[e]=0
        d[e]+=1
    M=[ d[e]*[e] for e in d]
    M.sort(key=len, reverse=True)
    return M

def getUniqueL(L):
    uL=[]
    for e in L:
        if e not in uL:
            uL.append(e)
    return uL

def getRandomMultList(maxField, maxMult):
    fieldN = random.randint(1, maxField)
    return sorted([random.randint(1,maxMult) for e in range(fieldN)],
                  reverse=True)

def getRandomMultiset(maxField, maxMult):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    L=getRandomMultList(maxField, maxMult)
    fieldN=len(L)
    return [n*[alphabet[i]] for i,n in enumerate(L)]

def flattenList(M):
    return [e for sublist in M for e in sublist]

def getMultListFromM(M):
    return [len(m) for m in M ]
