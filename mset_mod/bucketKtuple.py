import time
import random

import sys
sys.path.append('../')
from mset_lib.core import *
from mset_lib.miscellaneous import *



if __name__ == '__main__':

    str1="""\nSuppose that we have 4 buckets with
corresponding ball capacities of 4,3,2,1. 
This means that the maximum number of balls they
can store is 10. How many ways are there to store k
balls in the 4 buckets?\n"""

    str2="""Ok, so the limited capacity is a problem
however, we can easely overcome it by noting that 
the capacities can be seen as a multiplitity list:
\n\tL=[4, 3, 2, 1]\n"""

    L = [4,3,2,1]
    
    str3="""Using the optimized multiset
combination function C2, we can calulate this for
0 <= k < 10.\n"""
    
    print(str1)

    print(str2)

    print(str3)

    print("k\tC(L,k)")
    for k in range(sum(L)+1):
        print("%d\t%d" %(k, C2(L, k)))

    print()

    str4="""Notice the symmetry of C with respect to
k, C(L,k) == C(L,N-k) where N=10 in our case. Note
that the problem can be more generally expressed in
terms of L, expressing the maximum capacity as N=sum(L)
and the number of buckets as n=len(L).\n"""

    print(str4)

    str5="""Now, notice that sum_k=0^10 C(L,k) = """

    s = sum([C2(L, k ) for k in range(10+1)])
    
    print(str5+str(s)+" = (4+1)!\n")
    

    str6="""In fact, for any given multiset
\nsum_k=0^N C(L,k) = (m_0+1)(m_1+1)*···*(m_(n-1)+1)\n
where the m_j are the multiplicities.
"""

    print(str6)

    str7="""Now how about generating
 the configurations? In this case we use the V0
function. Lets say that we want to place k=2 balls."""

    C=V0(L,2)

    print("The configurations are:\n")

    print("j   conf    sum")
    for j,c in enumerate(C):
        print(j, c, sum(c))

    print()

    print("That simply listed the C(L,2)="
          +str(C2(L,2))+" possibilities.\n"+\
          "Notice that the sum of conf, for any\n"+\
          "configuration, always gives 2.\n")

    print("Each possibility has a combinatorial\n"
"weight given as the following table:\n")


    WE=getCombCoefL(L,2)

    print("j    conf   we")
    for j, c, we in zip(range(len(C)), C, WE):
        print(j, c, we)

    print("\nWhere the \"we\" variable stands for the combinatorial weight.\n")

    str8="""Note that as expected:\n\n nck(10,2)="""\
    +str(nck(10,2))+"""\n
 sum_j=0^C(L,2) we_j = """+str(sum(WE))

    print(str8)

    print("\nThis means that we can easely normalize.\n")
