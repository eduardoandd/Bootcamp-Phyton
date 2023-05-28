numeros=[1,2,3,4,4,5,5]
# print(set(numeros))

# print(set("abacaxi"))

# print(set(("palio","palio","gol","celta")))

# linguagens = {"Python","Java","Python","c#"}
# print(linguagens)
# linguagens = list(linguagens)
# print(linguagens[0])

linguagens = {"Python","Java","Python","c#"}

for i ,linguagem in enumerate(linguagens):
    print(f"{i}: {linguagem}")
    
print("--- UNION ---")

conjunto_a={1,2,3,4}
conjunto_b={3,4,1}

uniao=conjunto_a.union(conjunto_b)
print(uniao)

diferenca= conjunto_a.difference(conjunto_b)
diferenca= conjunto_b.difference(conjunto_a)
print(diferenca)

symmetric = conjunto_a.symmetric_difference(conjunto_b)
print(symmetric)

print("--- issubset ---")
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

conjunto_a={1,2,3}
conjunto_b={4,5,6}


print("--- isdisjoint ---")
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_b.isdisjoint(conjunto_a))

print("---add---")
sorteio={1,23}

sorteio.add(24)
sorteio.add(26)
sorteio.add(21)
print(sorteio)

print("---discard---")

numeros = {1,2,56,765,323,5,7}
numeros.discard(1)
print(numeros)
print(len(numeros))

print(56 in numeros)

