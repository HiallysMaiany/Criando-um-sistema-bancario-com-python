# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []
        self.saques_diarios = 0
        self.limite_saques_diarios = 3
        self.limite_saque_valor = 500.00

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: +R${valor:.2f}')
            print(f'Depósito de R${valor:.2f} realizado com sucesso !')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self,valor):
       if self.saques_diarios >= self.limite_saques_diarios:
           print('Vocês atingiu o limite diário de saques.')
       elif valor > self.limite_saque_valor:
           print('O valor do saque excede o limite máximo de R$500,00')
       elif valor > self.saldo:
           print('Saldo insuficiente para realizar o saque.')
       elif valor <= 0:
           print('O valor do saque deve ser positivo.')
       else:
           self.saldo -= valor
           self.saques_diarios += 1
           self.extrato.append(f'Saque: -R${valor:.2f}')
           print(f'Saque de R${valor:.2f} realizado com sucesso !')

    def exibir_extrato(self):
        print(f'\nExtrato da conta de {self.titular}:')
        if not self.extrato:
            print('Não foram realizadas movimentações.')
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f'Saldo atual: R${self.saldo:.2f}\n')

    def resetar_saques_diarios(self):
        self.saques_diarios = 0

def menu():
    print('{:=^40}'.format('   MENU INICIAL    '))
    print('''
       [0] DEPÓSITO
       [1] SAQUE
       [2] EXTRATO
       [3] SAIR''')
        
conta = ContaBancaria('Hiallys', 0)

while True:
    menu()
    opcao = int(input('Digite o número que corresponde a opção desejada: '))

    if opcao == 0:
        valor = float(input("Digite o valor a ser depositado: "))
        conta.depositar(valor)

    elif opcao == 1:
        valor = float(input("Digite o valor a ser sacado: "))
        conta.sacar(valor)

    elif opcao == 2:
        conta.exibir_extrato()

    elif opcao == 3:
        print("Obrigado por usar o Sistema Bancário. Até logo!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")





    