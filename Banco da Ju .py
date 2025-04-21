# Banco da Júlia 2.0

saldo = 0

print("Bem-vindo(a) ao Banco da Júlia, o melhor do Brasil - rápido, fácil e simples!")

while True:
    print("\nO que você quer fazer?")
    print("1 - Ver saldo")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("4 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print(f"Seu saldo é R${saldo}")
    elif escolha == "2":
        valor = int(input("Quanto você quer depositar? R$"))
        saldo += valor
        print(f"Depósito feito! Seu saldo agora é R${saldo}")
    elif escolha == "3":
        print (f"O valor disponível para saque é de: R${saldo}")
        saque = int(input("Quanto você quer sacar? R$"))
        if saque > saldo:
            print("Saldo insuficiente! Tente de novo.")
        else:
            saldo -= saque
            print(f"Saque feito! Seu saldo agora é R${saldo}")
    
    elif escolha == "4":
        print("Tchau! Obrigado por usar nosso.")
        break
    else:
        print("Opção inválida! Tente de novo.")
