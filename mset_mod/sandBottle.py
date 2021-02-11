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
    print("\nImagine we have %d bottles each can hold %d sand particles." %(b, c))
    print("Suppose that each container has sand of only one color making\n"
          "all the sand particles of the same color indistinguishable.\n")
    N=sum(L)

    print("Now suppose that we mix the contents of the %d bottles and\n"
          "fill completely one bottle (with %d sand particles). How many\n"
          "different ways are there to fill that bottle?\n" %(b, c))

    k = 10**6
    print("We calculate simply C2(L, %d) = %d" %(k, C2(L, k)))

    print("So an interesting pattern appears of 5's, 0's and 1's.\n"
          "let's look a bit deeper, how about we choose powers of 10\n"
          "from the set:\n")

    i = 0
    while (10**i <= N):
        k = 10**i
        print(i, k, C2(L,k))
        i+=1

    print("\nWith the exception of the first 2 terms, the somewhat 501\n"
          "pattern emerges. There must be some simple expression behind.\n"
          "We can actually propose a sum of powers\n"
          "function that may \"simulate\" those results:\n\n"
          " f(i) = 5*10**(2*i-1)+1*10**i+5*10**(i-1)+1\n\n"
          "Granted, the 1 multiplying 10**i seems silly, it is there\n"
          "to give a bit of form. Let's test it while comparing to C2.\n")

    def f(i):
        return 5*10**(2*i-1)+1*10**i+5*10**(i-1)+1
    
    i = 0
    while (10**i <= N):
        k = 10**i
        print(i, k, C2(L,k), f(i))
        i+=1


    print("\nf(i) is able to reproduce exactly the same results as C2, even the first 2\n"
          "and it is even FASTER!! It is unclear at the moment if there\n"
          "is a general way to construct these functions.\n\n"
          "Note also that the first value is not 3 but 3.0. That means that the\n"
          "f(i) calculation was not done purely in the realm of the integers.\n")
