import cliente

class Conta():
    def __init__(self, User, saldo, limite) :
        self.saldo = saldo
        self.User = User
        self.limite = limite


    def Sacar(self):
        return F"Voce sacou R${self.saldo}"
        self.saldo = int(0)
            
        
    def Depositar(self, valor):
        self.saldo += valor
        return F"Voçe depositou R${valor} \nseu saldo atual e de {self.saldo}."
    
        
    def Mostrar(self):   
        return F"seu saldo atual e de R${self.saldo}"

    
       
          



           


    

        

