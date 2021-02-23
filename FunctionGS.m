function [s]=FunctionGS(f,x,p)
Salt=0; % adim araligi alt degeri
Sust=1; % adim araligi ust degeri
DS=0.0001; % 
TAU = 0.38197; % tolerans degeri
EPS = DS/(Sust-Salt); % tolerans degeri
N = round(-2.078*log(EPS)); %iterasyon sayisi

s1 = Salt + TAU*(Sust - Salt); 
f1 = feval(inline(f),x+s1*p);
s2 = Sust - TAU*(Sust - Salt);
f2 = feval(inline(f),x+s2*p);

for k = 1:N
   if f2<f1
      Salt = s1;
      s1 = s2;
      f1 = f2;
      s2 = Sust - TAU*(Sust - Salt);
      f2 = feval(inline(f),x+s2*p);
   elseif f1<f2
       Sust = s2;
       s2 = s1;
       f2 = f1;
       s1 = Salt + TAU*(Sust - Salt);
       f1 = feval(inline(f),x+s1*p);
   end
end

s = (Salt+Sust)/2;
