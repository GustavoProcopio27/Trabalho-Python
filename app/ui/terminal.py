from enum import Enum

class TerminalUI(Enum):
    MENU_SELECTORS = (
                        "=============== MENU ==================== \n"      
                        "1. Carregar arquivos da pasta \n"                  
                        "2. Exibir dados da(s) estação(ões)\n"              
                        "3. Exibir estatísticas (média, máximo etc.)\n"                                             
                        "4. Filtrar dados por data\n"                          
                        "5. Exportar relatório\n"                           
                        "6. Sair\n"
                        
                    ) 
    
    YEAR_CHOOSER = (
                    "1. Dados de 2020\n"        
                    "2. Dados de 2021\n"
                    "3. Dados de 2022\n"
                    "4. Dados de 2023\n"
                    "5. Dados de 2024\n"
                   )   
    
def show_main_menu():
    print(TerminalUI.MENU_SELECTORS.value)

def show_folder_chooser_menu():
    print(TerminalUI.YEAR_CHOOSER.value)