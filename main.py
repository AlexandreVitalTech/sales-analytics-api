from fastapi import FastAPI
from typing import Dict, Optional
from src.reader import carregar_venda
from src.analysis import *
app = FastAPI()
dados = carregar_venda()
@app.get("/")
def root():
    return {"mensagem": "Olá, fastAPI!"}

@app.get("/total")
def total():
    resultado = total_vendas(dados)
    return {"Total de vendas:", resultado}

@app.get("/ticket")
def ticket():
    resultado = ticket_medio(dados)
    return {"Média de vendas:", resultado}

@app.get("/categoria")
def categoria() -> Dict[str, int]:
    resultado = vendas_por_categ(dados)
    return resultado

@app.get("/cidade")
def cidade() -> Dict[str, int]:
    resultado = vendas_por_cidade(dados)
    return resultado

@app.get("/ext_max")
def ext_max() -> Dict[str, int]:
    resultado = produto_extremo_vendido(dados, max)
    return resultado

@app.get("/ext_min")
def ext_min() -> Dict[str, int]:
    resultado = produto_extremo_vendido(dados, min)
    return resultado
@app.get("/canal")
def canal() -> Dict[str, int]:
    resultado = analise_canal(dados)
    return resultado
@app.get("/pagamento")
def pagamento() -> Dict[str, int]:
    resultado = analise_pagamento(dados)
    return resultado