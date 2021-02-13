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
          " https://math.stackexchange.com/questions/2111132/number-of-ways-to-choose-n-objects-from-groups-of-indistinguishable-objects\n")

    print("Asks how many ways are there to choose 8 from a multiset\n"
          "M = [5*['b']]+[6*['r']]+[7*['g']] (were b, r, g are refer to blue,\n"
    " red and green balls), or in other words:\n")

    M = [5*['b']]+[6*['r']]+[7*['g']]

    print(" M = ", M)

    print()

    print("Note that as a convention the generating functions internally sort\n"
          "with respect to the multiplicity size in the following manner:\n")

    M.sort(key=len, reverse=True)

    print(" M = ", M)

    print()

    print("That means that the corresponding multiplicity list is:\n")

    L=getMultListFromM(M)


    print(" L = ", L)

    print("\nIn short the solution can be calculated using any of the C functions\n"
          "were C2 is the best performing. We simply calculate it:\n\n"
          " C2(L, 8) = %d\n\n"
          "As easy as that, please note that the answer is identical to\n"
          "the published ones."%(C2(L, 8)))


    print()

    print("Notice that given the solution is more direct than the provided solutions\n")

    print("BTW, here are the unique elements:\n")

    for i, e in enumerate(MG(M, 8)):
        print(i, e)

    print()
