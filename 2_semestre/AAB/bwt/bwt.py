def find_ith_occ(l, elem, index):
        j,k = 0,0
        while k < index and j < len(l):
            if l[j] == elem:
                k = k +1
            if k == index: 
                return j
            j += 1
        return -1 



class BWT:
    def __init__(self, seq):
        self.bwt = self.buildbwt(seq)
    
    
    def buildbwt(self, text):
        ls = [ ]
        for i in range(len(text)):
            ls.append(text[i:]+text[:i]) # junta á lista a primeira parte da seq junta com a segunda parte, com slicing, com 1 ( começa na posição 1 e o 0 passa para ultimo) e por aí fora
        ls.sort()
        res = " "
        for i in range(len(text)):
            res += ls[i][len(text)-1] #apanha sempre o ultimo elemento de cada tuplo na lista ls
        return res


    def get_first_col (self):
        firstcol = []
        for c in self.bwt:
            firstcol.append(c)
        firstcol.sort()
        return firstcol


    def inverse_bwt(self):
        firstcol = self.get_first_col()
        res = ""
        c = "$"
        occ = 1
        for i in range(len(self.bwt)-1):
            pos = find_ith_occ(self.bwt, c, occ)
            c = firstcol[pos]
            occ = 1
            k = pos-1
            while firstcol[k] == c and k >= 0:
                occ += 1
                k -= 1
            res += c
        return res

    def last_to_first(self):
        res = []
        firstcol = self.get_first_col()
        for i in range(len(firstcol)):
            c = self.bwt[i]
            ocs = self.bwt[:i].count(c) + 1
            res.append(find_ith_occ(firstcol, c, ocs))
        return res 


def test():
    seq = "TAGACAGAGA$"
    bw = BWT(seq)
    print (bw.bwt)
    print (bw.inverse_bwt())
    print (bw.last_to_first())
test()