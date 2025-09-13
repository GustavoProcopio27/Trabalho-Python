from pathlib import Path
from io import StringIO
from app.models.estatisticas import Estatisticas
from app.models.estacao import EstacaoMeteorologica

def get_conteudo(estacoes:list[EstacaoMeteorologica]):
    conteudo=''
    for estacao in estacoes:
        conteudo+=estacao.__str__()
        estatisticas=Estatisticas(estacao.registros)
        conteudo+="\n * Estatisticas da estação:\n"
        conteudo+=f"{estatisticas.__str__()}"
    return conteudo 
  
def exportar_relatorio(estacoes):
    output=StringIO()
    
    output.write(get_conteudo(estacoes))
    output.seek(0)
    
    downloads_path=Path.home() / "Downloads"
    downloads_path.mkdir(exist_ok=True)
    
    arquivo=downloads_path / "relatorio.txt"
    
    try:
        with open(file=arquivo, mode="w",encoding="utf-8") as f:
            f.write(output.getvalue())
        print(f"Relatorio salvo em {arquivo}")
    except Exception as ex:
        print(f"erro: {ex}")
        print("Erro ocorrido ao salvar o arquivo")
    
    
