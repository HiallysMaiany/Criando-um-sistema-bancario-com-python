def menu():
    print('{:=^40}'.format('  MENU INICIAL  '))
    print('''
       [0] DEPÓSITO
       [1] SAQUE
       [2] EXTRATO
       [3] CRIAR USUÁRIO
       [4] CRIAR CONTA
       [5] SAIR''')

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques_diarios):
    if numero_saques >= limite_saques_diarios:
        print("Você atingiu o limite diário de saques.")
    elif valor > limite:
        print("O valor do saque excede o limite máximo de R$500,00.")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor <= 0:
        print("O valor do saque deve ser positivo.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque: -R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f"\nExtrato da conta:")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"Saldo atual: R${saldo:.2f}\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Já existe um usuário com esse CPF.")
        return usuarios
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário cadastrado com sucesso!")
    return usuarios

def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return contas
    numero_conta = len(contas) + 1
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(conta)
    print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario['nome']}!")
    return contas

# Variáveis globais
usuarios = []
contas = []
saldo = 0
extrato = []
numero_saques = 0
limite_saques_diarios = 3
limite_saque_valor = 500.00

while True:
    menu()
    opcao = int(input('Digite o número que corresponde a opção desejada: '))

    if opcao == 0:
        valor = float(input("Digite o valor a ser depositado: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == 1:
        valor = float(input("Digite o valor a ser sacado: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo, valor=valor, extrato=extrato, 
            limite=limite_saque_valor, numero_saques=numero_saques, 
            limite_saques_diarios=limite_saques_diarios)
    elif opcao == 2:
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == 3:
        usuarios = criar_usuario(usuarios)
    elif opcao == 4:
        contas = criar_conta(contas, usuarios)
    elif opcao == 5:
        print("Obrigado por usar o Sistema Bancário. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

