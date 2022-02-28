from dic import dic as d


class PWD_MANAGER:
    def __init__(self) -> None:
        self.pwd=""
        self.enc_pwd=""
        # dar o import de todas as pass ja guardadas no txt e passar para o dic_pass
        
        self.dic_pass={}

    def encry(self):
        '''função que encripta as pass'''
        dic=d
        pwd = self.pwd
        new_pwd=""
        for letter in pwd:
            if letter in dic:
                new_pwd+=dic[letter]
            if letter not in dic:
                new_pwd+=letter
        return new_pwd
    
    def get_key(self,val):
        '''função que vai buscar a key correspondente a um certo valor'''
        for key, value in d.items():
            if val == value:
                return key


    def deencrypt(self):
        '''função que rever a encriptação'''
        #print(self.dic_pass.items())
        key=(str(input("Qual pass? ")))
        pwd_cryp= self.dic_pass[key]
        pwd=""
        for letter in pwd_cryp:
            pwd+=self.get_key(letter)
        print(pwd)


    def ver_file(self):
        '''função que permite ver todas as pass guardadas'''
        pass

    
    def guardar(self):
        '''função que permite guardar novas pass'''
        new=str(input("Nova password a armazenar: "))
        key=str(input("De onde é a password? "))
        self.pwd = new
        self.enc_pwd = self.encry()
        self.dic_pass[key]=self.enc_pwd
        
        
new=PWD_MANAGER()
new.guardar()
new.deencrypt()
