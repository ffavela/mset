import sys
import math

sys.setrecursionlimit(5000)

print(sys.getrecursionlimit())

def H1(N,k):#hockey stick
    if k==0:
        return 1
    return sum([H1(i,k-1) for i in range(k-1,N)])

# def H2(N,k): # put the reverse one here
#     if k==0:
#         return 1

def h(N,k):
    def Nh(k,i=0):
        if k == 0:
            return 1
        return sum([Nh(k-1,j+1) for j in range(i,N-k+1)])
    if k > N:
        return 0
    return Nh(k)

def getBFromU(N,k,u):
    """given math.comb(N,k) find the path "B" for solution u"""
    u+=1 #New
    def f(N,k,s=0,b=[]):
        if k<0:
            return b
        l=math.comb(N,k)
        t=s+l
        if u<=t:
            return f(N-1,k-1,s,b+[0])#descend left
        return f(N-1,k,t,b+[1])#descend right
    return f(N-1,k-1)

def getILL(N,k):
    """Returns a list of lists of indices"""
    def w(i,L):
        return [ [i] + e for e in L]
    def f(k,i=0):
        if i > N-k:
            return []
        if k == 0:
            return [[]]
        return w(i,f(k-1,i+1)) + f(k,i+1)
    return f(k)

def getBFromIL(I):
    """Returns a list of lists of 0s and 1s"""
    B = I[0]*[1] + [0]
    base = I[0]+1
    for i in I[1:]:
        B += (i-base)*[1] + [0]
        base = i+1
    return B

def getIFromB(B):
    I=[]
    c=0
    for b in B:
        if b==0:
            I+=[c]
        c+=1
    return I

def getUFromB(N,k,B):
    u=0 #Better u=0?
    if B == []:
        return math.comb(N,k)
    for b in B:
        l=math.comb(N-1,k-1)
        if b == 1:
            u+=l
        else: #b==0
            k-=1
        N-=1
    return u

def getListWithoutIndex(i,L):
    if len(L) == 1:
        return []
    return L[:i]+L[i+1:]

def w(e,LL):
    return [[e] + L for L in LL]

def getPermutedLists(L):
    """Given a list it returns a list of lists with all the possible
permutations"""
    if len(L) == 1:
        return [[L[0]]]
    pL = []
    for i,e in enumerate(L):
        nL=getListWithoutIndex(i,L)
        pL+=w(e,getPermutedLists(nL))
    return pL

def getPermutationListFromU(N,u,p=[],aL=[]):
    if aL == []:
        aL=list(range(N))
    if N == 0:
        return p
    I=u//math.factorial(N-1)
    return getPermutationListFromU(N-1,u%math.factorial(N-1),p+[aL[I]],getListWithoutIndex(I,aL))

def getUFromPermutationList(p):
    N=len(p)#Can be eliminated by N=len(aL) on each descent
    aL=list(range(N))
    def g(p,N,aL):
        if p == []:
            return 0
        I=aL.index(p[0])
        return I*math.factorial(N-1)+g(p[1:],N-1,getListWithoutIndex(I,aL))
    return g(p,N,aL)
