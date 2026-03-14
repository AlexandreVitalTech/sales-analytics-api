import csv
from datetime import datetime
from pathlib import Path
def carregar_venda():
    base_lib = Path(__file__).resolve().parent.parent
    csv_loc = base_lib / "data" / "data.csv"  
    dados = []
    with open(csv_loc, 'r') as file:
     readCsv = csv.reader(file)
     next(readCsv)
     for line in readCsv:
            venda = {
                "id": int(line[0]),
                "data": datetime.strptime(line[1], "%Y-%m-%d").date(),
                "cliente": line[2],
                "cidade": line[3],
                "produto": line[4],
                "categoria": line[5],
                "quantidade": int(line[6]),
                "preco": float(line[7]),
                "desconto": float(line[8]),
                "pagamento": line[9],
                "canal": line[10]
            }
            dados.append(venda)
    return dados