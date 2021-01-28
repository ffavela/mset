from mset_lib.core import *

print("Hello world!")

# # M=[getSet('a',3), getSet('b',2), getSet('c',1)]
# # M=[getSet('x',6)]
# # S=[e for sublist in M for e in sublist]
# # print(S)
# # newLL=G(S,3)
# # print("\nBegin newLL\n")
# # print(newLL)
# # print("\nEnd newLL\n")
# # lOfStr=getLOfStr(newLL)
# # print(lOfStr)
# # print(len(lOfStr))
# # print(", ".join(lOfStr))


# # S=100*['a']+50*['b']+15*['c']
# # S=['a0','a1','a2','b0','b1','c0','c1','d0','e0']
# S=['a0','a1','a2','b0','b1','c0']
# print(G(S,4))
# print(len(G(S,4)))

# print(zG(S,4))
# print(len(zG(S,4)))



# # print("\nNow doing the new version\n")
# # print(nG(S,4))
# # print(len(nG(S,4)))


# # print("\nThe newer version\n")
# # print(NG(S,4))
# # print(len(NG(S,4)))

# M=[24*['a'],16*['b'],2*['c']]
# # M=[['a0','a1','a2'],['b0','b1'],['c0']]
# # M=[['a','a','a'],['b','b'],['c']]ç
# # M=[10*['r'],7*['v'],3*['n'],1*['a']]
# print("\n Now testing the multiset version\n")
# # val=5
# L=[len(m) for m in M]
# N=sum(L)

# for val in range(N):
#     # print(mG(M,val))
#     print("Val is ", val)
#     print(len(mG(M,val)))
    
#     # print("\n Now testing the newer multiset version\n")
#     # print(MG(M,val))
#     print(len(MG(M,val)))


#     print(C(L,val))

# # print("Doing the memoized version")
# # print(memoG(S,4))
# # print(len(memoG(S,4)))

# #for i in range(len(S)):
# #    print(G(S,i))
