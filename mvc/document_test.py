import document

# Testes para o módulo document.py
def test_adicao_e_duplicacao():
  document.resetar()

  assert document.adicionar_atendente("Alice") == "Atendente Alice adicionado com sucesso."
  assert document.adicionar_atendente("") == "Você deve fornecer um nome para o atendente."
  assert document.adicionar_atendente("Alice") == "Atendente já existe."

def test_registro_venda():
  document.resetar()
  document.adicionar_atendente("Bob")
  document.adicionar_atendente("Charlie")

  assert document.registrar_venda(0) == "Venda registrada para Bob."
  assert document.registrar_venda(1) == "Venda registrada para Charlie."
  assert document.registrar_venda(0) == "Venda registrada para Bob."

  atendentes = document.obter_atendentes()
  assert atendentes[0]["vendas"] == 2
  assert atendentes[1]["vendas"] == 1

if __name__ == "__main__":
  test_adicao_e_duplicacao()
  test_registro_venda()
  print("Todos os testes passaram.")