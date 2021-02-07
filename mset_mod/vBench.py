import time

import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *



if __name__ == '__main__':


    for i in range(20):
        L=getRandomMultList(8, 8)
        k=random.randint(0, sum(L))

        t0=time.time()
        v0=V0(L,k)
        t1=time.time()
        v0T=t1-t0

        t2=time.time()
        v1=V1(L,k)
        t3=time.time()
        v1T=t3-t2

        compBool=True
        for vp0, vp1 in zip(v0,v1):
            if not (vp0 == vp1).all():
                compBool =False
                break
        
        cBool = len(v0) == len(v1)

        print(compBool, cBool, len(v1), v0T, v1T, v0T >= v1T)
