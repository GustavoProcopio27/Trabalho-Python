from functools import wraps
from app.ui.terminal import show_main_menu
from time import sleep
from os import name, system

def main_ruuner():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                system('cls' if name == 'nt' else 'clear')
                show_main_menu()
                try:
                    option:int=int(input("--------------- Escolha uma opção ---------------:\n"))
                    print("\n")
                except Exception:
                    sleep(1)
                    option:int=7

                saida = func(option, *args, **kwargs)
                if saida:
                    break
                
        return wrapper
    return decorator