import os
import random
import platform
import shutil
from colorama import init, Fore

init()

def clear_console():
    
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def cargar_archivo():
    
    ruta_archivo = input("Introduce la ruta al archivo o directorio que deseas poner en juego: ")
    if not os.path.exists(ruta_archivo):
        print(Fore.RED + "El archivo/directorio no existe." + Fore.RESET)
        return None
    return ruta_archivo

def jugar_ruleta(archivo):
    
    NUMERO_MUERTE = random.randint(1, 10)
    MENSAJES = [
        "¡Ups! Parece que te estas arriesgando, pero tal vez deberías rendirte.",
        "¿Seguro que quieres seguir jugando? Rendirte es una opción también.",
        "¡Cuidado! Esto se está poniendo peligroso. ¿Quizás quieres rendirte?",
        "Todavía tienes tiempo para rendirte. No esperes demasiado tarde."
    ]
    
    intentos = 0
    while intentos < 4:
        mensaje = random.choice(MENSAJES)

        seleccion = input("Elige un número del 1 al 10: ")
        try:
            seleccion = int(seleccion)
            if seleccion < 1 or seleccion > 10:
                print(Fore.RED + "Número fuera de rango. Debe ser entre 1 y 10." + Fore.RESET)
                continue
        except ValueError:
            print(Fore.RED + "Entrada inválida. Debes ingresar un número entero." + Fore.RESET)
            continue

        if seleccion == NUMERO_MUERTE:
            print(Fore.RED + "¡Has perdido! El archivo/directorio ha sido eliminado." + Fore.RESET)
            delete_file(archivo)
            return False
        else:
            print(Fore.YELLOW + mensaje + Fore.RESET)
        intentos += 1

    print(Fore.GREEN + "¡Has ganado esta ronda!" + Fore.RESET)
    return True

def delete_file(filename):
   
    try:
        if os.path.isfile(filename):
            os.remove(filename)
            print(f"¡El archivo '{filename}' ha sido eliminado!")
        elif os.path.isdir(filename):
            shutil.rmtree(filename)
            print(f"¡El directorio '{filename}' ha sido eliminado!")
    except Exception as e:
        print(f"No se pudo eliminar '{filename}': {e}")

def menu_print():
    
    clear_console()
    print("""
     +____________________/\\/__ / /|
   .'' ._____________'._____      / /|/\\
  : () :              :\ ----\|    \ )
   '..'______________.'0|----|      \\
                    0_0/____/        \\
                        |----    /----\\
                       || -\\ --|      \\
                       ||   || ||\\      \\
                        \\____// '|      \\
Bang! Bang!                     .'/       |
                               .:/        |
                               :/_________|\\
   """)
    archivo = cargar_archivo()
    if archivo:
        while True:
            if not jugar_ruleta(archivo):
                break
            opcion = input("¿Quieres seguir jugando? (s/n): ").lower()
            if opcion != 's':
                break

if __name__ == "__main__":
    while True:
        menu_print()
        opcion_salir = input("¿Quieres salir del juego? (s/n): ").lower()
        if opcion_salir == 's':
            print("¡Gracias por jugar! ¡Hasta luego!")
            break
