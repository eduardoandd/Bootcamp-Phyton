frutas =['laranja', 'maçã', 'uva']
print(frutas)
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])
print(frutas[0])

frutas = []
print(frutas)


letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

print("--- LISTA ANINHADAS ---")

matriz = [
    [1,"a",2],
    ["b","a",2],
    [1,"djsk",2.7]
]

print(matriz)
print(matriz[1][2])
print(matriz[2][2])

print("--- FATIAMENTO ---")

lista = list("PYTHON")
print(lista[1:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

print("--- ITERAR LISTA ---")

carros = ["gol", "celta", "palio"]
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

print("--- ADICIONANDO NOVOS VALORES A LISTA ---")

numeros =[1,30,21,2,10,65,34]
pares =[numero for numero in numeros if numero % 2 == 0]
print(pares)

quadrado = []
for numero in numeros :
     quadrado = [numero**2  for numero in numeros]
     print(quadrado)
    
    


    


