import time

import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *

if __name__ == "__main__":
    print("We know that in a poker deck are 52 different cards.\n"
          "If we add the \"standard\" 2 jokers then there will be\n"
          "54 cards 2 of which are completely identical.\n"
          "the number of possible different hands (H) lies between\n\n"
          "  %d = nck(52,5) < H < nck(54,5) = %d \n\n"
          %(nck(52, 5), nck(54, 5)))

    print("That expression spans %d different potential values for H.\n"
          "While it does constrain it performs very poorly.\n"
          %(nck(54, 5) - nck(52, 5)))

    strL="[2]+52*[1]"
    L=eval(strL)
    print("A better way is to use mset by first constructing the\n"
          "multiplicity list L = %s, and then calling the combination function:\n\n"
          " C2(L, 5) = H = %d\n\n"
          "Giving the desired value exactly!\n"
          %(strL, C2(L,5)))
