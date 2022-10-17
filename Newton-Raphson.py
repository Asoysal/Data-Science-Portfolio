from __future__ import division # it is for decimal number
x = 3
f = (x-1)**2*(x-2)*(x-3)
loop = 1

while loop == 1:
    f1 = 2*(x-1)*(x-2)*(x-3)+(x-1)**2*(2*x-5)
    f2 = 2*(x-2)*(x-3)+2*(x-1)*(2*x-5)+2*(x-1)*(2*x-5)+2*(x-1)**2
    print (x,f1,f2)  
    dx = -f1/f2
    x = x + dx
    f = (x-1)**2*(x-2)*(x-3)
    f1 = 2*(x-1)*(x-2)*(x-3)+(x-1)**2*(2*x-5)
    if abs(f1)<10**-6 :
        loop = 0
print (x,f1,f2)







