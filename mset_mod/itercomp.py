import itertools as it
import timeit

import sys
sys.path.append('../')
from mset_lib.core import *


def getAllIterComb(S,k):
    return [e for e in it.combinations(S, k)]

testcode = '''
import itertools as it
def getAllIterComb(S,k):
    return [e for e in it.combinations(S, k)]

S="frankyrox"
k=3
getAllIterComb(S,k)
'''

print(timeit.timeit('output = 10*5'))

print(timeit.timeit(stmt = testcode))
# for e in it.combinations("frankyrox", 3):
#     print(e)

S="frankyrox"
k=5

R=getAllIterComb(S,k)
print(len(R))
print(len(set(R)))

print(len(zG(S,k)))
