import json
from datetime import datetime
bd = "transacoes.json"

def carregar_dados():
    with open(bd, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(transacoes):
    with open(bd, "w", encoding="utf-8") as f:
        json.dump(transacoes, f, indent=4, ensure_ascii=False)

def adicionar_transacao(transacoes, descricao, valor, tipo):
    transacao = {
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    transacoes.append(transacao)
    salvar_dados(transacoes)
    print(f"{tipo} registrada: {descricao} - R$ {valor}")

def calcular_saldo(transacoes):
    saldo = 0
    for transacao in transacoes:
        if transacao["tipo"] == "receita":
            saldo += transacao["valor"]
        else:
            saldo -= transacao["valor"]
    return saldo

def listar_transacoes(transacoes):
    print("Transações:")
    for transacao in transacoes:
        print(f"{transacao['data']} - {transacao['tipo']} - R$ {transacao['valor']} - {transacao['descricao']}")

def menu():
    print("===== Controle Financeiro =====")
    print("1. Adicionar receita")
    print("2. Adicionar despesa")
    print("3. Ver todas as transações")
    print("4. Ver saldo")
    print("0. Sair")
    return input("Escolha uma opção: ")

transacoes = carregar_dados()

while True:
    opcao = menu()

    if opcao == "1":
        descricao = input("Descrição da receita: ")
        valor = float(input("Valor (R$): "))
        adicionar_transacao(transacoes, descricao, valor, "receita")

    elif opcao == "2":
        descricao = input("Descrição da despesa: ")
        valor = float(input("Valor (R$): "))
        adicionar_transacao(transacoes, descricao, valor, "despesa")

    elif opcao == "3":
        listar_transacoes(transacoes)

    elif opcao == "4":
        print(f"Saldo atual: R$ {calcular_saldo(transacoes)}")

    elif opcao == "0":
        print("Até logo!")
        break
