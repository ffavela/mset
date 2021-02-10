import time

import random
import matplotlib.pyplot as plt

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *

if __name__ == "__main__":
    print("Given a poker deck we know that there are 52 different cards.\n"
          "This this means that there are nck(52,5) = %d different possible hands.\n\n"
          "We know that a deck has 4 suits with 13 different cards each suit.\n"
          "If we were to ignore the suit, then there are 13 different sets\n"
          "with 4 elements each as the following multiplicity list:\n\n"%(nck(52, 5)))

    L = 13*[4]
    print("  L = ", L)

    print()

    print("This is in essence a partitioning scheme for the card deck.\n"
          "We are deliberately saying that each of those 4 item elements\n"
          "is indistinguishable from the others in the same group\n"
          "but distinguishable between the different groups.\n")

    print("In this case, the number of different hands will be less.\n"
          "Note that the stars and bars (multicombination) approach will not work since\n"
          "the maximum size of each group is 4, that approach will overcount...\n\n")

    print("However using mset we can calculate this easily and it gives C(L, 5) = %d\n" %(C2(L, 5)))

    print("Note that the calculation is for possible different hands, it counts possibilities.\n"
          "Now if we were to sum the combinatorial weight of each possibility then if should\n"
          "sum to nck(52, 5) = %d. We will not print the generated output\n"
          "(it would flood the terminal) but we will create the weight list plot it and calculate the sum.\n" %(nck(52, 5)))

    weightL = getCombCoefL(L, 5)

    weightS = sum(weightL)
    
    print("So indeed the weightL has %d elements (as calculated by C(L, 5))\n"
          "and the sum is %d which is the same as calculated by nck(52, 5).\n"
          %(len(weightL), weightS))

    print()

    print("Note that the plot has the combination number as the x axis,\n"
          "this is and index corresponding to the \"natural\" way the \n"
          "combination elements were generated, the y axis is the\n"
          "combinatorial weight for these possibilities, notice the\n"
          "visual self similarity (zoom in).")

    plt.plot(weightL)
    plt.xlabel('Combination number')
    plt.ylabel('Weight')
    plt.title('Poker plot!')

    plt.show()
    
