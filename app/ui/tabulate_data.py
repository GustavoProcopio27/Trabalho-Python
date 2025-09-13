from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.registro import RegistroMetereologico
from time import sleep
def tabulate(data:list["RegistroMetereologico"])->None:
    formated_data=list()
    for row in data:
        data, hora, temperatura, umidade, precipitacao = row.tolist()
        linha_formatada:list[str] = [
            f"{str(data):<15}",                   # data: até 15 caracteres (sobrando)
            f"{hora:<10}",                    # hora: até 10, suficiente pra "2300 UTC"
            f"{float(temperatura):>10.2f}",   # temperatura: até 10, com 2 casas decimais
            f"{float(umidade):>10.2f}",       # umidade: idem
            f"{float(precipitacao):>16.2f}",  # precipitacao: maior ainda
        ]
        formated_data.append(linha_formatada)

    # Cabeçalhos com mesmo espaçamento
    headers:list[str] = [
        f"{'data':<15}",
        f"{'hora':<10}",
        f"{'temperatura':>10}",
        f"{'umidade':>10}",
        f"{'precipitacao':>15}"
    ]

    # Separador bonitinho
    print("=" * 77)
    print("| " + " | ".join(headers) + " |")
    print("=" * 77)

    # Linhas de dados
    for row in formated_data:
        print("| " + " | ".join(row) + " |")
        sleep(0.001)

    print("=" * 77)
    
