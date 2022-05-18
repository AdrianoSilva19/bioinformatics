# -*- coding: utf-8 -*-


class Automata:
    
    def __init__(self, alphabet, pattern):
        self.numstates = len(pattern) + 1
        self.alphabet = alphabet
        self.transitionTable = {}
        self.buildTransitionTable(pattern)        
    
    def buildTransitionTable(self, pattern):
        count=0
        for q in range(self.numstates):
            for a in self.alphabet:
                if q <=2:
                    pos_letra=()     # posição de partida e letra encontrada
                    pos_letra += q,a
                    self.transitionTable[pos_letra]=0 
                    # fazer condições
                    if pattern[q]==a:
                        pos_letra=()     
                        pos_letra += q,a
                        count+=1
                        self.transitionTable[pos_letra]=count
                    elif pattern[q]!=a and q!=0:
                        stage=q-1
                        pos_letra=(stage,a)
                        pos=(q,a)
                        self.transitionTable[pos]=self.transitionTable[pos_letra]
                




       
    def printAutomata(self):
        print ("States: " , self.numstates)
        print ("Alphabet: " , self.alphabet)
        print ("Transition table:")
        for k in self.transitionTable.keys():
            print (k[0], ",", k[1], " -> ", self.transitionTable[k])
         
    def nextState(self, current, symbol):
        pass
        
    def applySeq(self, seq):
        q = 0
        res = [q]
        #...
        return res
        
    def occurencesPattern(self, text):
        q = 0 
        res = []
        # ....
        return res

def overlap(s1, s2):
    maxov = min(len(s1), len(s2))
    for i in range(maxov,0,-1):
        if s1[-i:] == s2[:i]: return i
    return 0
               
def test():
    auto = Automata("AC", "ACA")
    auto.printAutomata()
    print (auto.applySeq("CACAACAA"))
    print (auto.occurencesPattern("CACAACAA"))

test()

#States:  4
#Alphabet:  AC
#Transition table:
#0 , A  ->  1
#0 , C  ->  0
#1 , A  ->  1
#1 , C  ->  2
#2 , A  ->  3
#2 , C  ->  0
#3 , A  ->  1
#3 , C  ->  2
#[0, 0, 1, 2, 3, 1, 2, 3, 1]
#[1, 4]



