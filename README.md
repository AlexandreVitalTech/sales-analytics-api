# 📊 Sales Analytics API + Painel de Vendas

Sistema de análise e visualização de dados de vendas de uma empresa fictícia, com API própria em **FastAPI** e um painel interativo em **React**.

O projeto nasceu como um exercício prático de todo o ciclo de um produto de dados: leitura e tratamento de um CSV bruto, exposição via API REST, e visualização em gráficos no front-end.

---

## 🧱 Stack

**Backend**
- Python 3
- FastAPI
- Uvicorn (servidor ASGI)

**Frontend**
- React
- Vite
- Recharts (gráficos)

---

## ✨ Funcionalidades

O painel exibe, a partir dos dados de `data/data.csv`:

- 🧾 Resumo geral: total de vendas, ticket médio, produto mais vendido e menos vendido
- 📦 Vendas por categoria (gráfico de barras)
- 🏙️ Vendas por cidade (gráfico de barras horizontal)
- 🛒 Canal de venda — Loja x Online (gráfico de pizza)
- 💳 Forma de pagamento (gráfico de barras)

---

## 📁 Estrutura do projeto

```
sales-analytics-api-main/
├── main.py                # API FastAPI (rotas)
├── data/
│   └── data.csv           # Base de dados de vendas
├── src/
│   ├── reader.py          # Leitura/parsing do CSV
│   ├── analysis.py        # Regras de agregação dos dados
│   └── reports.py         # Geração de relatórios
└── frontend/
    ├── index.html
    ├── package.json
    └── src/
        ├── App.jsx         # Layout principal do painel
        ├── api.js          # Chamadas à API
        └── ...
```

---

## 🚀 Como rodar

### Pré-requisitos
- [Python 3.10+](https://www.python.org/)
- [Node.js 18+](https://nodejs.org/) (inclui o `npm`)

### 1. Backend (API)

Na raiz do projeto:

```bash
pip install fastapi uvicorn
uvicorn main:app --reload --port 8000
```

A API sobe em `http://127.0.0.1:8000`.

### 2. Frontend (painel)

Em outro terminal:

```bash
cd frontend
npm install
npm run dev
```

O Vite indicará o endereço local (normalmente `http://localhost:5173`). Com o backend rodando na porta 8000, o painel carrega os dados automaticamente.

> Se o backend rodar em outro host/porta, ajuste `API_BASE_URL` em `frontend/src/api.js`.

---

## 🔌 Referência da API

| Rota          | Descrição                                  |
|---------------|---------------------------------------------|
| `GET /total`     | Total de vendas em R$                     |
| `GET /ticket`    | Ticket médio em R$                        |
| `GET /categoria` | Quantidade vendida por categoria          |
| `GET /cidade`    | Quantidade vendida por cidade             |
| `GET /ext_max`   | Produto(s) mais vendido(s)                |
| `GET /ext_min`   | Produto(s) menos vendido(s)               |
| `GET /canal`     | Vendas por canal (Loja / Online)          |
| `GET /pagamento` | Vendas por forma de pagamento             |

CORS está habilitado (`CORSMiddleware`) para permitir chamadas do front-end a partir de outra porta.

---

## 🗺️ Possíveis próximos passos

- Filtro por período (data inicial/final)
- Autenticação para uso em produção
- Deploy do backend e do frontend

---

## 👤 Finalidade

Projeto pessoal de estudo, a fim de unir backend (Python + FastAPI), manipulação de dados (CSV) e frontend orientado a dados (React + Recharts).
