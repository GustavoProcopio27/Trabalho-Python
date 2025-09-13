from enum import Enum
from app.ui.tabulate_data import tabulate
from app.models.estatisticas import Estatisticas
from app.models.estacao import EstacaoMeteorologica
from app.models.registro import RegistroMetereologico
from datetime import date

class TerminalUI(Enum):
    MENU_SELECTORS:str = (
                        "=============== MENU ==================== \n"      
                        "1. Carregar arquivos da pasta \n"                  
                        "2. Exibir dados da(s) estação(ões)\n"              
                        "3. Exibir estatísticas (média, máximo etc.)\n"                                             
                        "4. Filtrar dados por data\n"                          
                        "5. Exportar relatório\n"                           
                        "6. Sair\n"
                        
                    ) 
    
    YEAR_CHOOSER:str = (
                    "=============== OPÇÕES ==================== \n"
                    "1. Dados de 2020\n"        
                    "2. Dados de 2021\n"
                    "3. Dados de 2022\n"
                    "4. Dados de 2023\n"
                    "5. Dados de 2024\n"
                   )   
    
    NUMBER_SELECTOR:str = (
                    "=============== OPÇÕES ==================== \n"
                    "1. Todas estações\n"
                    "2. Única estação\n"
                    )
    
def show_main_menu():
    print(TerminalUI.MENU_SELECTORS.value)

def show_folder_chooser_menu():
    print(TerminalUI.YEAR_CHOOSER.value)
    
def show_stations_quantity_chooser_menu():
    print(TerminalUI.NUMBER_SELECTOR.value)    
    

    
def show_estacoes(estacoes:list[EstacaoMeteorologica]):
    for estacao in estacoes:
        print(estacao) 
        registros:list[RegistroMetereologico] = estacao.registros
        print(tabulate(registros))    
        
        
        
def show_statisticas(estacoes:list[EstacaoMeteorologica]):
    if not estacoes:
        print("Nenhuma estacao encontrada")    
    for estacao in estacoes:
        print(estacao)
        estatisticas:Estatisticas=Estatisticas(estacao.registros)
        print("\n * Estatisticas da estação:\n")
        print(estatisticas)
    
        
def show_estacoes_data(estacoes:list[EstacaoMeteorologica],inicio:date,fim:date):
    for estacao in estacoes:
        print(estacao) 
        registros:list[RegistroMetereologico] = estacao.registros
        registros:list[RegistroMetereologico]=[registro for registro in registros if registro.data>=inicio and registro.data<fim]
        print(tabulate(registros))              