from datetime import datetime

def saldo_bancario(valor_conta):
    print(f"\033[32m{'SALDO ATUAL':~^48}\nR${valor_conta:.2f}\033[m")


def deposito_valido():
    valor_deposito = float(input("VALOR DO DEPOSITO\n-->"))
    if valor_deposito > 0:
        print(f"\033[32mDEPOSITO DE R${valor_deposito:.2f} EFETUADO!\033[m")
        return valor_deposito
    else:
        print(f"\033[31m{'DEPOSITO INVÁLIDO':~^48}\033[m")
        return 0


def saque_valido():
    valor_saque = float(input("VALOR A SER SACADO\n-->"))
    if 0 < valor_saque <= 500:
        print(f"\033[32mVALOR DE {valor_saque:.2f} SACADO!\033[m")
        return valor_saque
    else:
        print(f"\033[31m{'SAQUE INVÁLIDO':~^48}\033[m\nO valor do saque precisa estar entre R$1,00 a R$500,00")
        return 0


def extrato_bancario(extrato):
    for transacao in extrato:
        print(f"\033[34m{transacao[0].strftime('%d/%m/%Y %H:%M:%S')} - {transacao[1]} - R${transacao[2]:.2f}\033[m")
        print("-" * 48)


cadastro_usuario = []
while True:
    print(f"\033[32m{'BANCO SEP':-^48}\033[m")
    opcoes = input(f"{'OPÇÕES':^48}\n[1]ACESSAR CONTA [2]CADASTRO DE CLIENTE [3]SAIR\n--> ")
    if opcoes == "2":
        nome = input("Digite seu nome: ").title().split()
        senha = input("Digite sua senha: ").split()
        usuario = {"Nome": nome, "Senha": senha, "Saldo": None}
        cadastro_usuario.append(usuario)
        print(f"\033[32m{'CADASTRO REALIZADO COM SUCESSO!!!':~^48}\033[m")
    elif opcoes == "1":
        nome = input("Digite seu nome: ").title().split()
        senha = input("Digite sua senha: ").split()
        for usuario in cadastro_usuario:
            if usuario["Nome"] == nome and usuario["Senha"] == senha:
                print(f"\033[32m{'BEM VINDO!!!':~^48}\033[m")
                saldo = usuario["Saldo"] or 0
                deposito_diario, saque_diario = 4, 3
                historico_transacoes = []
                while True:
                    print("~" * 48)
                    escolha_opcao = input(
                        f"{'OPÇÕES': ^48}\n{'[1]SALDO [2]DEPOSITO [3]SAQUE [4]EXTRATO [5]SAIR'}\n-->")
                    if escolha_opcao == "1":
                        saldo_bancario(saldo)
                    elif escolha_opcao == "2":
                        if deposito_diario != 0:
                            valor_deposito = deposito_valido()
                            saldo += valor_deposito
                            deposito_diario -= 1
                            historico_transacoes.append((datetime.now(), "DEPOSITO", valor_deposito))
                        else:
                            print(f"\033[31m{'DEPOSITO DIÁRIO EXCEDIDO':~^48}\033[m")
                    elif escolha_opcao == "3":
                        if saque_diario != 0:
                            if saldo >= 500:
                                valor_saque = saque_valido()
                                saldo -= valor_saque
                                saque_diario -= 1
                                historico_transacoes.append((datetime.now(), "SAQUE", valor_saque))
                            else:
                                print(f"\033[31m{'SAQUE INVÁLIDO':~^48}\033[m\nSua conta possui R${saldo:.2f}.\nSaque mínimo de R$500,00")
                        else: 
                            print(f"\033[31m{'SAQUE DIÁRIO EXCEDIDO':~^48}\033[m")
                    elif escolha_opcao == "4":
                        if len(historico_transacoes) > 0:
                            extrato_bancario(historico_transacoes)
                        else:
                            print(f"\033[31m{'NENHUMA OPERAÇÃO REALIZADA':~^48}\033[m")
                    elif escolha_opcao == "5":
                        print(f"\033[32m{'VOLTE SEMPRE':~^48}\033[m")
                        usuario["Saldo"] = saldo
                        break
                    else:
                        print(f"\033[31m{' OPÇÃO INVÁLIDA ':~^48}\033[m")
        else:
            print(f"\033[31m{'USUARIO NÃO CADASTRADO!!!':~^48}\033[m")
    elif opcoes == "3":
        print(f"\033[32m{'VOLTE SEMPRE':~^48}\033[m")
        break
    else:
        print("Opção inválida.")