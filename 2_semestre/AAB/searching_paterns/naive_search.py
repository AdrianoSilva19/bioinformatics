# -*- coding: utf-8 -*-

from errno import EDESTADDRREQ


def naive_serach(pattern,sequence):
    res=[]
    for i in range(len(sequence)-len(pattern)+1):  #o -len(pattern) é para não procurar até ao fim da seq mas podesse retirar
        equal=0
        while equal<(len(pattern)) and pattern[equal]==sequence[i+equal]:
            equal+=1
        if equal==len(pattern):
            res.append(i)
    return res

x=naive_serach('ACTG','AATACTGCTACT')
print(f'patterns occurs in positions :{str(x)}')