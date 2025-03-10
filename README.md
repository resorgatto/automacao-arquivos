# 📂 Automação de Extração e Renomeação de Arquivos

Este projeto permite a **extração automática de arquivos ZIP e RAR** utilizando o **WinRAR** e a **renomeação de arquivos PDF** seguindo um padrão baseado em datas e informações contidas no nome do arquivo.

---

## 📌 **Funcionalidades**
✅ **Extração de Arquivos**: Suporta extração de arquivos `.zip` e `.rar` automaticamente.  
✅ **Renomeação Inteligente**: Renomeia arquivos PDF com base em datas e informações extraídas do nome original.  
✅ **Interface Gráfica Simples**: Utiliza **Tkinter** para seleção de arquivos/pastas e exibição de mensagens ao usuário.  
✅ **Detecção Automática do WinRAR**: Identifica a instalação do WinRAR no sistema para extração de arquivos `.rar`.

---

## 📂 **Estrutura do Projeto**
```
📁 AutomacaoNotas
│-- automacao.py  # Código principal
│-- README.md     # Documentação do projeto
```

---

## 🔧 **Pré-requisitos**
Antes de executar o script, certifique-se de ter:

1. **Python 3.x** instalado.
2. **Bibliotecas necessárias** (instaláveis com o comando abaixo):
   ```bash
   pip install tk
   ```
3. **WinRAR instalado** (caso precise extrair arquivos `.rar`).

---

## 🚀 **Como Usar**
### 1️⃣ Executar o Script
No terminal ou CMD, navegue até a pasta do projeto e execute:
```bash
python automacao.py
```

### 2️⃣ Selecionar Arquivo ou Pasta
O programa abrirá uma interface para selecionar:
- Um **arquivo ZIP ou RAR** para extração e renomeação.
- Uma **pasta contendo PDFs** para renomeação automática.

### 3️⃣ Processamento
- Se for um **arquivo ZIP/RAR**, ele será extraído e os PDFs serão renomeados automaticamente.
- Se for uma **pasta com PDFs**, apenas a renomeação será feita.

---

## ⚠ **Possíveis Problemas e Soluções**
### 🔴 **WinRAR não encontrado**
- Certifique-se de que o **WinRAR está instalado**.
- Caso esteja instalado em um diretório diferente, atualize a função `find_winrar()` no código.

### 🔴 **Erro ao Extrair Arquivo RAR**
- Execute o comando abaixo para verificar se o WinRAR está acessível pelo terminal:
  ```bash
  where winrar
  ```
- Se não encontrar, adicione o caminho manualmente no `find_winrar()`.

### 🔴 **Problemas na Renomeação de Arquivos**
- O script depende de **datas e padrões no nome do arquivo** para renomear corretamente.
- Verifique se os arquivos seguem um padrão esperado (ex: `01.10.2023 - Nome do Arquivo.pdf`).

---

## 🛠 **Personalizações**
Caso precise modificar o script:
- **Alterar o padrão de renomeação**: Modifique a função `rename_pdfs()`.
- **Adicionar suporte para outros formatos de arquivo**: Edite a função `extract_archive()`.

---

## 📜 **Licença**
Este projeto é de código aberto e pode ser modificado e distribuído livremente.

---

## 💡 **Dúvidas ou Sugestões?**
Fique à vontade para contribuir com melhorias ou abrir issues no repositório!

🚀 **Happy Coding!**

