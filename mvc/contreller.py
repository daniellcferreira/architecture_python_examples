import document as model

view = None


# Atribui a view ao controller
def atribuir_view(_view):
    global view
    view = _view


# funçõa para adicionar um atendente
def adicionar_atendente(nome):
    resultado = model.adicionar_atendente(nome)  # Chama a função do model
    if resultado == "vazio":
        view.alerta("O nome do atendente não pode ser vazio. Digite um nome válido.")
    elif resultado == "existe":
        view.alerta("Atendente já existe. Digite outro nome.")
    elif resultado == "sucesso":
        view.alerta("Atendente adicionado com sucesso.")
        view.atualizar_interface()  # Atualiza a interface da view


# função para resetar os dados de todos os atendentes
def resetar_atendentes():
    model.resetar()
    view.atualizar_interface()


# função para adicionar uma venda
def registrar_venda(indice):
    model.registrar_venda(indice)
    view.atualizar_interface()


# função listar os atendentes
def lista_atendentes():
    return model.obter_atendentes()
