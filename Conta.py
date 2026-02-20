class Conta:
    def __init__(self, titular , numero, saldo):
        self._saldo=0
        self.numero=numero
        self.titular=titular

    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self,_saldo):
        if _saldo <0:
            print("Saldo não pode ser negativo")
        else:  
            self._saldo= _saldo