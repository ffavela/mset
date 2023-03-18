import time

import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *


if __name__ == '__main__':

    print("### CHANGE THE VARIABLES IN THE CODE TO GRASP IT BETTER ;-) ###\n")

    print("Suppose that you have the following multiset:\n")
    # M=[4*['a'], 2*['b'], ['c']]
    # M=[['c'], 2*['b'], 4*['a']]
    M=[['c'], 3*['a'], 3*['b'], 6*['d']]
    L=getMultListFromM(M)
    print("The multiplicity list is L =", L)
    k=4

    print(" M = ", M)

    print()

    print("That means that the multiplicity list is:\n")

    
    print(" L = ", L)

    n=len(L)
    N=sum([e for e in L])

    print()
    
    print("That means that there are n = %d sets with N = %d total number of elements"
          %(n, N))
    
    
    print("If we were to choose k = %d unique elements and generate all the terms\n"
          "we can use the MG(M, k) function whose output gives:" %(k))

    print()

    #Just avoiding M to be innadvertively sorted
    MM=M.copy()
    outMG=MG(MM, k)

    for i, e in enumerate(outMG):
        print(i, e)

    print()

    print("The unsorted version")

    newOutMG=nMG(M, k)

    for i, e in enumerate(newOutMG):
        print(i, e)

    print()

    cResultLen = len(outMG)
    comb=nck(N, k)

    print("Note that there are %d different solutions which is clearly\n"
          "different from the expected one when using tradicional combinatorics:\n\n"
          " nck(%d, %d) = %d\n\nAnd also different from the tradicional way of doing\n"
          "combinations with repetitions (multicombinations), normally referred as the\n"
          "stars and bars approach:\n\n nck(n+k-1, k) = nck(%d+%d-1, %d) = %d\n\n"
          "Since there are constraints imposed by the limited repeat nature of the multiset.\n"
          %(cResultLen, N, k, nck(N, k), n, k, k,  nck(n+k-1,k)))

    cResult = C2(L, k)
    print("If we use the optimized counting function C2(L, k), see core.py at the libraries,\n"
          "we obtain:\n")

    print(" C2(L, %d) = %d \n" %(k, cResult))

    nCResult = nC2(L, k)

    print("The unsorted mult list version gives ", nCResult)
    print("Which gives exactly the total number of elements as previously enumerated.\n")

    print("It turns out that this problem has multiple equivalences, see also bucketKtuple.py")
