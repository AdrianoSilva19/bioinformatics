function [f]= nelder_mead(x,w)
u=[x(1)^2+x(2)^2
x(1)^2+x(2)^2+w*(-4*x(1)-x(2)+4)
x(1)^2+x(2)^2+w*(-x(1)-2*x(2)+6)];
f=max(u);
end 
% na function escrever a função dada
% para ver as iterações:  
% options=optimset('Display','iter');
% para correr com o algoritmo neldermead:   
% [xmin,fmin,exitflag,output]=fminsearch('nelder_mead',[1 1 1 1],options)
% xmin é vetor minimizante fmin é o minimo

%% EXERCICIO1
function f=NM1(x)
u=[abs(x(1)),abs(x(2)-1)];
f=max(u);
end


%% EXERCICIO 2
 function f=NM2(x)
u=[x(1)^2+x(2)^4
(2-x(1))^2+(2-x(2))^2
2*exp(-x(1)+x(2))];
f=max(u);
end


%% EXERCICIO 3
function [f]= NM3(x)
n=length(x);
f=n*max(x)-sum(x);
end
%n=5
%i=1:n
% x1(i)=i-((n/2)+0.5)
% op=optimset('TolX',1e-20,'MaxFunEvals',10000,'MaxIter',10000);

%% EXERCICIO 4
function [f]= NM4(x)
f=prod(x)-min(x);
end
%n=2
%i=1:n
%x1(i)=i-((n/2)+0.5)
%op=optimset('MaxFunEvals',5000)

%% EXERCICIO 5

function f=NM5(x,w)
u=[x(1)^2+x(2)^2
x(1)^2+x(2)^2+w*(-4*x(1)-x(2)+4)
x(1)^2+x(2)^2+w*(-x(1)-2*x(2)+6)];
f=max(u);
end
