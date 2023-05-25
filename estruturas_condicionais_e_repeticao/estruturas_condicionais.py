import sys


# MAIOR_IDADE = 18
# IDADE_ESPECIAL = 12

# idade = int(input("Informe sua idade: "))

# if idade >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar cnh")

# elif idade >=IDADE_ESPECIAL and idade <=MAIOR_IDADE :
#     print("Pode fazer aulas teoricas")
    
# else:
#     print("Menor de idade")


# print("-----------------------------------------")

# saldo = 300
# saque = float(input("Informe o saque: "))

# if saque <= saldo:
#     print("Sacado!")
# else:
#     print("saldo insuficiente")
    
# print("-----------------------------------------")

# opcao = int(input("Informe a opção: [1]Sacar ou [2]Extrato "))

# if opcao == 1:
#     saque= float(input("Informe quanto deseja sacar "))
#     print(saque)
# elif opcao ==2:
#     print("Extrato:")
# else:
#     sys.exit("Opção invalida")

print("-----------------------------------------")

# MAIOR_IDADE =17

# if MAIOR_IDADE >=18 :
#     print("Maior de idade")
# else :
#     print("Menor de idade")

print("IF INCADEADO")

# conta_normal = True
# conta_universitaria = True

# saldo = 2000
# saque = 1900
# cheque_especial = 500

# if conta_normal:
#     if saldo >= saque:
#         print("Saque realizado com sucesso")
#     elif saque <= (saldo + cheque_especial):
#         print("saque realizado com uso do cheque especial")
#     else:
#         print("Não foi possivel realizar o saque, saldo insuficiente")
# elif conta_universitaria:
#     if saldo >= saque:
#         print("Saque realziado com sucesso")
#     else:
#         print("Saldo insuficiente")
# else:
#     print("Sistema nao reconheseu seu tipo de conta, entre em contato com o gerente")    

print("operador ternario -----------------------")

saldo = 200
saque = 300

status = "Sucesso" if saldo >= saque else "Falha"

print(status)