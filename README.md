<<<<<<< HEAD
Sistema fictício de visualização das estatísticas de venda de uma empresa fictícia. No momento, API desenvolvida. Pendente a implementação de interface
Base de dados usada para o desenvolvimento a nível de testes: data/data.csv
=======
# Sales Analytics API + Painel de Vendas

Sistema de visualização das estatísticas de venda de uma empresa fictícia.

- **Backend**: API em Python (FastAPI), lendo os dados de `data/data.csv`.
- **Frontend**: painel React (Vite) com gráficos em Recharts, na pasta `frontend/`.

## 1. Rodando o backend (API)

Dentro da pasta deste projeto (`sales-analytics-api-main`):

```bash
pip install fastapi uvicorn
uvicorn main:app --reload --port 8000
```

A API vai subir em `http://127.0.0.1:8000`. Endpoints disponíveis:

| Rota          | Retorno                                   |
|---------------|--------------------------------------------|
| `/total`      | total de vendas em R$                      |
| `/ticket`     | ticket médio em R$                         |
| `/categoria`  | quantidade vendida por categoria           |
| `/cidade`     | quantidade vendida por cidade              |
| `/ext_max`    | produto(s) mais vendido(s)                 |
| `/ext_min`    | produto(s) menos vendido(s)                |
| `/canal`      | vendas por canal (Loja / Online)           |
| `/pagamento`  | vendas por forma de pagamento              |

> Foi adicionado CORS (`CORSMiddleware`) para o front-end (rodando em outra porta) conseguir chamar a API sem bloqueio do navegador.

## 2. Rodando o front-end (painel)

Em outro terminal, entre na pasta `frontend/`:

```bash
cd frontend
npm install
npm run dev
```

O Vite vai indicar o endereço local, normalmente `http://localhost:5173`. Abra no navegador — com o backend já rodando na porta 8000, o painel carrega os dados automaticamente.

Se o backend rodar em outra porta/host, ajuste `API_BASE_URL` em `frontend/src/api.js`.

## 3. Estrutura do painel

- Cartão de resumo (estilo "recibo"): total de vendas, ticket médio, produto mais e menos vendido.
- Gráfico de barras: vendas por categoria.
- Gráfico de barras (horizontal): vendas por cidade.
- Gráfico de pizza: canal de venda (Loja x Online).
- Gráfico de barras: forma de pagamento.

## O que foi corrigido em relação à API original

- `/total` e `/ticket` retornavam um `set` Python (`{"texto", valor}`), o que não é uma estrutura JSON confiável. Agora retornam um dicionário (`{"total_vendas": ...}` / `{"ticket_medio": ...}`).
- Adicionado `CORSMiddleware` para permitir chamadas do front-end React.
>>>>>>> 1afe209 (projeto finalizado)
