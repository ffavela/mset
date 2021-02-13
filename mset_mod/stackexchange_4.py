import time

import random
import matplotlib.pyplot as plt

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *

if __name__ == "__main__":
    b=3
    c=10**6
    L=b*[c]

    print("\nThe stack exchange post:\n\n"
          " https://math.stackexchange.com/questions/148243/number-of-k-combinations-of-a-multiset\n")

    print("Asks how many ways are there to choose 4 characters from the word \"POSSESSES\" \n")

    w="POSSESSES"
    
    M = getMFromS(list(w))

    print("In other words it asks to choose 4 from the multiset:\n")

    print(" M = ", M)

    print()

    print("That means that the corresponding multiplicity list is:\n")

    L=getMultListFromM(M)


    print(" L = ", L)

    print("\nIn short the solution can be calculated using any of the C functions\n"
          "were C2 is the best performing. We simply calculate it:\n\n"
          " C2(L, 4) = %d\n\n"
          "As easy as that, (no inclusion exclusion principle is invoked)\n"
          "please note that the answer is identical to\n"
          "the published ones."%(C2(L, 4)))


    print()

    print("Notice that given the solution is more direct than the provided solutions\n")

    print("BTW, the unique elements are:\n")

    for i, e in enumerate(MG(M, 4)):
        print(i, e)

    print()
