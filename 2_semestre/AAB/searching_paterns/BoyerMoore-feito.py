# -*- coding: utf-8 -*-

class BoyerMoore:
    
    def __init__(self, alphabet, pattern):
        self.alphabet = alphabet  # alfabeto usado pelos algoritmos
        self.pattern = pattern    # padrao a ser procurado
        self.occ={}
        self.f = [0]*(len(self.pattern)+1)
        self.s = [0]*(len(self.pattern)+1)
        self.preprocess()
        
        
        #self.preprocess()

    def preprocess(self):
        self.process_bcr()
        self.process_gsr()
        
    def process_bcr(self): # codigo para pre processamento para o bad character rule
        for base in self.alphabet:
            self.occ[base]=-1
        for j in range(len(self.pattern)):
            self.occ[self.pattern[j]]=j
        #print (self.occ) 

            
    def process_gsr(self): # codigo para pre processar para o good character rule
        i = (len(self.pattern))
        j = (len(self.pattern)+1)
        self.f[i]=j
        while i >0:
            while j <= len(self.pattern) and self.pattern[i-1] != self.pattern[j-1]:
                if self.s[j]==0:
                    self.s[j] = j - i
                j = self.f[j]
            i -= 1
            j -= 1
            self.f[i] = j
        j=self.f[0]
        for i in range(len(self.pattern)):
            if self.s[i]==0:
                self.s[i]=j
            if i==j:
                j= self.f[j]

        
    def search_pattern(self, text):
        res = []
        i=0
        while i <= (len(text)-len(self.pattern)):
            j = len(self.pattern)-1
            while j >=0 and self.pattern[j]==text[j+i]:
                j-=1
            if j < 0:
                res.append(i)
                i=i+self.s[0]
            else:
                c=text[j+i]
                lista=[self.s[j+1],j-self.occ[c]]
                i+=max(lista)
        return res

def test():
    bm = BoyerMoore("ACTG", "ACCA")
    print (bm.search_pattern("ATAGAACCAATGAACCATGATGAACCATGGATACCCAACCACC"))

test()

# result: [5, 13, 23, 37]
            
