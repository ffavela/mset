import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *

if __name__ == '__main__':
    for i in range(10):
        L=getRandomMultList(5, 5)
        print("L=", L)
        N=sum(L)
        coefL=[C1(L,k) for k in range(N+1)]
        print("coefL = ", coefL)
        print(isSymmetric(coefL))
        print()
            
