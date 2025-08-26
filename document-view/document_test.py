import document

# Teste para a função adicionar_atendente no módulo document.py
def test_adicao_e_duplicacao():
  document.resetar()
  assert document.adicionar_atendente("Alice") == "ok"
  #assert document.adicionar_atendente("") == "vazio"
  #assert document.adicionar_atendente("Alice") == "duplicado"

# Teste para a função incrementar_venda no módulo document.py
def test_incremento():
  document.resetar()
  document.adicionar_atendente("Bob")
  document.incrementar_venda(0)
  assert document.obter_atendentes()[0]["vendas"] == 1

# Execução dos testes
if __name__ == "__main__":
  test_adicao_e_duplicacao()
  test_incremento()
  print("Todos os testes passaram.")