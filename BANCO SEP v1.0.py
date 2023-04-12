from datetime import datetime


print(f"\033[32m{'BANCO SEP':-^40}\033[m")
saldo, saque_diario, deposito_diario = 0, 3, 5
historico_transacoes = []
while True:
    print(f"{'OPÇÕES': ^40}\n{'[1]SALDO [2]DEPOSITO [3]SAQUE [4]EXTRATO'}")
    opcao = str(input("-->"))
    print("-" * 40)
    while opcao not in '1234':
        print(f"\033[31mOPÇÃO INVÁLIDA\033[m\n{'OPÇÕES': ^40}\n{'[1]SALDO [2]DEPOSITO [3]SAQUE [4]EXTRATO'}")
        opcao = str(input("-->"))
    if opcao == "1":
        print(f"SALDO ATUAL \nR${saldo:.2f}")
    if opcao == "2":
        if deposito_diario != 0:
            print("VALOR DO DEPOSITO")
            deposito = float(input("-->R$"))
            while not deposito > 0:
                print(f"DEPOSITO INVÁLIDO!")
                deposito = float(input("-->R$"))
            if deposito > 0:
                saldo += deposito
                historico_transacoes.append((datetime.now(), "DEPÓSITO", deposito))
                print(f"DEPOSITO DE R${deposito:.2f} EFETUADO!")
            deposito_diario -= 1
        else:
            print("DEPOSITO DIÁRIO EXCEDIDO!")
    if opcao == "3":
        if saque_diario != 0:
            if 0 < saldo <= 500:
                print("VALOR DO SAQUE")
                valor_saque = float(input("-->"))
                if 1 < valor_saque < saldo:
                    print(f"VALOR DE {valor_saque:.2f} SACADO!")
                    saldo -= valor_saque
                    saque_diario -= 1
                    historico_transacoes.append((datetime.now(), "SAQUE", -valor_saque))
                else:
                    print("VALOR DE SAQUE INVÁLIDO")
            elif saldo > 500:
                print("VALOR DO SAQUE")
                valor_saque = float(input("-->"))
                if 1 < valor_saque <= 500:
                    saldo -= valor_saque
                    saque_diario -= 1
                    historico_transacoes.append((datetime.now(), "SAQUE", -valor_saque))
                    print(f"VALOR DE {valor_saque:.2f} SACADO!")
                else:
                    print("O SAQUE DEVE ESTAR ENTRE R$1,00 E R$500,00")
            else:
                print(f"SAQUE INDISPONÍVEL!\nSALDO ATUAL --> R${saldo:.2f}")
        else:
            print("SAQUE DIÁRIO EXCEDIDO")
    if opcao == "4":
        print("HISTÓRICO DE TRANSAÇÕES")
        for transacao in historico_transacoes:
            print(f"{transacao[0].strftime('%d/%m/%Y %H:%M:%S')} - {transacao[1]} - R${transacao[2]:.2f}")
    print("-" * 40)
