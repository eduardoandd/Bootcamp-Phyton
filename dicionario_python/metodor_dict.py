contatos = {
    "teste":{"nome":"Eduardo", "idade":21},
    2:{"nome":"Eduardo amdrade", "idade":21},
    3:{"nome":"Andre rodrigues", "idade":21}
}

contatos.clear()
print(contatos)


print("--- COPY ---")

copia = contatos.copy()
print(id(contatos))
print(id(copia))

print("--- FROMKEYS ---")

chave= dict.fromkeys(["nome","telefone"])
print(chave)
chave2 = dict.fromkeys(["nome","telefone"], "eduardo")
print(chave2)

print("--- GET ---")

contatos = {
    "teste":{"nome":"Eduardo", "idade":21},
    2:{"nome":"Eduardo amdrade", "idade":21},
    3:{"nome":"Andre rodrigues", "idade":21}
}

print(contatos.get("chave"))
print(contatos.get("chave",[]))
print(contatos.get(2))

print("--- items ---")

print(contatos.items())

print("--- Keys ---")

novo_dicionario = {1:100, 2:"teste", "b":"python"}
print(novo_dicionario.keys())

print("--- pop ---")

#print(novo_dicionario.pop(1))
#print(novo_dicionario.pop(1),{})

print("--- popItem ---")
print(novo_dicionario.popitem())

print("--- setDefault ---")

print(novo_dicionario.setdefault("idade",28))
print(novo_dicionario)

print("--- update ---")
novo_dicionario.update({1:200})
print(novo_dicionario)

print("--- values ---")
print(novo_dicionario.keys(),novo_dicionario.values())

print("--- in ---")

teste= {
    1:{"nome": "Eduardo","idade": 21,"telefone": "11993582674"},
    2:{"nome": "Josiane Sanches de Andrade", "idade": 40,"telefone":"11993582674"}    
}

resultado = 1 in novo_dicionario
print(resultado)

resultado= "nome" in teste[2]
print(resultado)

print("--- del ---")

del teste[1]["telefone"]
del teste[2]
print(teste)




