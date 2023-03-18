# coding: utf-8
from math import log

def getStringInNewBase(number, base):
    v='0123456789abcdefghijklmnopqrstuvwxyz'
    if not 1<base<len(v):
        print("error: out of scope")
        return None
    #getting the maximum power in new base
    n=0
    if number != 0:
        n=int(log(number,base))#round down to nearest int
    def g(number,n,s=''):
        if n==0:
            return s+v[number]
        return g(number%base**n,n-1,s+v[number//base**n])
    return g(number,n)
    
