from typing import Optional


banco = [
    {"conta": 1, "cliente": "marcos", "saldo": 150.50},
    {"conta": 2, "cliente": "maria", "saldo": 320.00}
]

conta_atual = 2


def adicionarconta(nome: str, saldo: float) -> None:
    global conta_atual
    conta_atual += 1
    conta = {
        "conta": conta_atual,
        "cliente": nome,
        "saldo": saldo
    }
    banco.append(conta)
    print("conta cadastrada com sucesso!")


def obterconta(conta: int) -> Optional[dict or None]:
    for cliente in banco:
        if cliente['conta'] == conta:
            return cliente
    return None


def buscarcliente(conta: int) -> None:
    cliente = obterconta(conta)
    if cliente:
        print(f"N. Conta: {cliente['conta']}")
        print(f"Nome: {cliente['cliente']}")
        print(f"saldo: {cliente['saldo']}")
    else:
        print('cliente não existe!')

def listarTodos() -> None:
    for clinte in banco:
        buscarcliente(clinte['conta'])
        print('--------------------')

def editarNome(conta: int, novo_nome: str) -> None:
    cliente = obterconta(conta)
    if cliente:
        cliente['cliente'] = novo_nome
        print('Dados alterados com sucesso!')
    else:
        print('Cliente não encontrato!')

def removerConta(conta: int) -> None:
    cliente = obterconta(conta)
    if cliente:
        banco.remove(cliente)
        print('Cliente removido com sucesso!')
    else:
        print('Cliente não encontrato')


















