

class Conta:
    def __init__(self, titular , numero, saldo):
        self._saldo=0
        self._numero=numero
        self._titular=titular

    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self,_saldo):
        if _saldo <0:
            print("Saldo não pode ser negativo")
        else:  
            self._saldo= _saldo

    def saque(self , valor):
        if (self._saldo >= valor):
            self._saldo-= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar saque")

    def depositar(self , valor):
        self._saldo += valor

    
    def extrato(self):
        print(f"cliente : {self._titular}, Saldo atual :{self._saldo}")

