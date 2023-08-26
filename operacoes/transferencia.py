from banco import obterconta, banco


def transferir(contaori: int, contades: int, valor: float) -> None:
    contaorigem = obterconta(contaori)
    contadestino = obterconta(contades)
    if contaori and contades:
        if contaorigem['saldo'] >= valor:
            contaorigem['saldo'] -= valor
            contadestino['saldo'] += valor
            print('Tranferencia realizada com sucesso!')
        else:
            print('Saldo insuficiente para tranferencia!')
    else:
        print('Uma ou mais contas não encontradas!')

print(banco)
transferir(1, 2,150)
print(banco)