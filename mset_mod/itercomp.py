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

if __name__ == '__main__':
    import timeit

    print(timeit.timeit('output = 10*5'))

    S="mississippi"
    S=sorted(list(S))
    print(S)
    k=5

    R=getAllIterComb(S,k)
    print(len(R))

    # print(len(set(R))) #Unhashable in the current form

    myR=zG(S,k)
    print(len(myR))

    print(timeit.timeit(stmt='dumbCompare(myR, R)',
                        globals=globals(), number=5))

    print(dumbCompare(myR, R))
    print(myR[0], R[0])

    M = getMsetForm2(S)

    print(M)

    uL=getUniqueL(R)

    print(len(uL))

    combM=MG(M,k)
    print(len(combM))


    for i in range(10):
        # L=getRandomMultList(10, 10)

        # print(L)

        M=getRandomMultiset(10, 10)
        # print(M)
        S=flattenList(M)
        # print(S)

        R=getAllIterComb(S,k)
        uL=getUniqueL(R)

        str4Time="""
R=getAllIterComb(S,k)
uL=getUniqueL(R)
        """

        exeTR=timeit.timeit(stmt=str4Time,
                            globals=globals(), number=1)

        uLen=len(uL)

        combM=MG(M,k)
        exeTM=timeit.timeit(stmt="MG(M,k)",
                            globals=globals(), number=1)

        cMLen=len(combM)

        print(dumbCompare(uL, combM), uLen, cMLen, exeTR, exeTM, exeTR >= exeTM)
