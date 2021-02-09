import time

import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *



if __name__ == '__main__':

    print("cBool   c2\t    c0T\t         c1T\t\t\t c2T")
    for i in range(20):
        L=getRandomMultList(20, 20)
        k=random.randint(1, 8)

        t0=time.time()
        c0=C0(L,k)
        t1=time.time()
        c0T=t1-t0

        t2=time.time()
        c1=C1(L,k)
        t3=time.time()
        c1T=t3-t2

        t4=time.time()
        c2=C2(L,k)
        t5=time.time()

        c2T=t5-t4

        cBool= c0 == c1 == c2


        print(cBool, c2, c0T, c1T, c2T)
