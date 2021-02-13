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
          " https://math.stackexchange.com/questions/1556194/combinatorics-choosing-r-elements-from-a-multiset-of-n-elements-given-some-el\n")

    print("Asks how many ways there to choose 3 from a multiset\n"
          "M = [3*['a']]+[4*['b']]+[2*['c']], or in other words:\n")

    M = [3*['a']]+[4*['b']]+[2*['c']]

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
          " C2(L, 3) = %d\n\n"
          "As easy as that, please note that the answer is identical to\n"
          "the published ones."%(C2(L, 3)))


    print()

    print("Notice that given the solution involving a generating function\n"
          "by multiplying polynomia is slower... this actually suggest a faster\n"
          "way for doing this, a \"multiset theorem\" (not a multinomial theorem!)\n"
          "that provides the coeficients from polynomial multiplications much FASTER.\n")

    print("BTW, here are the unique elements:\n")

    for i, e in enumerate(MG(M, 3)):
        print(i, e)

    print()
