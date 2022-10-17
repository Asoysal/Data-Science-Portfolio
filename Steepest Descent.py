import numpy as np
import numdifftools as nd
import math
from numpy import linalg as LA


#define initial point
x= ([-2,3.5])



#define function
def fmain(x):
    return 3+(x[0]-1.5*x[1])**2+(x[1]-2)**2

g = nd.Gradient(fmain)(x)

f_r = fmain(x)


def goldensection(fmain,x,p):
        s_min = 0
        s_max = 1
        dx = 10**-4
        to = 0.38197
        eps = dx/(s_max-s_min)
        N = int(np.around((-2.078)*(math.log(eps))))
        N = N+1
        
        s1 = s_min + to * (s_max-s_min)
        f1 = fmain(x+s1*p)
        s2 =  s_max - to * (s_max-s_min)
        f2 = fmain(x+s2*p)
        
        for k in range(N):
            if f2<f1:
                s_min =s1
                s1 = s2
                f1 =f2
                s2 =  s_max - to * (s_max-s_min)
                f2 = fmain(x+s2*p)
            elif f1<f2:
                    s_max = s2
                    s2 = s1
                    f2 = f1
                    s1 = s_min + to * (s_max-s_min)
                    f1 = fmain(x+s1*p)   
        s = (s_min+s_max)/2   
        return s

loop = 1
nu_iteration = 0
while loop:

    nu_iteration = nu_iteration + 1
    Gradient = nd.Gradient(fmain)(x)
    p = - Gradient
    s = goldensection(fmain,x,p)
    dx = s * p
    x = x + dx
    F_r=fmain(x)
    print(s,np.transpose(x),np.transpose(Gradient),F_r)
    if LA.norm(Gradient) < 10**-4:   
        loop = 0


