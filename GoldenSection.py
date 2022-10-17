from __future__ import division
import math

xalt = 0
xust = 4
dx = 10**-4
to = 0.38197
eps = dx/(xust-xalt)

N = (-2.078)*(math.log10(eps))

print (N)

k = 0
x1 = xalt + to * (xust-xalt)
f1 = (x1 - 1) ** 2 * (x1 - 2) * (x1 - 3)
x2 =  xust - to * (xust-xalt)
f2 = (x2 - 1) ** 2 * (x2 - 2) * (x2 - 3)
#N = round(N) + 1
print (k,xalt,xust,f1,f2,N)
k = k + 1

#def gsfunction(x):
#    sayi=(x-1)**2*(x-2)*(x-3)
N = int(N)
loop = 1

while loop == 1:
    k = k + 1
    if f1<f2:
          xalt =x1
          x1 = x2
          f1 =f2
          x2 = xust - to * (xust-xalt)
          f2 = (x2 - 1) ** 2 * (x2 - 2) * (x2 - 3)
    elif f2>f1:
          xust = x2
          x2 = x1
          f2 = f1
          x1 = xalt + to * (xust-xalt)
          f1 = (x1 - 1) ** 2 * (x1 - 2) * (x1 - 3)
          if k == N:
             loop = 0


print (k,xalt,xust,f1,f2)
x = (xalt+xust)/2








