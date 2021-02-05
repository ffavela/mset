import time

import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *

rL=3000
if sys.getrecursionlimit() <= rL:
    print("Current recursion limit is = ", sys.getrecursionlimit())
    print("Incrementing the recursion limit to "+str(rL)+" just in case")
    sys.setrecursionlimit(rL)


if __name__ == '__main__':

    print("Count\tExecution time[s]")
    for i in range(20):
        L=getRandomMultList(100, 50)
        k=random.randint(0, sum(L)+1)

        t0=time.time()
        c2=C2(L,k)
        t1=time.time()

        c2T=t1-t0



        print(c2, c2T)
