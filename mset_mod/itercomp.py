import itertools as it
import timeit

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *


def getAllIterComb(S,k):
    return [list(e) for e in it.combinations(S, k)]

testcode = '''
import itertools as it
def getAllIterComb(S,k):
    return [e for e in it.combinations(S, k)]

S="mississippi"
k=3
getAllIterComb(S,k)
'''

print(timeit.timeit('output = 10*5'))

# print(timeit.timeit(stmt = testcode))
# for e in it.combinations("frankyrox", 3):
#     print(e)

S="mississippi"
S=sorted(list(S))
print(S)
k=5

R=getAllIterComb(S,k)
print(len(R))

# print(len(set(R))) #Unhashable in the current form

myR=zG(S,k)
print(len(myR))

print(dumbCompare(myR, R))

print(myR[0], R[0])

M = getMsetForm2(S)

print(M)

uL=getUniqueL(R)

print(len(uL))

combM=MG(M,k)
print(len(combM))

