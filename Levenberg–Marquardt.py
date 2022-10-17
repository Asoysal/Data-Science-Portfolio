from IPython import get_ipython
get_ipython().magic('reset -sf')
import numpy as np
import numdifftools as nd
import math
from numpy import linalg as LA
np.set_printoptions(precision=4)  

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

mu = 1
mumin = 1e-20
mumax = 1e+20
muscal = 10
I = np.identity(2)
x= ([-1.5,-1.5])




#define function
def fmain(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2

#define function with different format for jacobian.
def fmain_jac(x):
    return np.array([(10*x[1]-10*x[0]**2) , (1-x[0])])

Jacobien = nd.Jacobian(fmain_jac)(x)


nu_iteration = 0

E = fmain_jac(x)

F = fmain(x)

# print(np.array([sayac,mu,np.transpose(x),F]))
loop1 = 1
while loop1:

    nu_iteration = nu_iteration + 1
    Jacobien = nd.Jacobian(fmain_jac)(x)
    E = fmain_jac(x)
    loop2 = 1
    while loop2:
        Jacobien_transpozed =np.transpose(Jacobien)
        
       
        zk1 =  -LA.inv(np.matmul(Jacobien_transpozed, Jacobien)  +  mu*I )
        zk2 = np.matmul(Jacobien_transpozed,E) 
        zk = np.matmul(zk1,zk2)
        
        print(zk)
        if fmain(x + zk) < fmain(x):
            p = zk
            s = goldensection(fmain,x,p)
            x = x + np.dot( s,p)
            mu = mu / muscal
            loop2 = 0
            print('.....function does not decrease')
        else:
            mu = mu * muscal
            if mu > mumax:
                loop2 = 0
                print('.....mu reached the max ')
                loop1 = 0
                print('.....mu reached the max')

    F = fmain(x)
    print(nu_iteration,[mu],np.transpose(x),np.transpose(E),F)
    if LA.norm(np.matmul(Jacobien_transpozed,E) ) < 10**-4: 
        loop1 = 0
        print('.....Eigenvalues is positive')


