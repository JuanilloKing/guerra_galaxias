"""Lado cliente de la aplicación"""
import socket
import json
import clases.reino as reino
import clases.nave as nave
import clases.mandaloriano as mandaloriano

def jugar():
    """Función que inicia el juego"""
    print("=== SERVIDOR - LA GUERRA DE LAS GALAXIAS (2026) ===")
    print("1. Iniciar Guerra")
    print("2. Finalizar Servidor")
    print("Seleccionar opción para continuar:")

def mostrar_menu():
    """Función que muestra el menú principal del juego"""
    print("=== MENÚ PRINCIPAL ===")
    print("1. Crear Reino")
    print("2. Agregar Nave")
    print("3. Agregar Mandaloriano")
    print("4. Ver Reino")
    print("5. Salir")
    print("Seleccionar opción para continuar:")
    opcion = input()
    if opcion == "1":
        nombre_reino = input("Ingrese el nombre del reino: ")
        reino_actual = reino.Reino(nombre_reino)
        print(f"Reino '{nombre_reino}' creado exitosamente.")
    elif opcion == "2":
        print("Elige que nave quieres agregar:")
        print("1. Estrella de la Muerte")
        print("2. Ejecutor")
        print("3. Halcon Milenario")
        print("4. Nave Real de Naboo")
        print("5. Caza estelar jedi")
        opcion = input()
        if opcion == "1":
            nave_actual = nave.EstrellaMuerte
        if opcion == "2":
            nave_actual = nave.Ejecutor
        if opcion == "3":
            nave_actual = nave.HalconMilenario
        if opcion == "4":
            nave_actual = nave.NaveRealNaboo
        if opcion == "5":
            nave_actual = nave.CazaEstelarJedi
        if reino_actual:
            reino_actual.agregar_nave()
        else:
            print("Primero debes crear un reino.")
    elif opcion == "3":
        print("Agregando mandaloriano...")
    elif opcion == "4":
        print("Viendo reino...")
    elif opcion == "5":
        print("Saliendo del juego.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
