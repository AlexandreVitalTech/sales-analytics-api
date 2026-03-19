from fastapi import FastAPI
from src.reader import carregar_venda
from src.reports import sintetizar_relatorio
app = FastAPI()
dados = carregar_venda()
@app.get("/")
def root():
    return {"mensagem": "Olá, fastAPI!"}
"""
@app.get("/categoria")
def categoria():
    return {}
"""