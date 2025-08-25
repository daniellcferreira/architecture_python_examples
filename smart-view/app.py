import tkinter as tk
from tkinter import messagebox

# lista com os dados dos atendentes
atendentes = []


# função para adicionar atendente
def adicionar_atendente():
    nome = entrada_nome.get().strip()

    # validação do nome do atendente se estiver vazio
    if not nome:
        messagebox.showwarning(
            "Entrada Inválida", "O nome do atendente não pode estar vazio!"
        )
        return

    # validação do nome do atendente se já existir
    if nome in [a["nome"] for a in atendentes]:
        messagebox.showwarning("Entrada Inválida", "O nome do atendente já existe!")
        return

    atendentes.append({"nome": nome, "vendas": 0})  # inicializa vendas como 0
    entrada_nome.delete(0, tk.END)  # limpa o campo de entrada
    atualizar_interface()


# função para resetar os dados todos os atendentes
def resetar_atendentes():
    if messagebox.askyesno(
        "Confirmação", "Tem certeza que deseja resetar todos os dados dos atendentes?"
    ):
        atendentes.clear()

    atualizar_interface()


# função para incrementar vendas do atendente selecionado
def incrementar_vendas(indice):
    atendentes[indice]["vendas"] += 1
    atualizar_interface()


# função que desenha a interface
def atualizar_interface():
    # limpa o quadro de atendentes
    for widget in quadro_atendentes.winfo_children():
        widget.destroy()

    # redesenha os atendentes
    for i, atendente in enumerate(atendentes):
        texto = f"{atendente['nome']} - Vendas: {atendente['vendas']}"
        rotulo = tk.Label(quadro_atendentes, text=texto)
        rotulo.grid(row=i, column=0, sticky="w")

        # botão para incrementar vendas
        botao_incrementar = tk.Button(
            quadro_atendentes,
            text="+1 Venda",
            command=lambda i=i: incrementar_vendas(i),
        )
        botao_incrementar.grid(row=i, column=1) # adiciona o botão na coluna 1

# configuração da janela principal
janela = tk.Tk() # cria a janela principal
janela.title("Controle de Vendas dos Atendentes - Smart View") # título da janela

entrada_nome = tk.Entry(janela) # campo de entrada para o nome do atendente
entrada_nome.pack(pady=5) # posiciona o campo de entrada

botao_adicionar = tk.Button(janela, text="Adicionar Atendente", command=adicionar_atendente) # botão para adicionar atendente
botao_adicionar.pack() # posiciona o botão

botao_resetar = tk.Button(janela, text="Resetar Atendentes", command=resetar_atendentes) # botão para resetar atendentes
botao_resetar.pack(pady=0) # posiciona o botão

quadro_atendentes = tk.Frame(janela) # quadro para listar os atendentes
quadro_atendentes.pack(pady=10) # posiciona o quadro

atualizar_interface() # desenha a interface inicial

janela.mainloop() # inicia o loop principal da interface
