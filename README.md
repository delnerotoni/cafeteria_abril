# ☕ Cafeteria Abril

📊 **Análise exploratória de consumo em cafeteria (Abril 2023)**  
Este projeto tem como objetivo analisar o comportamento de consumo dos clientes de uma cafeteria durante o mês de abril, identificando padrões de compra, impacto de promoções e perfil dos clientes.

---

## 📂 Estrutura do Projeto

- 📁 **data/** → bases de dados (CSV, brutos ou tratados)  
- 📓 **notebooks/** → análises exploratórias em Jupyter  
- 🐍 **src/** → scripts Python reutilizáveis  
  - 🧹 `data_preprocessing.py` → funções de limpeza e transformação  
  - 📊 `visualization.py` → funções de gráficos e visualizações  
  - 🛠️ `utils.py` → utilitários gerais (carregar/salvar dados, helpers)  
- 📑 **reports/** → relatórios finais e dashboards consolidados  
  - 📝 `relatorio_exploratorio.md` → insights e descobertas  
- 📈 **dashboard/** → gráficos gerados automaticamente  
- 📦 **requirements.txt** → dependências do projeto  
- 📘 **README.md** → documentação do projeto  
- 🚫 **.gitignore** → arquivos/pastas ignorados pelo Git  

---

## 📊 Principais análises realizadas

- ✅ Ticket médio geral: cálculo do gasto médio por cliente  
- ✅ Distribuição de valores de compra: histograma e análise de dispersão  
- ✅ Impacto de promoções: comparação de ticket médio em dias com e sem promoção  
- ✅ Segmentação por faixa etária: análise de comportamento de consumo por idade  
- ✅ Turnos (manhã vs tarde): comparação de volume de vendas e ticket médio  
- ✅ Clientes frequentes vs ocasionais: diferenças de comportamento de consumo  

---

## 📈 Exemplos de visualizações

- 📊 Ticket médio por dia da semana  
- 🌞 vs 🌙 Ticket médio por turno (manhã/tarde)  
- 📉 Distribuição de valores de compra  
- 🎯 Comparação de consumo em dias com e sem promoção  

*(As figuras finais ficam salvas em `dashboard/` e `reports/`.)*

---

## 🛠️ Tecnologias utilizadas

- 🐍 **Python 3.10+**  
- 🗂️ **Pandas** → manipulação de dados  
- 📊 **Seaborn & Matplotlib** → visualizações  
- 📓 **Jupyter Notebook** → análises exploratórias  
- 🌐 **Git & GitHub** → versionamento e portfólio  

---

## 📌 Próximos passos

- 🔮 Criar modelos preditivos para estimar ticket médio  
- 📅 Avaliar sazonalidade (dias da semana, feriados)  
- 📊 Construir dashboard interativo (Streamlit ou Power BI)  
- 📝 Documentar insights finais em relatório executivo  

---

## 👨‍💻 Autor

Projeto desenvolvido por **Tony**  
📬 Contato: **delnerotoni@gmail.com**  
🌐 GitHub: [github.com/delnerotoni](https://github.com/delnerotoni)

---

## 🚀 Como rodar o projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/delnerotoni/cafeteria_abril.git
   cd cafeteria_abril


