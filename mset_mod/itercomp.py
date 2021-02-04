import itertools as it
import timeit
import time

import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *


def getAllIterComb(S,k):
    """
    It uses the itertools library to generate all the combinations
    """
    return [list(e) for e in it.combinations(S, k)]

if __name__ == '__main__':
    outStr1=""" Just a series of simple tests for comparing the output of the
    combinations of unique values as given by itertools (adding a
    "unique" function) and the homebrewed multiset combinations.

    First, a random multiset is created, it's number of fields
    (multiset sets) spans from 1 to 10. Then the number of elements
    each set has is also chosen. This gives a multiplicity list which
    is sorted in descending order."""
    print(outStr1)


    print("Some examples of the multiplicity lists:")

    for i in range(6):
        print(getRandomMultList(10, 10))

    outStr2="""

    Then a multiset is created using this multiplicity list where the
    sets are simply multiple instances of letter of the alphabet.

    """

    print("Some examples of the multiset lists are:")

    for i in range(6):
        print(getRandomMultiset(6, 3))


    print('\n')

    outStr3=""" The number of elements "k" that are chosen from the multiset is
also chosen randomly, note that if k>N (where N is the cardinality of
the multiset) then the end result is an empty list, that is, a list
with zero elements."""

    print(outStr3+'\n')

    print("Executing some random examples, please be patient (do a control-C (or kill it!)"
          " and relaunch so you can convince yourself that it actually does something"
          " in case you got unlucky and it begun with a tough one):\n")

    print("Bool N1 N2 T1 T2 Faster? countTime countFun")
    for i in range(10):
        k=random.randint(4, 6)
        M=getRandomMultiset(10, 10)
        L=getMultListFromM(M)#Just for counting
        S=flattenList(M)

        t0=time.time()
        R=getAllIterComb(S,k)
        uL=getUniqueL(R)
        t1=time.time()
        exeTR=t1-t0

        uLen=len(uL)

        t2=time.time()
        combM=MG(M,k)
        t3=time.time()
        exeTM=t3-t2

        cMLen=len(combM)

        t4=time.time()
        count=C(L,k)
        t5=time.time()

        countT=t5-t4

        print(dumbCompare(uL, combM), uLen, cMLen,
              exeTR, exeTM, exeTR >= exeTM, countT,
              count)
