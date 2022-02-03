# -*- coding: utf-8 -*-

import re
from math import log
from threading import local
from typing import List, Type
from unittest import result

'''
SeqManPy é um package multifuncional de manipulacao de sequencias biologicas. E um package multifacetado
que realiza desde manipulacoes simples de sequencias como, por exemplo, converter uma sequencia de DNA em RNA ate 
operacoes mais complexas como alinhamentos globais (Needleman-Wunsch) e alinhamentos locais (Smith-Waterman) ou 
alinhamentos progressivos de sequencias com consensos.

Author's: Adriano Silva PG43176, Rui Gomes PG45970, Sérgio Mendes PG42486, Tiago Oliveira PG45476
'''

def validacao_dna(seq: str) -> str:
    ''' 
    Recebe uma sequencia e valida-a como sendo de DNA (True) ou nao (False)
    
    Inputs:
        :seq: Sequencia para validação
        :type seq: string

    Returns:
        :return boolean: Validação da sequência
        :rtype boolean: boolean
    '''

    if type(seq) not in [str]:
        raise TypeError ('A sequência tem de ser uma string.')
        
    seq = seq.upper()
    seqcnt = 0
    for n in seq:
        if n in 'ACGT':
            seqcnt += 1
            if len(seq) == seqcnt:
                return True
        else:
            return False

def dna_rna (seq: str) -> str:
    '''
    Converte uma sequencia de DNA numa sequencia de RNA
    
    Inputs:
        :seq: Sequência para conversão
        :type seq: string

    Returns:
        :return rna: Sequência de RNA 
        :rtype rna: string
    '''

    if type(seq) not in [str]:
        raise TypeError ('Deve inserir uma string')

    seq = seq.upper()
    cnt = 0
    for n in seq:
        if n in 'ATGC':
            rna = seq.replace('T', 'U')
            cnt += 1
            if len(seq) == cnt:
                return rna
        else:
            raise TypeError ('Deve inserir uma sequência de DNA')
            break

def rna_dna(seq: str) -> str:
    '''
    Converte uma sequencia de RNA numa sequencia de DNA
    
    Inputs:
        :seq: Sequência para conversão
        :type seq: string

    Returns:
        :return dna: Sequência de DNA 
        :rtype dna: string
    '''

    if type(seq) not in [str]:
        raise TypeError ('Deve inserir uma string')
    seq = seq.upper()
    rnacnt = 0
    for n in seq:
        if n in 'AUGC':
            dna = seq.replace('U', 'T')
            rnacnt += 1
            if len(seq) == rnacnt:
                return dna
        else:
            raise TypeError ('Deve inserir uma sequência de DNA')
            break

def complemento_inverso(seq: str) -> str:
    '''
    Converte uma sequencia de DNA no seu complemento inverso (3' - 5')
    
    Inputs:
        :seq: Sequência para conversão
        :type seq: string

    Returns:
        :return complemento inverso: Sequência correpondente ao complemento inverso
        :rtype complemento inverso: string
    '''

    if type(seq) not in [str]:
        raise TypeError ('O seu input deve ser uma sequência')

    seq = seq.upper()
    inverse = ''
    for n in seq:
        if n in 'ATGC':
            if n == 'A':
                inverse += 'T'
            elif n == 'T':
                inverse += 'A'
            elif n == 'G':
                inverse += 'C'
            elif n == 'C':
                inverse += 'G'
        else:
            return False
            break

    if len(seq) == len(inverse):
        inverse = inverse[::-1]
        return inverse

def dna_rna_amino_erro(seq: str) -> str:
    '''
    Recebendo uma sequencia o programa procura validar a mesma como sendo DNA, RNA, Aminoacidos ou um erro (nenhum dos anteriores)

    Inputs:
        :seq: Sequência para validação
        :type seq: string

    Returns:
        :return: Validação DNA, RNA, Aminoacidos ou Erro
        :rtype return: string
    '''

    dna = 'ACGT'
    rna = 'ACGU'
    amino = 'ACDEFGHIKLMNPQRSTVWY'
    dnact = 0
    rnact = 0
    aminoct = 0
    myc = 0

    
    if type(seq) not in [str]:
        raise TypeError ('O seu input deve ser uma string')
        

    seq = seq.upper()
    #verificar se é uma sequência de DNA
    for n in seq:
        if n in dna:
            dnact +=1
            if len(seq) == dnact:
                return 'DNA' 
                myc = 1
        else:
            break
    
    #verificar se é uma sequência de RNA
    for n in seq:
        if n in rna:
            rnact += 1
            if len(seq) == rnact:
                return 'RNA'
                myc = 1
        else:
            break
    
    #verificar se é uma sequência de aminoácidos
    if myc != 1:
        for n in seq:
            if n in amino:
                aminoct += 1
                if len(seq) == aminoct:
                    return'Aminoácidos'
            else:
                return 'Erro'
                break

def get_codons(DNA_seq: str) -> List[str]:
    '''
    Recebe uma sequencia de DNA e devolve uma lista dos seus codoes
    
    Inputs:
        :DNA_seq: Sequência de DNA
        :type seq: string

    Returns:
        :return: Lista de codões da sequência de DNA
        :rtype return: List[str]
    '''
    
    if type(DNA_seq) not in [str]:
        raise TypeError ('A sua sequencia não é uma sequencia de DNA')
    
    for n in DNA_seq:
        n = n.upper()
        if n not in 'ACTG':
            raise TypeError ('A sua sequencia não é uma sequencia DNA')

    DNA_seq = DNA_seq.upper()
    DNA_cod = re.findall('...', DNA_seq)
    return DNA_cod

def codon_to_amino(RNA_seq: str) -> str:
    '''
    Recebe uma sequencia de RNA e devolve a sequencia de aminoacidos: \n
    M - codao de iniciacao; _ - codao STOP

    Inputs:
        :RNA_seq: Sequência de RNA
        :type seq: string

    Returns:
        :aminoacidos: Sequência de aminoácidos
        :rtype aminoacidos: string    
    '''

    if type(RNA_seq) not in [str]:
        raise TypeError ('O seu input deve ser uma string')

    for n in RNA_seq:
        n = n.upper()
        if n not in 'ACUG':
            raise TypeError ('A sua sequencia não é uma sequencia RNA')

    rna = RNA_seq.upper()
    rna_codons = { # 'M' - START, '_' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "UGU": "C", "UGC": "C", "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E", "UUU": "F", "UUC": "F", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H", "AUA": "I", "AUU": "I", "AUC": "I", "AAA": "K", "AAG": "K", "UUA": "L", 
    "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "AUG": "M", "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", 
    "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", 
    "AGU": "S", "AGC": "S", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "GUU": "V", "GUC": "V", 
    "GUA": "V", "GUG": "V", "UGG": "W", "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*", "UGA": "*"}
    
    aminoacid = ""
    
    for i in range (0, len(rna), 3):
        codons = rna[i:i+3]
        aminoacid += rna_codons[codons]
    return aminoacid

def get_prots(DNA_seq: str) -> str:
    ''' 
    Recebe uma sequencia de DNA e devolve uma lista com as possiveis proteinas dessa sequencia
    
    Inputs:
        :DNA_seq: Sequência de DNA
        :type seq: string

    Returns:
        :return proteinas: Lista de proteínas possiveis para a sequência
        :rtype proteinas: List[str]
    '''
    if type(DNA_seq) not in [str]:
        raise TypeError ('O seu input deve ser uma string')

    for n in DNA_seq:
        n = n.upper()
        if n not in 'ACTG':
            raise TypeError ('A sua sequencia não é uma sequencia DNA')

    DNA_seq = DNA_seq.upper()

    gencode = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}


    def codoes(DNA_seq):
        DNA_cod = re.findall('...', DNA_seq)
        return DNA_cod


    def traducao(DNA_seq):
        cod = codoes(DNA_seq)
        amino = []
        for i in cod:
            amino += gencode[i]
        prot_seq = ''.join(map(str, amino)) # Convert list to string
        return prot_seq


    def complemento_inverso(DNA_seq):
        DNA_seq_inv = DNA_seq[:: -1]
        DNA_seq_inv = DNA_seq_inv.upper().replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
        DNA_seq_inv = DNA_seq_inv.upper()
        return DNA_seq_inv

    # as 6 orfs
    def reading_frames(DNA_seq):
        DNA_seq1 = DNA_seq[1:]
        DNA_seq2 = DNA_seq[2:]
        DNA_seq_inv = complemento_inverso(DNA_seq)
        DNA_seq_inv1 = DNA_seq_inv[1:]
        DNA_seq_inv2 = DNA_seq_inv[2:]
        prot_seq = traducao(DNA_seq)
        prot_seq1 = traducao(DNA_seq1)
        prot_seq2 = traducao(DNA_seq2)
        prot_seq_inv = traducao(DNA_seq_inv)
        prot_seq_inv1 = traducao(DNA_seq_inv1)
        prot_seq_inv2 = traducao(DNA_seq_inv2)
        protein = [prot_seq, prot_seq1, prot_seq2, prot_seq_inv, prot_seq_inv1, prot_seq_inv2]
        return protein

    def get_proteins(DNA_seq):
        protein = reading_frames(DNA_seq)
        true_protein = []
        for x in protein:
            true_protein += re.findall('M.*?_', x) #Expressão regular para permitir encontrar proteínas válidas
        #unique_protein = set(true_protein) #Eliminar proteínas duplicadas
        #unique_protein = sorted(unique_protein, key=len, reverse=True) #Ordenar por ordem decrescente de tamanho
        #for ele in unique_protein:
            #print(ele) #Imprimir por ordem decrescente de tamanhos e, para proteínas do mesmo tamanho, por ordem alfabética
        return true_protein
    
    return get_proteins(DNA_seq)

def dotplot(seq1: str, seq2: str, win_size: int = 1, stringency: int = 1, printing: bool = False):
    '''
    Recebe duas sequencias, window size e stringency e representa as duas sequencias numa matriz de pontos \n
        default stringency = 1 \n
        default win_size = -1  

    Inputs:
        :seq1: Sequência 1 para alinhar
        :type seq1: string
        :seq2: Sequência 2 para alinhar
        :type seq2: string
        :win_size: Window size (por omissão 1)
        :type win_size: int
        :stringency: Stringency (por omissão 1)
        :type stringency: int
        :printing: Formato do print da função. Se printing = True retorna uma matrix visual, se \\ 
        printing = False retorna a matriz em formato lista de listas iterável
        :type printing: boolean


    Returns:
        :return dotplot: Matriz dotplot com sequências
        :rtype dotplot: array
    
    '''
    
    if stringency > win_size:
        raise TypeError ('A stringency não pode ser superior à janela')
    
    if type(seq1) not in [str]:
        raise TypeError ('A sua sequencia 1 deve ser uma string')

    if type(seq2) not in [str]:
        raise TypeError ('A sua sequencia 2 deve ser uma string')
    
    seq1 = seq1.upper()
    seq2 = seq2.upper()
    mat = ([[' ' for s1 in range(1+len(seq2))] for s2 in range(1+len(seq1))])

    for lin in range(win_size, len(mat)):
        for col in range(win_size, len(mat[0])):
            if lin == win_size:
                count = 0
                for l in range(win_size): # dar o elementos que estao nas sequencias de acordo com a janela ( para cada elemento na janela de(x em x))
                    mat[l][col] = seq2[count + col-win_size]  # retirar a window para igualar a zero, no range do for col
                    count += 1            # contar os elementos colocados para quando formos buscar o elemento ao seq atraves do indice este nao seja repetido, ira haver sempre um indice diferente

            if col == win_size:
                mat[lin][0:win_size] = seq1[lin - win_size:lin]
            # todas as linhas colocar as mini sequencias com a window, neste caso a coluna da matriz será no maximo igual á window
            # vai sempre do valor da linha - o win_size para dar 0, até (:) o proprio valor da linha (X)


            same_nt = 0    # ver quantos valores das 'mini' sequencias sao iguais
            for nt in range(win_size):
                if seq1[lin - win_size:lin][nt] == seq2[col - win_size:col][nt]:
                    same_nt += 1
            # mesma logica que os de cima

            if same_nt >= stringency:
                mat[lin][col] = "*"
                
    #printing
    result = ''
    if printing == True:
        for lin in range(len(mat)):
            result +=' '.join(mat[lin])
            if lin != len (mat)-1:
                result+='\n'
        return result
    elif printing == False:
        return mat

def pwm(lista_seqs: List[str], pseudo: int = 0, printing: bool = True):
    ''' 
    Funcao que recebe uma lista de sequencias de tamanho igual o valor da pseucocontagem e o tipo de printing desejado. Devolve o perfil PWM das mesmas. \n
        
    Inputs:
        :lista_seqs: Lista de sequências
        :type lista_seqs: List[str]
        :pseudo: Valor da pseudocontagem do PWM (por omissão 0)
        :type pseudo: int
        :printing: Modo de retorno da matriz
        :type printing: bool
        
    Returns:
        :return PWM: PWM das sequências
        :rtype PWM: array
    '''
    if type(lista_seqs) not in [list]:
        raise TypeError ('A sua lista de sequências não é uma lista')

    for i in lista_seqs:
        if type(i) not in [str]:
            raise TypeError ('A sua lista de sequências possui valores que não são strings.')
    
    if len(lista_seqs) == 1:
        raise TypeError ('A sua lista de sequências deve ter mais do que uma sequência.')

    
    num_seqs = len(lista_seqs)
    result = []
    for z in zip(*lista_seqs):
        result.append({k: (z.count(k) + pseudo) / (num_seqs + (pseudo * 4)) for k in 'ACGT'})
    # o valor de pseudo é multiplicado pelo valor das bases, no caso de ser proteina pelos aminoacidos
    
    #print
    if printing == True:
        bases = sorted(result[0].keys())    # Do primeiro dicionario da lista de listas, tirar as keys (a,c,g,t)
        tab = [[f"{p[b]:-5.2f}" for b in bases] for p in result]    # para cada linha em perfil adicionar um (a,c,g,t)
        for p in zip(*([bases] + tab)):
            print (*p)
    else:
        return result

def pssm(lista_seqs: List[str], pseudo: int = 1, printing: bool = False):
    ''' 
    Funcao que recebe uma lista de sequencias de tamanho igual e a pseudocontagem (pseudo). Devolve o perfil PSSM das mesmas. \n
    
    Inputs:
        :lista_seqs: Lista de sequências
        :type lista_seqs: List[str]
        :pseudo: Valor da pseudocontagem do PSSM (por omissão 0)
        :type pseudo: int
        
    Returns:
        :return PSSM: PSSM das sequências
        :rtype PSSM: array
    '''

    if type(lista_seqs) not in [list]:
        raise TypeError ('A sua lista de sequências não é uma lista')

    for i in lista_seqs:
        if type(i) not in [str]:
            raise TypeError ('A sua lista de sequências possui valores que não são strings.')
    
    if len(lista_seqs) == 1:
        raise TypeError ('A sua lista de sequências deve ter mais do que uma sequência.')

    if pseudo == 0:
        raise TypeError ('A pseudocontagem do algoritmo PSSM não pode ser 0')

    num_seqs = len(lista_seqs)
    result = []
    for z in zip(*lista_seqs):
        result.append({k: log((z.count(k) + pseudo) * 4 / (num_seqs + (pseudo * 4)), 2) for k in "ACGT"})
    
    # print
    if printing == True:
        bases = sorted(result[0].keys())    # Do primeiro dicionario da lista de listas, tirar as keys (a,c,g,t)
        tab = [[f"{p[b]:-5.2f}" for b in bases] for p in result]    # para cada linha em perfil adicionar um (a,c,g,t)
        for p in zip(*([bases] + tab)):
            print(*p)
    else:
        return result

def seq_mais_prob(lista_seqs: List[str], seq: str, pseudo: int = 0):

    '''
    Funcao que recebe uma lista de sequencias com o mesmo tamanho, a pseudocontagem (pseudo) e uma sequencia maior. Esta funcao vai realizar
    um perfil pwm e descobrir de entre as sequências na lista de sequencias a mais provavel de ocorrer. \n

    Inputs:
        :lista_seqs: Lista de sequências
        :type lista_seqs: List[str]
        :seq: Sequência DNA
        :type seq: string
        :pseudo: Valor da pseudocontagem para o PWM (por omissão 0)
        :type pseudo: int
        
    Returns:
        :return seq_mais_provavel: Sequência mais provavel com base nos inputs
        :rtype PWM: str 
    '''

    if type(lista_seqs) not in [list]:
        raise TypeError ('Deve dar input de uma lista de strings')

    def pwm(lista_seqs,pseudo=0):
        num_seqs = len(lista_seqs)
        result = []
        for z in zip(*lista_seqs):
            result.append({k: (z.count(k) + pseudo) / (num_seqs + (pseudo * 4)) for k in "ACGT"})
        return result
    
    def prob_seq(seq,pwm):
        assert len(seq)==len(pwm), "Tamanhos diferentes entre 'seq' e 'pwm'!"
        result = 1
        for s in range(len(seq)):
            result *= pwm[s][seq[s]]
        return result
    
    def mais_prob(seq,P):
        chave=[]
        valor=[]
        for s in re.findall('(?=(....))', seq):
            chave.append(s)
            valor.append(prob_seq(s, pwm = P))
        dic= dict(zip(chave, valor))
        return f'{max(dic, key=dic.get)}', f'{dic[max(dic, key=dic.get)]}'
        # print(f'Sequencia mais provavel:{max(dic, key=dic.get)}')
        # print(f'Probabilidade da sequencia mais provavel: {dic[max(dic, key=dic.get)]}')
        
    
    P=pwm(lista_seqs,pseudo)
    return mais_prob(seq,P)

def alinhamentos(s1: str, s2: str, blossum: bool = False,  eqs: int = 2, diffs: int = 0, g: int = -1, local: bool = False, mat_print: bool = False):
    '''
    Esta função recebe duas sequências e realiza um alinhamento local ou global, conforme escolha do utilizador. É também possivel escolher
    a utilização, ou não, da matriz BLOSSUM para calculo do score ou podem ser passados como argumentos os valores para o calculo do mesmo.

    Inputs:
        :s1: Sequência 1
        :type s1: str
        :s2: Sequência 2
        :type s2: str
        :blossum: Matriz BLOSSUM
        :type blossum: bool
        :eqs: Valor do score para bases iguais
        :type eqs: int
        :diffs: Valor do score para bases diferentes
        :type diffs: int
        :g: Valor do score para espaçamento
        :type g: int
        :local: Tipo de alinhamento
        :type local: bool
        :printing: Modo de retorno do output
        :type printing: bool

    Returns:
        :return matriz int: Matriz com o valor do score
        :return matriz traceback: Matriz traceback do alinhamento
        :return score alinhamento: Score do alinhamento
        :return alinhamento: Duas sequências alinhadas
    '''
    if type(s1) not in [str] or type(s2) not in [str]:
        raise TypeError ('As suas sequências devem ser strings')

    if s1 not in s1.upper() or s2 not in s2.upper():
        raise TypeError ('As suas sequências devem estar em maiúsculas')

    def blossum62():
        linhas = '''   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V  B  Z  X  *
        A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0 -2 -1  0 -4
        R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3 -1  0 -1 -4
        N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3  3  0 -1 -4
        D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3  4  1 -1 -4
        C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1 -3 -3 -2 -4
        Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2  0  3 -1 -4
        E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4
        G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3 -1 -2 -1 -4
        H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3  0  0 -1 -4
        I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3 -3 -3 -1 -4
        L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1 -4 -3 -1 -4
        K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2  0  1 -1 -4
        M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1 -3 -1 -1 -4
        F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1 -3 -3 -1 -4
        P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2 -2 -1 -2 -4
        S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2  0  0  0 -4
        T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0 -1 -1  0 -4
        W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3 -4 -3 -2 -4
        Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1 -3 -2 -1 -4
        V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4 -3 -2 -1 -4
        B -2 -1  3  4 -3  0  1 -1  0 -3 -4  0 -3 -3 -2  0 -1 -4 -3 -3  4  1 -1 -4
        Z -1  0  0  1 -3  3  4 -2  0 -3 -3  1 -1 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4
        X  0 -1 -1 -1 -2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -2  0  0 -2 -1 -1 -1 -1 -1 -4
        * -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4  1'''
        blossum = {}
        headers, *mat = [linha.split() for linha in linhas.splitlines()]
        for linha in mat:
            letra, *resto = linha
            blossum[letra] = {}
            for outra, val in zip(headers, resto):
                blossum[letra][outra] = int(val)
        return blossum

    blossum62 = blossum62()

    def score_blossum(x1, x2, blossum):
        return blossum[x1][x2]

    def score(x1, x2): # match é 2 e nao match -1
        return eqs if x1 == x2 else diffs

    def pmat(s1, s2, mat):
        print(" ", *("-" +s2), sep = " " * 3)
        for x1, linha in zip("-" + s1, mat):
            print(x1, *[f"{x : 3d}"for x in linha])

    def ptr(s1, s2, mat):
        print(" ", *("-" +s2), sep = " " * 3)
        for x1, linha in zip("-" + s1, mat):
            print(x1, *[f"{x.rjust(3)}"for x in linha])

    def align(s1, s2, g):
        #g = -8
        mat = [[0 for C in range(len(s2) + 1)] for L in range(len(s1) + 1)]
        tr = [[" " for C in range(len(s2) + 1)] for L in range(len(s1) + 1)]
        for L in range(len(s1)):
            mat[L + 1][0] =mat[L][0] + g
            tr[L + 1][0] = "C"
        for C in range(len(s2)):
            mat[0][C + 1] =mat[0][C] + g
            tr[0][C + 1] = "E"
        if local:
            for L in range(len(s1)):
                mat[L + 1][0] = 0
                tr[L + 1][0] = "0"
            for C in range(len(s2)):
                mat[0][C + 1] = 0
                tr[0][C + 1] = "0"
        for L, x1 in enumerate(s1):
            for C, x2 in enumerate(s2):
                if blossum:
                    valor = [mat[L][C] + score_blossum(x1, x2, blossum62),  # diagonal
                             mat[L + 1][C] + g,  # vertical
                             mat[L][C + 1] + g]  # horizontal

                else:
                    valor=[mat[L][C] + score(x1, x2), #diagonal
                        mat[L + 1][C    ] + g, #vertical
                        mat[L    ][C + 1] + g] #horizontal

                if local: valor.append(0)
                direcoes = "D E C 0".split()
                mat[L + 1][C + 1] = max(valor)
                tr[L + 1][C + 1] = direcoes[valor.index(mat[L + 1][C + 1])]
                if sorted(valor)[-1] == sorted(valor)[-2]:
                    if valor[0] == valor[1]: tr[L + 1][C + 1] = "DE"
                    if valor[0] == valor[2]: tr[L + 1][C + 1] = "DC"
                    if valor[1] == valor[2]: tr[L + 1][C + 1] = "EC"
                    if valor[0] == valor[1] and valor[0] == valor[2]: tr[L + 1][C + 1] = "DCE"

        return mat, tr

    mat_valores, mat_direcoes = align(s1,s2, g)

    def criar_seqs(x, y, i , str_seq1, str_seq2, mat_val, mat_dir, s1, s2):
        if local is True and mat_dir[x][y] == "0":
            return str_seq1, str_seq2

        if (x == 0 and y == 0):
            return str_seq1, str_seq2
        
        if mat_dir[x][y] == "D":
            str_seq1[i] += s1[x - 1]
            str_seq2[i] += s2[y - 1]

            criar_seqs(x - 1, y - 1, i, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)

        elif mat_dir[x][y] == "E":
            str_seq1[i] += "-"
            str_seq2[i] += s2[y - 1]
            criar_seqs(x, y - 1, i, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)

        elif mat_dir[x][y] == "C":
            str_seq1[i] += s1[x - 1]
            str_seq2[i] += "-"
            criar_seqs(x - 1, y, i, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)

        elif mat_dir[x][y] == "DE":
            str_seq1.append(str_seq1[i])
            str_seq2.append(str_seq2[i])
            # Para caminho diagonal
            str_seq1[i] += s1[x - 1]
            str_seq2[i] += s2[y - 1]
            criar_seqs(x - 1, y - 1, i, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)
            # Para caminho esquerda
            str_seq1[i + 1] += "-"
            str_seq2[i + 1] += s2[y - 1]
            criar_seqs(x, y - 1, i + 1, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)

        elif mat_dir[x][y] == "DC":
            str_seq1.append(str_seq1[i])
            str_seq2.append(str_seq2[i])
            # Para caminho diagonal
            str_seq1[i] += s1[x - 1]
            str_seq2[i] += s2[y - 1]
            criar_seqs(x - 1, y - 1, i, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)
            # Para caminho cima
            str_seq1[i + 1] += s1[x - 1]
            str_seq2[i + 1] += "-"
            criar_seqs(x - 1, y, i + 1, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)

        elif mat_dir[x][y] == "EC":
            str_seq1.append(str_seq1[i])
            str_seq2.append(str_seq2[i])
            # Para caminho esquerda
            str_seq1[i] += "-"
            str_seq2[i] += s2[y - 1]
            criar_seqs(x, y - 1, i, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)
            # Para caminho cima
            str_seq1[i + 1] += s1[x - 1]
            str_seq2[i + 1] += "-"
            criar_seqs(x - 1, y, i + 1, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)

        elif mat_dir[x][y] == "DCE":
            str_seq1.append(str_seq1[i])
            str_seq2.append(str_seq2[i])
            str_seq1.append(str_seq1[i])
            str_seq2.append(str_seq2[i])
            # Para caminho diagonal
            str_seq1[i] += s1[x - 1]
            str_seq2[i] += s2[y - 1]
            criar_seqs(x - 1, y - 1, i, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)
            # Para caminho esquerda
            str_seq1[i + 1] += "-"
            str_seq2[i + 1] += s2[y - 1]
            criar_seqs(x, y - 1, i + 1, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)
            # Para caminho cima
            str_seq1[i + 2] += s1[x - 1]
            str_seq2[i + 2] += "-"
            criar_seqs(x - 1, y, i + 2, str_seq1, str_seq2, mat_val, mat_dir, s1, s2)
        sequencias = []
        sequencias.append(str_seq1)
        sequencias.append(str_seq2)
        return sequencias

    str_seq1 = [""]
    str_seq2 = [""]
    x = len(mat_direcoes) -1
    y = len(mat_direcoes[0]) -1
    if local:
        best_index = []
        best = (0, 0, 0)
        for l in range(len(mat_valores)):
            valores = mat_valores[l]
            if max(valores) >= best[0]:
                best = (max(valores), l, valores.index(max(valores)))
        best_index.append(best[1:])
        best_ind = best_index[0]
        x, y = best_ind[0], best_ind[1]
    sequencias = criar_seqs(x, y, 0, str_seq1, str_seq2, mat_valores, mat_direcoes, s1, s2)
    sequencias_done = []
    for i in range(len(sequencias)-1):
        sq1 = sequencias[0]
        sq2 = sequencias[1]
        sequencias_done.append(sq1[i])
        sequencias_done.append(sq2[i])


    def print_final(sequencias_done, mat_valores, mat_direcoes):
        max_score = []
        for m in range(len(mat_valores)):
            max_score.append(max(mat_valores[m]))
        max_score = max(max_score)
        sequencias_finais = []
        for s in sequencias_done: sequencias_finais.append(s[::-1])
        if mat_print:
            pmat(s1, s2, mat_valores)
            print("\n-----------------------------------\n")
            ptr(s1, s2, mat_direcoes)
            print("\n")
            if local:
                print("Melhor score do alinhamento otimo local: " + str(max_score))
            else:
                print("Melhor score do alinhamento otimo global: " + str(max_score))
            if len(sequencias_finais) == 2:
                print(f"Alinhamento: \n{sequencias_finais[0]}\n{sequencias_finais[1]}")
            if len(sequencias_finais) == 4:
                print(f"Alinhamento 1: \n{sequencias_finais[0]}\n{sequencias_finais[1]}\n")
                print(f"Alinhamento 2: \n{sequencias_finais[2]}\n{sequencias_finais[3]}")
        else: return sequencias_finais
    return print_final(sequencias_done, mat_valores, mat_direcoes)

def alinhamento_progressivo(seqs: List[str]) -> List[str]:
    '''
    Esta função recebe um lista de sequências e alinha-as progressivamente utilizando a ordem pela qual estão na lista.

    :seqs: Lista de sequências, ordenadas de forma decrescente pelo tamanho
    :type seqs: List

    :return seqs: Lista de sequências alinhadas progressivamente
    :rtype seqs: List

    '''

    if type(seqs) not in [list]:
        raise TypeError ('Deve inserir uma lista de sequências (strings) a alinhar')
        
    def global_align(s1, s2):
        sequencias = alinhamentos(s1, s2, eqs=4, diffs=-1, g=-4)
        A1, A2 = sequencias[0], sequencias[1]
        return A1, A2

    def consensus(s1, s2):
        return "".join(x1 if x1 == x2 else x1 if x2 == "-" else x2 for x1, x2 in zip(s1, s2))

    def malign(seqs):
        s1, s2, *resto = seqs
        A1, A2 = global_align(s1, s2)
        res = [A1, A2]
        Cons = consensus(A1, A2)
        for s in resto:
            A1, A2 = global_align(Cons, s)
            res.append(A2)
            Cons = consensus(A1, A2)

        res = []
        for s in seqs:
            A1, A2 = global_align(Cons, s)
            res.append(A2)
        return res
    return malign(seqs)



