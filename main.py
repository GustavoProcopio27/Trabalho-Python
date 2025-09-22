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
def main(option)->bool:

    global estacoes
    
    match option:
        ################################################################################
        #                           Ver Carregar dados                                 #
        ################################################################################
        case 1:
            show_folder_chooser_menu()
            try:
                opcao:int=int(input("--------------- Escolha uma opção ---------------:\n"))
            except ValueError:
                print("Opção invalida, retornando...")
                sleep(1)

                return False
            print("\n")   
             
            estacoes+=Reader.read_csv(opcao)
            print("Arquivos carregados com sucesso")
            print("Voltando ao menu principal")
            sleep(2)

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
                escolha:int=int(input("--------------- Escolha uma opção ---------------:\n"))
            except ValueError:
                print('Opção invalida, retornando...')
                sleep(1)
                return False
            
            match escolha:
                case 1:
                    show_estacoes(estacoes)
                    input("\nAperte ENTER para sair da visualização")
                case 2:
                    codigo:str=input("Entre com o codigo da estacao:")
                    estacao_escolhida:list["EstacaoMeteorologica"]=[estacao for estacao in estacoes if estacao.codigo==codigo]
                    if len(estacao_escolhida)==0:
                        print("Nenhuma estação encontrada com o codigo inserido")
                    show_estacoes(estacao_escolhida)
                    input("\nAperte ENTER para sair da visualização")

                
                case _:
                    show_estacoes(estacoes)
                    input("\nAperte ENTER para sair da visualização")






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
                escolha:int=int(input("--------------- Escolha uma opção ---------------:\n"))
            except ValueError:
                print('Opção invalida, retornando...')
                sleep(1)
                return False
            
            match escolha:
                case 1:
                    show_statisticas(estacoes)
                    input("\nAperte ENTER para sair da visualização")

                case 2:
                    codigo:str=input("Entre com o codigo da estacao:")
                    estacao_escolhida:list["EstacaoMeteorologica"]=[estacao for estacao in estacoes if estacao.codigo==codigo]
                    if len(estacao_escolhida)==0:
                        print("Nenhuma estação encontrada com o codigo inserido")
                    show_statisticas(estacao_escolhida)
                    input("\nAperte ENTER para sair da visualização")
                
                case _:
                    show_statisticas(estacoes)              
                    input("\nAperte ENTER para sair da visualização")
        ################################################################################
        #                              Filtrar pela data                               #
        ################################################################################              
        case 4:
            print("Entre com a data no formato ano/mes/dia \n Exemplo->2020/01/02")
            # Filtrar registros de todas estacoes por data
            inicio :str= input("Data inicial:")
            fim :str= input("Data final:")
            
            try:
                inicio,fim=datetime.strptime(inicio,"%Y/%m/%d").date(),datetime.strptime(fim,"%Y/%m/%d").date()
            except Exception:
                print(f"formato invalido: a expressão não bate no formato ano/mes/dia, retornando...")
                sleep(3)
                
                return False
                
            show_stations_quantity_chooser_menu()
            try:
                escolha=int(input("--------------- Escolha uma opção ---------------:\n"))
            except (ValueError,TypeError):
                return False
            match escolha:
                case 1:
                    show_estacoes_data(estacoes,inicio,fim) 
                    input("\nAperte ENTER para sair da visualização")
                case 2:
                    codigo:str=input("Entre com o codigo da estacao:")
                    estacao_escolhida:list["EstacaoMeteorologica"]=[estacao for estacao in estacoes if estacao.codigo==codigo]
                    if len(estacao_escolhida)==0:
                        print("Nenhuma estação encontrada com o codigo inserido")
                    show_estacoes_data(estacao_escolhida,inicio,fim) 
                    input("\nAperte ENTER para sair da visualização")
                
                case _:
                    show_estacoes_data(estacoes,inicio,fim)             
                    input("\nAperte ENTER para sair da visualização")
        ################################################################################
        #                            imprimir relatorio                                #
        ################################################################################        
        case 5:
            show_stations_quantity_chooser_menu()
            try:
                escolha:int=int(input("--------------- Escolha uma opção ---------------:\n"))
            except ValueError :
                return False
            
            match escolha:
                case 1:
                    exportar_relatorio(estacoes) 
                    
                case 2:
                    codigo:str=input("Entre com o codigo da estacao:")
                    estacao_escolhida:list["EstacaoMeteorologica"]=[estacao for estacao in estacoes if estacao.codigo==codigo]
                    if len(estacao_escolhida)==0:
                        print("Nenhuma estação encontrada com o codigo inserido")
                    exportar_relatorio(estacao_escolhida) 
    
                
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
            return False
            




if __name__ == "__main__":
    main()
