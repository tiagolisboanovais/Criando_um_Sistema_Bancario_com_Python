menu = """
=========== MENU BANCÁRIO ===========
  Bem vindo ao sistema do Banco TI!
   Escolha uma das opções abaixo:
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [q] Sair
=====================================

Digite abaixo a opção desejada:

"""

saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        
        valor_deposito = float(input("Digite o valor que você quer depositar: "))
        
        while valor_deposito < 0 :
            print("Você deve digitar um valor maior que R$ 0,00 para depositar")
            valor_deposito = float(input("Por favor, digite novamente abaixo o valor a ser depositado:")) 
        else:
            print(f"""Depósito realizado com sucesso!
O valor depositado foi R$ {valor_deposito} """)
            saldo = saldo + valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            

    
    elif opcao == "s":
        valor_saque = float(input("Digite o valor que você deseja sacar: "))
        
        while saldo < 0:
            
            print("Você não tem saldo suficiente para sacar.")
            
        else:
            while valor_saque <= 0 or valor_saque > limite_por_saque:
                print("Você deve digitar um valor maior que R$ 0,00 e menor que R$ 500,00!")
                valor_saque = float(input("Por favor, digite o valor que você deseja sacar: ")) 
            else:
                if numero_saques < LIMITE_SAQUES and saldo > 0: 
                    print(f"""Saque realizado com sucesso!
O valor sacado foi R$ {valor_saque} """)
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                    saldo = saldo - valor_saque
                    numero_saques = numero_saques + 1
                else: 
                    if numero_saques >= LIMITE_SAQUES and saldo <= 0:
                        print("Você não tem saldo suficiente e atingiu o atingiu o número total de saques diários.")
                    else:
                        if saldo <= 0:
                            print("Você não tem saldo suficiente para sacar.")
                        if numero_saques >= LIMITE_SAQUES:
                            print("Você atingiu o atingiu o número total de saques diários.")


    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")

    elif opcao == "q":
        mensagem_saindo_sistema = """
Saindo do Sistema...
Obrigado por usar nossos serviços!
"""
        print(mensagem_saindo_sistema)
        break
else:

    print("Operação inválida, por favor selecione novamente a operação desejada.")