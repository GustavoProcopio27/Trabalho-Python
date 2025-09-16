from app.ui.terminal import show_folder_chooser_menu,show_estacoes,show_statisticas,show_estacoes_data,show_stations_quantity_chooser_menu
from app.utils.export_data import exportar_relatorio
from app.utils.decorators import main_ruuner
from app.utils.file_reader import Reader
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
        ################################################################################
        #                           Ver Carregar dados                                 #
        ################################################################################
        case 1:
            show_folder_chooser_menu()
            try:
                opcao=int(input("--------------- Escolha uma opção ---------------:\n"))
            except ValueError:
                print("Opção invalida, retornando...")
                sleep(1)

                return False
            print("\n")   
             
            estacoes+=Reader.read_csv(opcao)
            print("Arquivos carregados com sucesso")
     
     
     
        ################################################################################
        #                                  Ver estacoes                                #
        ################################################################################                     
        case 2:
            if not estacoes:
                print("Nenhuma estacao disponivel, retornando...")
                sleep(1)

                return False
            
            show_stations_quantity_chooser_menu()
            
            try:
                escolha=int(input("--------------- Escolha uma opção ---------------:\n"))
            except ValueError:
                print('Opção invalida, retornando...')
                sleep(1)
                return False
            
            match escolha:
                case 1:
                    show_estacoes(estacoes)
                    
                case 2:
                    codigo:str=input("Entre com o codigo da estacao:")
                    estacao_escolhida=[estacao for estacao in estacoes if estacao.codigo==codigo]
                    show_estacoes(estacao_escolhida)
    
                
                case _:
                    show_estacoes(estacoes)






        ################################################################################
        #                              Ver estatisticas                                #
        ################################################################################
        case 3:
            if not estacoes:
                print('Opção invalida, retornando...')
                sleep(1)
                return False

            show_stations_quantity_chooser_menu()
            try:
                escolha=int(input("--------------- Escolha uma opção ---------------:\n"))
            except ValueError:
                print('Opção invalida, retornando...')
                sleep(1)
                return False
            
            match escolha:
                case 1:
                    show_statisticas(estacoes)
                    
                case 2:
                    codigo:str=input("Entre com o codigo da estacao")
                    estacao_escolhida=[estacao for estacao in estacoes if estacao.codigo==codigo]
                    show_statisticas(estacao_escolhida)
    
                
                case _:
                    show_statisticas(estacoes)              
                
        ################################################################################
        #                              Filtrar pela data                               #
        ################################################################################              
        case 4:
            
            # Filtrar registros de todas estacoes por data
            inicio= input("Data inicial:")
            fim = input("Data final:")
            
            try:
                inicio,fim=datetime.strptime(inicio,"%Y/%m/%d").date(),datetime.strptime(fim,"%Y/%m/%d").date()
            except Exception as ex:
                print(f"formato invalido: a expressão não bate no formato ano/mes/dia, retornando...")
                sleep(1)
                
                return False
                
            show_stations_quantity_chooser_menu()
            escolha=int(input("--------------- Escolha uma opção ---------------:\n"))
            match escolha:
                case 1:
                    show_estacoes_data(estacoes,inicio,fim) 
                    
                case 2:
                    codigo:str=input("Entre com o codigo da estacao")
                    estacao_escolhida=[estacao for estacao in estacoes if estacao.codigo==codigo]
                    show_estacoes_data(estacoes,inicio,fim) 
    
                
                case _:
                    show_estacoes_data(estacoes,inicio,fim)             
        
        ################################################################################
        #                            imprimir relatorio                                #
        ################################################################################        
        case 5:
            show_stations_quantity_chooser_menu()
            try:
                escolha=int(input("--------------- Escolha uma opção ---------------:\n"))
            except ValueError as ex:
                return False
            
            match escolha:
                case 1:
                    exportar_relatorio(estacoes) 
                    
                case 2:
                    codigo:str=input("Entre com o codigo da estacao")
                    estacao_escolhida=[estacao for estacao in estacoes if estacao.codigo==codigo]
                    exportar_relatorio(estacoes) 
    
                
                case _:
                    exportar_relatorio(estacoes)            
            
        ################################################################################
        #                              Sair da aplicação                               #
        ################################################################################        
        case 6:
            print("Saindo da aplicação...")
            sleep(1)
            return True 
        
        case _:
            print("Opção escolhida é invalida, retornando ao menu principal...")
            sleep(1)
            




if __name__ == "__main__":
    main()
