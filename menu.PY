import os
import platform

def mostrar_menu():
    print("Seleccione la ecuación que desea ejecutar:")
    print("1. Ecuación 1")
    print("2. Ecuación 2")
    print("3. Ecuación 3")
    print("4. Ecuación 4")
    print("5. Ecuación 5")
    print("6. Ecuación 6")
    print("7. Ecuación 7")
    print("8. Ecuación 8")
    print("9. Salir")

def ejecutar_ecuacion(ecuacion):
    os.system(f'python {ecuacion}.py')

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción: ")

    if opcion in [str(i) for i in range(1, 9)]:
        ejecutar_ecuacion(f"ecuacion{opcion}")
        input("Presione Enter para continuar...")
        limpiar_pantalla()
    elif opcion == "9":
        print("Saliendo...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
