class Main:
    pass

print("testando a classe")

from Cliente import Cliente

from Conta import Conta


c1 = Cliente("João",19989735625)

conta = Conta(c1.nome,12,0)

print(conta.titular, ", numero: ",conta.numero , "seu saldo: ", conta.saldo)

