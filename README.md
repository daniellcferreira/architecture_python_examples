# Arquiteturas de Software em Python — MVC, Document-View e Smart-View

![Python](https://img.shields.io/badge/Python-Linguagem-blue?style=flat-square&logo=python)
![Tkinter](https://img.shields.io/badge/Tkinter-Interface-orange?style=flat-square&logo=python)
![CLI](https://img.shields.io/badge/CLI-Interface-lightgrey?style=flat-square&logo=gnu-bash)

## Descrição
Este projeto implementa um **sistema de controle de vendas** baseado em diferentes abordagens de arquitetura e interface.  
Ele permite o registro de **atendentes** e contabiliza suas vendas, oferecendo múltiplas interfaces (Tkinter e CLI) e diferentes formas de visualização.

## Funcionalidades
- Adicionar atendentes.
- Impedir duplicação de nomes.
- Registrar vendas de forma incremental.
- Resetar todos os atendentes.
- Interfaces alternativas:
  - **Tkinter (GUI)**: interface gráfica interativa.
  - **CLI (Prompt)**: interface no terminal.
  - **Document View**: manipulação orientada a documentos.
  - **Smart View**: interface de visão inteligente.

---

## Estrutura do Projeto

### **1. MVC**
Arquitetura com separação em **Model, View e Controller**.
- `mvc/controller.py` → Lógica de controle, conecta Model e View.  
- `mvc/view_tk.py` → Interface gráfica com **Tkinter**.  
- `mvc/view_prompt.py` → Interface em linha de comando (CLI).  
- `mvc/app.py` → Ponto de entrada, inicializa a aplicação com a View escolhida.

### **2. Document View**
Implementa uma visão alternativa baseada em manipulação de **documentos**.
- `document-view/document.py` → Lógica do documento.  
- `document-view/document_test.py` → Testes automatizados.  
- `document-view/app.py` → Aplicação principal.

### **3. Smart View**
Apresenta uma forma de visualização inteligente dos dados.
- `smart-view/app.py` → Ponto de entrada para a aplicação Smart View.

---