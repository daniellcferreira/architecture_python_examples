# lista com os dados dos atendentes
atendentes = []


# função para adicionar um atendente
def adicionar_atendente(nome):
    # validação simples para garantir que o nome não esteja vazio
    if not nome:
        return "Você deve fornecer um nome para o atendente."
    # verifica se o atendente já existe
    if nome in [a["nome"] for a in atendentes]:
        return "Atendente já existe."

    atendentes.append({"nome": nome, "vendas": 0})  # adiciona o atendente com 0 vendas
    return f"Atendente {nome} adicionado com sucesso."


# função para resetar os dados dos atendentes
def resetar():
    atendentes.clear()
    return "Dados dos atendentes resetados."


# função para registrar uma venda
def registrar_venda(indice):
    atendentes[indice]["vendas"] += 1
    return f"Venda registrada para {atendentes[indice]['nome']}."


# função para obter os atendentes
def obter_atendentes():
    return atendentes
