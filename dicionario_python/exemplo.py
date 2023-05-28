pessoa = {"nome": "Eduardo", "idade": 21}
pessoa = dict(nome="Eduardo", idade=21)

pessoa["telefone"] = "993582674"
print(pessoa)
print(pessoa["nome"])
pessoa["nome"]= "Eduardo Andrade"
print(pessoa)

contatos = {
    1 : {"nome": "Eduardo Andrade", "telefone": "11993582674"},
    2 : {"nome": "Pedro henrique", "telefone": "1194382674"},
    3 : {"nome": "Eduardo", "telefone": "11993582674", "extra":{"a":1}},
}

# print(contatos[2]["telefone"])
# print(contatos[3]["extra"]["a"])

for chave in contatos:
    print(chave,contatos[chave])