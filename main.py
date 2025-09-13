from app.ui.terminal import show_folder_chooser_menu,show_estacoes,show_statisticas,show_estacoes_data
from app.utils.export_data import exportar_relatorio
from app.utils.decorators import main_ruuner
from app.utils.file_reader import Reader
from app.utils.exceptions import BreakCase
from datetime import date,datetime
from time import sleep
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.estacao import EstacaoMeteorologica
    
estacoes:list["EstacaoMeteorologica"]=list()
    
@main_ruuner()
def main(option):

    global estacoes
    
    match option:

        case 1:
            show_folder_chooser_menu()

            opcao=int(input("--------------- Escolha uma opção ---------------:\n"))
            print("\n")    
            estacoes+=Reader.read_csv(opcao)
     
                     
        case 2:
            if not estacoes:
                raise BreakCase()
            show_estacoes(estacoes)

        case 3:
            if not estacoes:
                raise BreakCase()

            
            # Estatisticas de uma estacao
            
            
            # Estatisticas de tudo
            show_statisticas(estacoes)    
                
         
        
        case 4:
            
            
            
            # Filtrar registros de todas estacoes por data
            inicio= input("Data inicial:")
            fim=input("Data final:")
            
            try:
                inicio,fim=datetime.strptime(inicio,"%Y/%m/%d").date(),datetime.strptime(fim,"%Y/%m/%d").date()
            except Exception as ex:
                print(f"formato invalido: {ex}")
            
            show_estacoes_data(estacoes,inicio,fim)    
        
        
        case 5:
            
        # Exportando relatorio com todas
            exportar_relatorio(estacoes)
        
        
        
        case 6:
            print("Saindo da aplicação...")
            sleep(1)
            return True 
        
        case _:
            print("Opção invalida, retornando...")
            sleep(1)




if __name__ == "__main__":
    main()
