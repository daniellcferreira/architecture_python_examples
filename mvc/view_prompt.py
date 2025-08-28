import controller
from types import SimpleNamespace


# função que o controller espera da view
def atualizar_interface():
    """ "Exibe a lista de atendentes ordenada segundo o Model"""
    print("\n === CONTADOR DE VENDAS ====")

    atendentes = controller.lista_atendentes()
    if not atendentes:
        print("(Sem atendentes)")
    else:
        for idx, a in enumerate(atendentes, start=1):
            print(f"{idx}. {a['nome']}: {a['vendas']} vendas")
    print("---------------------------\n")


def alerta(titulo: str, mensagem: str):
    """Mostra uma mensagem simpleas no console."""
    print(f"[{titulo}] {mensagem}\n")


# loop principal da cli
def loop_cli():
    """Loop de leitura de comando do usuário"""
    atualizar_interface()
    print("Intruções:")
    print("  <nome>        -> adiciona atendente")
    print("  <indice>      -> incrementa vendas (ex.: 2+)")
    print("  <q> ou <quit> -> sair\n")

    while True:
        comando = input("> ").strip()
        if not comando:
            atualizar_interface()
            continue

        if comando.lower() in {"q", "quit", "sair"}:
            break

        # incremento: formato n+
        if comando.endswith("+") and comando[:-1].isdigit():
            indice = indice = int(comando[:-1]) - 1  # conversão para indice 0-based
            controller.registrar_venda(indice)
        else:
            controller.adicionar_atendente(comando)


# entry point

if __name__ == "__main__":
    # usando um SimpleNamespace para expor atualizar() e alerta()
    view_ns = SimpleNamespace(atualizar_interface=atualizar_interface, alerta=alerta)
    controller.atribuir_view(view_ns)

    # inicia o loop da cli
    loop_cli()
