from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.analysis import (
    analise_canal,
    analise_pagamento,
    produto_extremo_vendido,
    ticket_medio,
    total_vendas,
    vendas_por_categ,
    vendas_por_cidade,
)
from src.reader import carregar_venda

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"mensagem": "Olá, FastAPI!"}


@app.get("/total")
def total():
    dados = carregar_venda()
    return {"total_vendas": total_vendas(dados)}


@app.get("/ticket")
def ticket():
    dados = carregar_venda()
    return {"ticket_medio": ticket_medio(dados)}


@app.get("/categoria")
def categoria() -> Dict[str, int]:
    dados = carregar_venda()
    return vendas_por_categ(dados)


@app.get("/cidade")
def cidade() -> Dict[str, int]:
    dados = carregar_venda()
    return vendas_por_cidade(dados)


@app.get("/ext_max")
def ext_max() -> Dict[str, int]:
    dados = carregar_venda()
    return produto_extremo_vendido(dados, max)


@app.get("/ext_min")
def ext_min() -> Dict[str, int]:
    dados = carregar_venda()
    return produto_extremo_vendido(dados, min)


@app.get("/canal")
def canal() -> Dict[str, int]:
    dados = carregar_venda()
    return analise_canal(dados)


@app.get("/pagamento")
def pagamento() -> Dict[str, int]:
    dados = carregar_venda()
    return analise_pagamento(dados)
