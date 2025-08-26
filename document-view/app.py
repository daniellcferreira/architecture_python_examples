import tkinter as tk
from tkinter import messagebox
import document


# função para adicionar um atendente
def adicionar_atendente():
    nome = entrada_nome.get().strip()  # obtem o nome do atendente digitado
    resultado = document.adicionar_atendente(nome)  # tenta adicionar o atendente

    if resultado == "vazio":
        messagebox.showwarning(
            "Entrada Inválida", "O nome do atendente não pode estar vazio!"
        )
    elif resultado == "duplicado":
        messagebox.showinfo("Entrada Inválida", "O nome do atendente ja existe!")

    entrada_nome.delete(0, tk.END)  # limpa o campo de entrada
    atualizar_interface()  # atualiza a lista de atendentes exibida


# função para resetar os dados de todos os atendentes
def resetar_atendentes():
    if messagebox.askyesno(
        "Confirmação", "Tem certeza que deseja resetar todos os atendentes?"
    ):  # confirma a ação
        document.resetar()
        atualizar_interface()
        messagebox.showinfo("Reset", "Todos os atendentes foram resetados!")


# função que desenha a interface gráfica
def atualizar_interface():
    for widget in quadro_atendentes.winfo_children():
        widget.destroy()  # limpa o quadro de atendentes

    for i, atendente in enumerate(
        document.obter_atendentes()
    ):  # obtém a lista de atendentes
        rotulo = tk.Label(
            quadro_atendentes, text=f"{atendente['nome']}: {atendente['vendas']} vendas"
        )  # cria um rotulo com o nome do atendente e a quantidade de vendas
        rotulo.grid(
            row=i, column=0, sticky="w"
        )  # posiciona o rotulo na linha i e coluna 0

        botao_vender = tk.Button(
            quadro_atendentes,
            text="Vender",
            command=lambda i=i: [document.incrementar_venda(i), atualizar_interface()],
        )  # cria um botão para incrementar a venda

        botao_vender.grid(row=i, column=1)  # posiciona o botão na linha i e coluna 1


# cria a janela principal
janela = tk.Tk()
janela.title("Controle de Vendas - Smart View")

entrada_nome = tk.Entry(janela)  # campo de entrada para o nome do atendente
entrada_nome.pack(pady=5)  # posiciona o campo na janela

botao_adicionar = tk.Button(
    janela, text="Adicionar Atendente", command=adicionar_atendente
)  # botão para adicionar atendente
botao_adicionar.pack(pady=5)  # posiciona o botão na janela

botao_resetar = tk.Button(
    janela, text="Resetar Atendentes", command=resetar_atendentes
)  # botão para resetar atendentes
botao_resetar.pack(pady=5)  # posiciona o botão na janela

quadro_atendentes = tk.Frame(janela)  # quadro para listar os atendentes
quadro_atendentes.pack(pady=10)  # posiciona o quadro na janela

atualizar_interface()  # desenha a interface inicial

janela.mainloop()  # inicia o loop principal da interface
