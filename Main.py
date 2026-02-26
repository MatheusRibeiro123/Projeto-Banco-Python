class Main:
    "Classe principal"
    
    pass

print("testando a classe")

from Cliente import Cliente

from Conta import Conta


c1 = Cliente("João",19989735625)
conta12 = Conta(c1.get_nome(),12,0)

conta12.depositar(155)
conta12.saque(55)
conta12. extrato()

print (Main.__doc__)




