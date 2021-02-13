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
          " https://math.stackexchange.com/questions/210302/how-many-ways-balls-can-be-selected\n")

    print("Asks how many ways are there to choose 25 balls from a multiset\n"
          "M = [15*['r']]+[20*['b']]+[25*['g']] (were b, r, g are refer to blue,\n"
    " red and green balls), or in other words:\n")

    M = [15*['r']]+[20*['b']]+[25*['g']]

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
          " C2(L, 25) = %d\n\n"
          "As easy as that, please note that the answer is identical to\n"
          "the published ones."%(C2(L, 25)))


    print()

    print("Notice that given the solution is more direct than the provided solutions\n")

    print("BTW, uncomment the following lines to see all the elements:\n")

    # for i, e in enumerate(MG(M, 25)):
    #     print(i, e)

    print()
