import time

import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *


if __name__ == '__main__':

    L=[3,2,5, 10, 20, 50] #Remember this will be sorted
    print("The list is L = ", L)

    print()
    print("cBool  C2  C3    c2T            c3T          c2T>=c3T")
    for k in range(sum(L)+1):
        t0=time.time()
        c2=C2(L,k)
        t1=time.time()
        c2T=t1-t0

        t2=time.time()
        c3=C3(L,k)
        t3=time.time()
        c3T=t3-t2

        cBool= c2 == c3


        print(cBool, c2, c3,  c2T, c3T, c2T >= c3T)
