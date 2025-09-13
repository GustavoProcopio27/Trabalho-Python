from functools import wraps
from app.ui.terminal import show_main_menu
from time import sleep
from os import name, system
def main_ruuner():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                show_main_menu()
                try:
                    option=int(input("--------------- Escolha uma opção ---------------:\n"))
                    print("\n")
                except Exception:
                    print("t Opção escolhida é invalida, saindo da aplicação...")
                    sleep(1)
                    if name == 'nt':
                        system('cls')
                    else:
                        system('clear')
                saida = func(option, *args, **kwargs)
                if saida:
                    break
                
        return wrapper
    return decorator