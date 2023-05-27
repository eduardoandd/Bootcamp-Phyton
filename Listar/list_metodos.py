#append - serve para adicionar novos elementos

lista = []
print(lista)

lista.append(1)
lista.append("python")
lista.append([20,"teste",20.2])
print(lista)

print("---CLEAR---")
#lista.clear()
print(lista)

print("---COPY---")
l2 = lista.copy()
print(id(lista))
print(id(l2))
l2[0] = 3
print(l2)
print(lista)

print("---COUNT---")

cores = ["Vermelho", "azul","azul","rosa",3,5,7,3]
print(cores.count("azul"))
print(cores.count(3))

print("---EXTEND---")

linguagens = ["java","python"]
linguagens.extend(["c","python"])
# print(linguagens)
# print(linguagens.index('python'))

print(linguagens.pop())
print(linguagens.pop(0))
print(linguagens.pop(1))
print(linguagens)
linguagens.remove('python')
print(linguagens)

print("---REVERSE---")

linguagens = ["java","python"]
linguagens.extend(["c","python"])
linguagens.reverse()
print(linguagens)

print("---SORT---")
linguagens = ["java","python"]
linguagens.extend(["c","ruby"])
print(linguagens)

linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

linguagens.sort(reverse=False)
print(linguagens)

linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

print("---len---")

print(len(linguagens))







