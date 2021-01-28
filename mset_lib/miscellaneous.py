from math import factorial
import operator as op
from functools import reduce

def ncr(r,n):
    #Important condition
    if r > n or n < 0:
        return 0
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def myComb(k,N):
    if k > N or N < 0:
        return 0
    return int(factorial(N)/(factorial(k)*factorial(N-k)))
