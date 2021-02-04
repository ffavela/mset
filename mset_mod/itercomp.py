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
    outStr1="""Just a series of simple tests for comparing the output of the
combinations of unique values as given by itertools (adding a
"unique" function) and the homebrewed multiset combinations.

First, a random multiset is created, it's number of fields
(multiset sets) spans from 1 to 8. Then the number of elements
each set has is also chosen. This gives a multiplicity list which
is sorted in descending order."""
    print(outStr1)

    MList= [getRandomMultiset(6, 3) for i in range(6)]
    LList=[getMultListFromM(M) for M in MList]

    print("Some examples of the multiplicity lists (using small vals for printing):\n")

    for L in LList:
        print("L = ", L)

    outStr2="""

Then a multiset is created using this multiplicity list where the
sets are simply multiple instances of letter of the alphabet.

    """

    print("\nSome examples of the multiset lists are (consistent with"
          " the respective multiplicities):\n")

    for M in MList:
        print("M = ", M)


    print('\n')

    outStr3="""The number of elements "k" that are chosen from the multiset is
also chosen randomly (between 1 and 8), note that if k>N (where N is the cardinality of
the multiset) then the end result is an empty list, that is, a list
with zero elements."""

    print(outStr3+'\n')

    print("The headers correspond to:")

    hMean="""Bool = checks if the unique itertools results are equal to the homebrewed generator
N1= the number of unique elements using itertools
N2= the number of unique elements using homebrew
T1=Time for running iter
T2=Time for running homebrew
Faster?= a boolean that tests if HB is faster than iter
countTime= time for the counting function
cTBool= checks if counting time is faster than homebrew generator
countFun= the result from the counting function
cBool=checks is the count result is identical to the iter version\n"""

    print(hMean)

    print("Executing some random examples, please be patient (do a control-C (or kill it!)"
          " and relaunch so you can convince yourself that it actually does something"
          " in case you got unlucky and it began with a tough one), bare in mind that"
          " the slow processes are due to the itertools part ;-)\n")

    print("Bool N1 N2 T1 T2 Faster? countTime cTBool countFun cBool")
    for i in range(10):
        k=random.randint(1, 8)
        M=getRandomMultiset(8, 8)
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
        count=C0(L,k)
        t5=time.time()

        countT=t5-t4

        cBool= uLen == count

        print(dumbCompare(uL, combM), uLen, cMLen,
              exeTR, exeTM, exeTR >= exeTM, countT,
              exeTM >= countT,
              count, cBool)


    print("\nNote that the \"traditional\" way is slower and that the homebrewed"
          " functions are not even optimized.\n")
