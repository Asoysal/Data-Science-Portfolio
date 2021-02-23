clear all
close all
clc

x = [-4.5;-3.5];
f = '3+(x(1)-1.5*x(2))^2+(x(2)-2)^2';
g = '[2*(x(1)-1.5*x(2)); -3*(x(1)-1.5*x(2))+2*(x(2)-2)]';
Gradient = feval(inline(g),x);
F = feval(inline(f),x);
disp([x',Gradient',F])

kosul = 1; sayac=0;
while kosul   
if sayac==0
Gradient = feval(inline(g),x);
p = -Gradient; 
Gradienteski = feval(inline(g),x);
    peski= p;
else
    
    Gradient = feval(inline(g),x);
    beta = (Gradient'*Gradient) / (Gradienteski'*Gradienteski);
    p = -Gradient + beta*peski;
end
sayac=sayac+1;
[s]=FunctionGS(f,x,p);
dx = s*p;
x = x + dx;

F = feval(inline(f),x);
disp([s,x',Gradient',F])
if norm(Gradient)<1e-4; kosul=0; end
end
sayac