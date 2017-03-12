import matplotlib.pyplot as plt
import numpy as np
# Simulating the exact solution to the truncated random walk (brownian.py)
global l
l = [0.5]

N = 500


def getL(x):
    if x >= len(l): return 0
    elif x<0: return 0
    else: return l[x]

for i in range(1, N+1):
    newl = []
    ans = 0
    ans2 = 0
    if i%2 == 0: # EVEN
        newl.append(2*getL(0)+getL(1))
        ans += 2*getL(0)+getL(1)
        ans2 += 2*getL(0)+getL(1)
        for j in range(1, i//2):
            v = getL(j) + getL(j+1)
            newl.append(v)
            ans += v * (j*2+1)
            ans2 += v * ((j*2+1) ** 2)
    else:  # ODD
        for j in range(1+i//2):
            v = getL(j-1)+getL(j)
            newl.append(getL(j-1)+getL(j))
            ans += v * j * 2
            ans2 += v * ((j * 2)**2)
    l = newl
    xbar = (ans/(2.**(i-1)))
    x2bar = (ans2/(2.**(i-1)))
    print x2bar-xbar**2
