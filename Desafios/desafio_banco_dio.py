menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
'''

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))
    
    if opcao == 1:
        valor = float(input("Informe o valor do deposito"))
        if(valor > 0):
            saldo+=valor
            extrato+=f"Deposíto: R${valor:.2f}\n Saldo: R${saldo}"
        else :
            print("Valor inserido é inválido")
    
    elif opcao == 2:
        valor = float(input("Informe o valor do saque"))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > LIMITE
        
        excedeu_saques = numero_saques > LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente")
        
        elif excedeu_limite:
            print(f"Você não pode sacar mais que R${LIMITE}")
        
        elif excedeu_saques:
            print(f"você tem direito apenas a {LIMITE_SAQUES} por dia!")
        
        elif valor > 0:
            saldo-= valor
            extrato = f"Saque R${valor}"
            numero_saques +=1
        else:
            print("Valor informado é inválido")
            
    elif opcao == 3:
        print("\n================== EXTRATO ==================")
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    
    
        
        

        
        
        
            
                
        
        