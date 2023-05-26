#OLD STYLE %

nome="Eduardo"
idade=21
profissao = "Programador"
linguagem="Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s. \n estou matriculado no curso de %s" % (nome,idade,profissao,linguagem))
print()
#FORMAT
print("--------FORMAT----------")
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {}. \n estou matriculado no curso de {}".format(nome,idade,profissao,linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {0}. \n estou matriculado no curso de {1}".format(nome,idade,profissao,linguagem))

print()

print("---f-string----")
print(f"Olá! Me chamo {nome} e tenho {idade} anos")

PI = 3.14343
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.4f}")
print(f"Valor de PI: {PI:5.4f}")
