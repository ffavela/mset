from functions import *
from random import shuffle

N=6
k=3

for i in getILL(N,k):
    print(getIFromB(getBFromIL(i)), getBFromU(N,k, getUFromB(N,k,getBFromIL(i))),getUFromB(N,k,getBFromIL(i)),i, getBFromIL(i))

p=['cocacola', 'ruffles', 'panditas', 'donas', 'leche']

recibo=['cocacola', 'ruffles', 'donas', 'leche']

print("Productos comprados =")
print( recibo)

N=len(p)
k=len(recibo)

I=[p.index(e) for e in recibo]

print(I)

B=getBFromIL(I)
print(B)

u=getUFromB(N,k,B)
print(u)

print("Sending N,k,u =",N,k,u)

B=getBFromU(N,k,u)

print(B)

I=getIFromB(B)

print(I)

reciboRemoto=[p[i] for i in I]

print(reciboRemoto)

print("##################Permutation stuff###################")

L=[3,4,6,2,56]

print(L)

print(getListWithoutIndex(2,L))

v=666

LL=[[1,2,3], [6,5,4], [1,9,5]]

print(LL)

print(w(v,LL))

print("##############Permuted last######")

# L=['ruffles', 'gansito', 'panditas']
# L=['ruffles', 'gansito']
L=[0,1,2,3]
print("L=",L)

pL=getPermutedLists(L)
print(pL)

print(len(pL))

for i,e in enumerate(pL):
    print(i,e)

print()
print("#####Number to perm list and viceversa#########")
print()

L=[0,1,2,3]

pLFu=getPermutationListFromU(4,17)
print(pLFu)
print("########Getting the permutaion list from u######")
for i in range(24):
    p=getPermutationListFromU(4,i)
    print(i,p,getUFromPermutationList(p))

print("######Ending the loop here#########")
print("Now the number from a particular permutation")

p=[3, 0, 2, 1]
#p=[1, 0, 2, 3]
#p=[0, 2, 3, 1]
print("p =", p)
u=getUFromPermutationList(p)
print("u =", u)

L=[21, 6, 18, 1, 23, 4, 7, 22, 16, 0, 12, 13, 10, 19, 17, 20, 2, 14, 9, 11, 3, 8, 15, 5]
print(L)
u=getUFromPermutationList(L)
print(u, len(str(u)))
p=getPermutationListFromU(len(L),u)
print(p)

print()
print("#############Shuffling fun##########")
print()

L=list(range(52))
print(L)
shuffle(L)
print(L)
u=getUFromPermutationList(L)
print(u, len(str(u)))
p=getPermutationListFromU(len(L),u)
print(p)

print("Checking next")
pp=getPermutationListFromU(len(L),u+21)
print(u+ 21, len(str(u+21)))
print(pp)
