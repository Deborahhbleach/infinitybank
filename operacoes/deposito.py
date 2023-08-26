from banco import obterconta, banco


def depositar(conta: int, valor: float) -> None:
    cliente = obterconta(conta)
    if cliente:
        cliente['saldo'] += valor
        print('Deposito realizado com sucesso!')
    else:
        print('cliente não encontrado!')

