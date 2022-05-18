%% 


fo=-[]; %isto é a função objetivo (- quando é maximização)
A=[]; % matriz das restrições de desigualdade

B= []; % vetor das restrições de desigualdade, mesmos numero de colunas que linhas da A

Aeq=[]; % matriz das restrições de igualdade (Aeq=Beq)
Beq=[]; % vetor de restrições de igualdade
lb=zeros(1,X); % limite minimo (se não pode haver numeros negativos mantes, colocar  no segundo o mesmo que as colunas A
ub=[]; % limite superior (limite superiror das variaveis)
[xmin,fmin,exitflag,output]=linprog(fo,A,B,Aeq,Beq,lb,ub) % xmin da as variaveis, fmin da custo ou lucro


%%
% FICHA DE LINPROG
%EXERCICIO 1

% fo= 260x1 + 390x2
% restrições x1+3x2<=660
% limite superior x1<=450 limute inf=<325

fo=-[260 390]; %isto é a função objetivo 
A=[1 3]; % matriz das restrições de desigualdade

B= [660]; % vetor das restrições de desigualdade, mesmos numero de colunas que linhas da A

Aeq=[]; % matriz das restrições de igualdade (Aeq=Beq)
Beq=[]; % vetor de restrições de igualdade
lb=zeros(1,2); % limite minimo (se não pode haver numeros negativos mantes, colocar  no segundo o mesmo que as colunas A
ub=[450 325]; % limite superior (limite superiror das variaveis)
[xmin,fmin,exitflag,output]=linprog(fo,A,B,Aeq,Beq,lb,ub)

% produto maximo de vendas é fmin
%% 
%EXERCICIO 2

% fo=2x1 +1.5x2
% restrições 0.5x1 +1.7x2 <=9
%            6x1+1x2<=45
%            x1 + x2 <=10
% maximizar os ganhos


fo=-[2 1.5]; %isto é a função objetivo (- quando é maximização)
A=[0.5 1.7
    6 1
    1 1]; % matriz das restrições de desigualdade

B= [9 45 10]; % vetor das restrições de desigualdade, mesmos numero de colunas que linhas da A

Aeq=[]; % matriz das restrições de igualdade (Aeq=Beq)
Beq=[]; % vetor de restrições de igualdade
lb=zeros(1,2); % limite minimo (se não pode haver numeros negativos mantes, colocar  no segundo o mesmo que as colunas A
ub=[]; % limite superior (limite superiror das variaveis)
[xmin,fmin,exitflag,output]=linprog(fo,A,B,Aeq,Beq,lb,ub) % xmin da as variaveis, fmin da custo ou lucro

%% 
% EXERCICIO 3

% fo= 7A 12B 5C 10D
% restrições 
% rosas= 3A + 5B + 4C + 4D <= 600
% tulipas= 6B 8C <= 400
% cravos= 2A + 2B + 2C +2D <= 500
% margaridas= 4A + 4B + 6D <= 400
% MAXIMIZAR LUCRO


fo=-[7 12 5 10]; %isto é a função objetivo (- quando é maximização)
A=[3 5 4 4
   6 0 8 0
   2 2 2 2
   4 4 0 6]; % matriz das restrições de desigualdade

B= [600 400 500 400]; % vetor das restrições de desigualdade, mesmos numero de colunas que linhas da A

Aeq=[]; % matriz das restrições de igualdade (Aeq=Beq)
Beq=[]; % vetor de restrições de igualdade
lb=zeros(1,4); % limite minimo (se não pode haver numeros negativos mantes, colocar  no segundo o mesmo que as colunas A
ub=[]; % limite superior (limite superiror das variaveis)
[xmin,fmin,exitflag,output]=linprog(fo,A,B,Aeq,Beq,lb,ub) % xmin da as variaveis, fmin da custo ou lucro

%%
% EXERCICIO 4

% fo= 0.6a o.8b 1c 0.3d 0.5e 0.9f 0.4g 0.6h
% restrições
% tudo junto tem de dar pelo menos 200 a + b + c + d + e + f + g + h >= 200
% açucar = 0.3c 0.8d 0.05e = 0.2*200
% leite = 0.2c 0.7e 0.75f = 0.1*200
% agua = 0.2a +0.3b + 0.15c + 0.15d + 0.15e + 0.10f + 0.10g + 0.10h = 0.15*200
% gordura = 0.8a + 0.7b + 0.35c + 0.05d + 0.10e 0.15f 0.30g 0.15h >=0.2*200
% ovos 0.6g 0.75h >= 0.25*200

fo=[0.6 0.8 1 0.3 0.5 0.9 0.4 0.6]; %isto é a função objetivo (- quando é maximização)
A=-[1 1 1 1 1 1 1 1
    0.8 0.7 0.35 0.05 0.10 0.15 0.30 0.15
    0 0 0 0 0 0 0.6 0.75]; % matriz das restrições de desigualdade

B=-[200 0.2*200 0.25*200]; % vetor das restrições de desigualdade, mesmos numero de colunas que linhas da A

Aeq=[0 0 0.3 0.8 0.05 0 0 0
    0 0 0.2 0 0.7 0.75 0 0
    0.2 0.3 0.15 0.15 0.15 0.10 0.10 0.10]; % matriz das restrições de igualdade (Aeq=Beq)
Beq=[0.2*200 0.1*200 0.15*200]; % vetor de restrições de igualdade
lb=zeros(1,8); % limite minimo (se não pode haver numeros negativos mantes, colocar  no segundo o mesmo que as colunas A
ub=[]; % limite superior (limite superiror das variaveis)
[xmin,fmin,exitflag,output]=linprog(fo,A,B,Aeq,Beq,lb,ub) % xmin da as variaveis, fmin da custo ou lucro

