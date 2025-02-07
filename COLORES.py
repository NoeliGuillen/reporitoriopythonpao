
from colorama import init, Fore, Back, Style
init()

while True: 
    print(f"{Fore.RED}Universidad Victori.")
    print(f"{Fore.RED}Control Escolar")
    nombre=input(f"{Fore.CYAN}Digita el nombre del alumno: ") 
    while True:
        unocali=float(input("Digita la primera calificación: "))
        if (unocali <1 or unocali > 10):
            print(f"Error: Debes ingresar un número valido")
            continue
        break
    while True:
        doscali=float(input(f"{Fore.WHITE}Digita la segunda calificación: "))
        if (doscali <1 or doscali > 10):
            print(f"{Fore.WHITE}Error: Debes ingresar un número valido")
            continue
        break
    while True: 
        trescali=float(input(f"{Fore.WHITE}Digita la tercera calificación: "))
        if (trescali <1 or  trescali > 10):
            print(f"{Fore.WHITE}Error: Debes ingresar un número valido")
            continue
        break
    promedio= (unocali+doscali+trescali)/3; 
    print(f"{Fore.WHITE}\nEl alumno {nombre}")
    print(f"{Fore.RED}\b  Su primera calificación fue: {unocali}")
    print(f"{Fore.GREEN}\b  Su segunda calificación fue: {doscali}")
    print(f"\b {Fore.YELLOW} Su tercera calificación fue: {trescali}")
    print(f"\b  {Fore.BLACK}Obtuvo un promedio de {promedio} puntos")
    resp = input("\n¿Quieres hacer otra conversión? (s/n): ").strip().lower()
    if resp != "s":
        print("Gracias por usar el conversor. ¡Hasta luego!")
        break