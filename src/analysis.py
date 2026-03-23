def total_vendas(dados):
     total = 0
     for venda in dados:
        preco = venda["preco"]
        quantidade = venda["quantidade"]
        total += round(preco * quantidade, 2)
     return total

def vendas_por_categ(dados):
        vendas_categ = {}
        for venda in dados:
                categoria = venda["categoria"]
                quantidade = venda["quantidade"]
                if categoria in vendas_categ:
                        vendas_categ[categoria] += quantidade
                else:
                        vendas_categ[categoria] = quantidade
        return vendas_categ

def vendas_por_cidade(dados):
        vendas_cidade = {}
        for venda in dados:
                cidade = venda["cidade"]
                quantidade = venda["quantidade"]
                if cidade in vendas_cidade:
                        vendas_cidade[cidade] += quantidade
                else:
                        vendas_cidade[cidade] = quantidade
        return vendas_cidade

def produto_extremo_vendido(dados, tipo):
        param = tipo
        vendas_produto = {}
        for venda in dados:
                produto = venda["produto"]
                quantidade = venda["quantidade"]
                if produto not in vendas_produto:
                        vendas_produto[produto] = 0
                vendas_produto[produto] += quantidade    
        extremo = param(vendas_produto.values())
        extremo_vendido = {}
        for produto, quant in vendas_produto.items():
                if quant == extremo:
                        extremo_vendido[produto] = quant
        return extremo_vendido

def ticket_medio(dados):
        total = total_vendas(dados)
        quant_vendas = len(dados)
        ticket_medio = round(total / quant_vendas, 2)
        return ticket_medio    
        
def analise_canal(dados):
         quant_canal = {}
         for venda in dados:
                 canal = venda["canal"]
                 if canal in quant_canal:
                        quant_canal[canal] += 1
                 else:
                        quant_canal[canal] = 1
         return quant_canal

def analise_pagamento(dados):
         quant_pagamento = {}
         for venda in dados:
                 pagamento = venda["pagamento"]
                 if pagamento in quant_pagamento:
                        quant_pagamento[pagamento] += 1
                 else:
                        quant_pagamento[pagamento] = 1
         return quant_pagamento