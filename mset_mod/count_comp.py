import time

import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *

if __name__ == '__main__':
    for i in range(10):
        L=getRandomMultList(200, 200)
        print(L)
        k=4
        t0=time.time()
        c0=C0(L,k)
        t1=time.time()

        t2=time.time()
        c1=C1(L,k)
        t3=time.time()

        print(c0==c1, c0, c1, t1-t0, t3-t2,
              t1-t0 >= t3-t2 )
