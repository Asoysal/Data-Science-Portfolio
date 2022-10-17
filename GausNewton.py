from IPython import get_ipython
get_ipython().magic('reset -sf')
import numpy as np
import numdifftools as nd
import math
from numpy import linalg as LA




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

x= ([-1.5,-1.5])



#define function
def fmain(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2


Gradient = nd.Gradient(fmain)(x)

Hessian = nd.Hessian(fmain)(x)

#define function with different format for jacobian.
def fmain_jac(x):
    return np.array([(10*x[1]-10*x[0]**2) , (1-x[0])])

Jacobien = nd.Jacobian(fmain_jac)(x)

E = fmain_jac(x)

F = fmain(x)


# print(np.array([np.transpose(x),np.transpose(Gradient),F]))

loop = 1
nu_iteration = 0
while loop:

    nu_iteration = nu_iteration + 1
    
   
    Jacobien = nd.Jacobian(fmain_jac)(x)
    
   
    E = fmain_jac(x)
    Jacobien_transpozed =np.transpose(Jacobien)
    Gradient = 2 * np.matmul(Jacobien_transpozed,E)
    Hessian = 2 * np.matmul(Jacobien_transpozed,Jacobien)
    
 
    
    if np.amin(	LA.eig(Hessian)[0]) > 0:
        p = - np.matmul(LA.inv(Hessian),Gradient)
    else:
        mu = np.abs(np.amin(	LA.eig(Hessian)[0])) + 1e-05
        p = - np.matmul(LA.inv(Hessian + mu * np.identity(2)),Gradient)
    s = goldensection(fmain,x,p)
    dx = s * p
    x = x + dx
    F_r=fmain(x)
    print(s,np.transpose(x),np.transpose(Gradient),F_r)
    if  LA.norm(Gradient) < 10**-4:   
        loop = 0


