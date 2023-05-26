nome = input("Informe o seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
print(nome, end='....\n')
print(sobrenome)


T = input("Digite seu texto")

if(len(T) >=140):
    print("MUTE")
else:
    print("TWEET")