# lista com os dados dos atendentes
atendentes = []


# função para adicionar um atendente
def adicionar_atendente(nome):
    # verifica se existe um nome
    if not nome:
        raise ValueError("O nome do atendente não pode ser vazio.")
    # verifica se o atendente já existe
    if nome in [a["nome"] for a in atendentes]:
        raise ValueError("Atendente já existe.")
    # adiciona o atendente à lista
    atendentes.append({"nome": nome, "vendas": 0})
    return "ok"

    # funçãp para resetar os dados dos atendentes


def resetar():
    atendentes.clear()


# função para incrementar a venda de um atendente
def incrementar_venda(indice):
    atendentes[indice]["vendas"] += 1


# função para obter os atendentes
def obter_atendentes():
    return atendentes
