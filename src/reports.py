def sintetizar_relatorio(dados):
    relatorio = {
        "total_vendido": total_vendas(dados),
        "ticket": ticket_medio(dados),
        "vendas_categoria": vendas_por_categ(dados),
        "vendas_cidade": vendas_por_cidade(dados),
        "produto_mais_vendido": produto_extremo_vendido(dados, max),
        "produto_menos_vendido": produto_extremo_vendido(dados, min),
        "analise_canal": analise_canal(dados),
        "analise_pagamento": analise_pagamento(dados)
    }
    return relatorio

def exibir_relatorio(titulo, dicionario):
    print("\n", titulo)
    for nome, quant in dicionario.items ():
        print("-", nome, ":", quant)
    
def gerar_relatorio():
    relatorio = sintetizar_relatorio(dados)
    print("======== RELATÓRIO DE VENDAS ======== \n")
    print("\n Total vendido: R$" + str(round(relatorio["total_vendido"], 2)))
    print("\n Ticket médio: R$" + str(relatorio["ticket"]))
    exibir_relatorio(
        "\n Vendas por categoria",
        relatorio["vendas_categoria"]
    )
    exibir_relatorio(
        "Vendas por cidade",
        relatorio["vendas_cidade"]
    )
    exibir_relatorio(
        "\n Produto mais vendido",
        relatorio["produto_mais_vendido"]
    )
    exibir_relatorio(
        "Produtos menos vendidos",
        relatorio["produto_menos_vendido"]
    )
    print("\n \n ======== LEVANTAMENTOS ======== \n")
    exibir_relatorio(
        "\n Métodos de pagamento",
        relatorio["analise_pagamento"]
    )
    exibir_relatorio(
        "Locais de compra",
        relatorio["analise_canal"]
    )
    gerar_relatorio()