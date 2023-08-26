from banco import obterconta, banco

def consultarSaldo(conta: int) -> None:
    cliente = obterconta(conta)
    if cliente:
        print(f"seu saldo: {cliente['saldo']}")
    else:
        print('Cliente não encontrato!')




