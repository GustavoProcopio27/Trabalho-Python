from app.ui.terminal import show_folder_chooser_menu
from app.ui.tabulate_data import tabulate

from app.utils.decorators import main_ruuner
from app.utils.file_reader import Reader
from app.utils.logging_config import configurar_logging
from app.utils.exceptions import BreakCase
from time import sleep
from typing import TYPE_CHECKING
import logging 
if TYPE_CHECKING:
    from app.models.estacao import EstacaoMeteorologica
    from app.models.registro import RegistroMetereologico
    
estacoes:list["EstacaoMeteorologica"]=list()
    
@main_ruuner()
def main(option):
    configurar_logging()
    logger=logging.getLogger(__name__)
    
    global estacoes
    
    match option:

        case 1:
            show_folder_chooser_menu()

            opcao=int(input("--------------- Escolha uma opção ---------------:\n"))
            print("\n")    
            estacoes=Reader.read_csv(opcao)
     
                     
        case 2:
            if not estacoes:
                raise BreakCase()
            for estacao in estacoes:
                print(estacao) 
                registros:list["RegistroMetereologico"] = estacao.get_registers()
                print(tabulate(registros))

        case 3:
            pass
        
        
        case 4:
            pass
        
        
        case 5:
            pass
        
        
        
        
        case 6:
            print("Saindo da aplicação...")
            sleep(1)
            return True 
        
        case _:
            print("Opção invalida, retornando...")
            sleep(1)




if __name__ == "__main__":
    main()
