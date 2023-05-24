print(True and True)
print(True and False)
print(False and False)
print(True and True)
print(True or True)
print(False or False)
print(False or True)
print("--------------------------------------")

saldo = 100
saque = 50
limite = 50

print(saldo >= saque and saque >= limite)
print(saldo <= saque or saque >= limite)

negacao = not 1000 > 1500
print(negacao)

contatos_emergencia = []
print(contatos_emergencia)
negacao_contatos=not contatos_emergencia
print(negacao_contatos)

negacao_string=not "saque 1500"
print(negacao_string)
negacao_string=not ""
print(negacao_string)


