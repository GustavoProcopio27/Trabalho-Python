from ui.terminal import print_main_menu,print_folder_chooser_menu
from time import sleep

def main():
    while True:
        print_main_menu()

        option=int(input("--------------- Escolha uma opção ---------------:\n"))
        print("\n")
        match option:
            case 1:
                print_folder_chooser_menu()
                opcao=int(input("--------------- Escolha uma opção ---------------:\n"))
                print("\n")                
                
            case 2:
                pass

            case 6:
                print("Saindo da aplicação...")
                sleep(1)
                break
            case _:
                print("Opção invalida, retornando...")
                sleep(1)

                break



if __name__ == "__main__":
    main()
