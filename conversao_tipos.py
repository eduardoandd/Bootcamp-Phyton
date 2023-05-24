preco = 10
print(preco)

print("----------------------------")

preco = float(preco)
print(preco)

print("----------------------------")

preco /=2
print(preco)

print("FLOAT -> INT")

preco = int(preco)
preco *=preco
print(preco)

print("DIFERENÇA DE '/' E '//' ")

print(preco/2)
print(preco//2)

print("NUMERICO -> STRING")

preco = 10.50
idade = 28

print(preco)
print(idade)

preco = str(preco)
idade = str(idade)
print(preco+idade)

print("STRING -> FLOAT")

preco = "10.50"
preco2="28"
print(float(preco))
print(float(preco2))

print("----------------------------")

print(int(1.2))
print(int("10"))
print(str("O valor é:"), float("23.50") + int("10"))

resultado = "o resultado é: "
n1 = "10"
n2 = "10.5"
print(str(resultado), float(n1)+float(n2))
print(type(resultado))

n3 = 30
print(type(n3))

print(type(30/7)) #sla
print(type(30//3)) #30
      




