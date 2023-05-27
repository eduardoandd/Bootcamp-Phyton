saldo = 2000

opcao = int(input("Selecione uma opção:\n[1]SACAR\n[2]DEPOSITAR\n[3] SAIR "))

if opcao == 1:
    print(f"seu saldo é: {saldo}")    
    
    for tentativa in range(1,10,1):
        
        if(tentativa <= 3) :
            if(tentativa == 1):
                print(f"Bem vindo! Essa é sua tentativa número: {tentativa} do dia")
            
                valor=float(input("Insira quanto deseja sacar "))
                if valor > saldo :
                    print("saldo insuficiente")
                else:
                    saldo = saldo-valor
                    print(f"Seu saldo é: {saldo}")
                    
            elif(tentativa !=4):
                opcao_saque=int(input("Deseja efetuar mais um saque? \n[1]SIM\n[2]NÃO" ))
                if(opcao_saque ==1):
                    print(f"Bem vindo! Essa é sua tentativa número: {tentativa} do dia!")
                    valor=float(input("Insira quanto deseja sacar"))
                    
                    if valor > saldo :
                        print("saldo insuficiente")
                    else:
                        saldo = saldo-valor
                        print(f"Seu saldo é: R${saldo}")
                        
                else:
                    print(f'''
                          Obrigado!
                              ===EXTRATO===
                          valor sacado: R${valor}
                          seu saldo: R${saldo}
                          ''')
                    break            
        else :
            
            print(f"Agora você excedeu o número de 3 tentativas  diarias")
            break

elif(opcao == 2):
    valor=float(input("Quanto deseja depositar? "))
    resultado= saldo+valor
    print(f'''
                       ===EXTRATO===
            O deposito de R${valor} foi realizado.
            O seu saldo agora é R${resultado}.
          ''')

elif(opcao ==3):
    print("Saindo...")

else:
    print("Opção inválida")
    
    
    
     
            
            
        
    
        
   
            
                
                
            
       
        
        
        
        
        
        
            
        
    
    
     
        
        
        
    
        
    



# deposito = int(input("Insira o valor de deposito "))

# extrato = f"O valor do seu deposito é: {deposito}"





# print(f'''
#       O valor da sua conta agora é: {conta_saldo + deposito}
#       ------------------------------------------------------
#       extrato:
#       {extrato}
      
#       ''')