import time

import random
import matplotlib.pyplot as plt

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *

if __name__ == "__main__":
    b=8
    c=10
    L=b*[c]
    print("Imagine we have %d buckest each with capacity %d." %(b, c))
    print("That is equivalent of having a multiplitity list L = ", L)
    N=sum(L)
    print("This means that the maximum capacity is %d." %(N))

    k=N//2
    # k=10 #This one has the bool as True

    print("If we were to place k = %d balls in L then there are a total of\n"
          "C(L,k) = %d different configurations.\n" %(k, C2(L,k)))

    print("Each configuration has a combinatorial weight which has to sum\n"
          "exactly nck(%d,%d) = %d. So lets test this, this might take a few minutes\n"
          "A list with the %d configurations will be filled with their weight,\n"
          "the boolean value will be printed as well as the resulting number.\n"
          "Afterwards a plot will be made.\n"
          "Notice the self similarity. Kind of like gaussians of gaussians of ... Zoom in!\n"
          %(N, k, nck(N,k), C2(L,k) ))

    combCL = getCombCoefL(L, k)

    wSum = sum(combCL)

    print( wSum == nck(N,k), wSum )

    print("\nI think that there are rounding errors (depeding in your choice of k), the"
          " numbers could be close but not quite the same...\n")

    print("\nNow check the plot! It uses the naturally generated order of the combinations\n"
          "for the x axis and the weight of the configurations for the y axis.\n")

    plt.plot(combCL)
    plt.xlabel('Combination number')
    plt.ylabel('Weight')
    plt.title('Zoom Zoom!')

    plt.show()
