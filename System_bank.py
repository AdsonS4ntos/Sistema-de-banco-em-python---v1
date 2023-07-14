menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [f] Fechar


    => """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        inserir_valor = int(input("Insira o valor para depositar: "))

        if inserir_valor < 0:
            print("Não é possível depositar um valor negativo.")
        else:
            if inserir_valor > limite:
                print(f"O valor {inserir_valor} está acima do limite, operação inválida. Tente novamente com valores abaixo de R$ 500.")
            else:
                saldo += inserir_valor
                extrato.append(f"Depósito: +R${inserir_valor}")
                print(f"Foi depositado o valor de R$ {inserir_valor}. Seu saldo atual é R$ {saldo}")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido")
        else:
            inserir_saque = int(input("Insira o valor para sacar: "))

            if inserir_saque > saldo:
                print("Não é possível sacar um valor acima do saldo disponível.")
            else:
                saldo -= inserir_saque
                numero_saques += 1
                extrato.append(f"Saque: -R${inserir_saque}")
                print(f"O valor sacado foi de R${inserir_saque}. Seu saldo atual é R${saldo}. Total de saques: {numero_saques}")

    elif opcao == "e":
        print(f"Seu saldo atual é: R${saldo}")
        if len(extrato) == 0:
            print("Não houve movimentações no extrato.")
        else:
            print("Extrato:")
            for operacao in extrato:
                print(operacao)

    elif opcao == "f":
        print("Operação finalizada")
        break

    else:
        print("Operação inválida. Tente novamente com as opções fornecidas.")