import time

import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *

if __name__ == "__main__":
    print("We know that in a poker deck are 52 different cards.\n"
          "This this means that there are nck(52,5) = %d different possible hands.\n\n"
          %(nck(52, 5)))

    strL= "52*[1]"
    print("Let's say that they are all indistinguishable, that means that the corresponding multiplicity list is:\n\n"
          " in a compact form L= %s \n" %(strL))

    L = eval(strL)

    print("Or in an expanded form L = ", L)
    
    print("In this case, doing the mset calculation and doing the nck(52,5)\n"
          "are exactly the same; C2(L, 5) = %d\n\n" %(C2(L, 5)))

    print("There is no apparent advantaje in using mset for this case\n"
          "(it is even slower) however we can profit from the current form\n"
          "since we can consider cases where we add adittional\n"
          "identical card decks and ask how many possible 5 card hands\n"
          "can be handed for a given amount of card decks.\n")

    print("#deck\tL\tC2(L,5)")
    for i in range(1,7):
        strL= "52*["+str(i)+"]"
        L=eval(strL)
        print("%d\t%s\t%d" %(i, strL, C2(L,5)))

    print("\nThe first value is exactly what was expected, the fifth too\n"
          "it can be easely calculated using the stars and bars approach\n"
          "notice that the sixth gives exactly the same result, this happens\n"
          "for higher values also, the problem is approached through\n"
          "from the combinations with repetition of sets. Using 2, 3 or 4 decks\n"
          "eventhough the numbers are smaller than with 5 there is no\n"
          "clear way of doing the calculation without:\n\n"
          "1) enumerating all possibilities\n"
          "2) using mset\n")

    print("These calculations are assuming you are the first one be be dealt\n"
          "the cards!!\n")
    
    print("Also, different poker hands will have different absolute frequencies\n"
          "(or combinatorial weights), in order to calculate this L has to\n"
          "be repartitioned to accomodate what is considered indistinguishable\n"
          "for the respective hands.\n")
