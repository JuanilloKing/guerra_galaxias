"""
Lado cliente de la aplicación La Guerra de las Galaxias (2026).
Este módulo gestiona la creación del reino y la comunicación con el servidor.
"""
import socket
import json
import clases.reino as reino
from clases.nave import EstrellaMuerte, Ejecutor, HalconMilenario, NaveRealNaboo, CazaEstelarJedi
from clases.mandaloriano import MandalorianoNivel1, MandalorianoNivel2, MandalorianoNivel3, MandalorianoNivel4, MandalorianoNivel5
import sys as sys
try:
    from tabulate import tabulate
except ImportError:
    print("\n⚠️ATENCIÓN⚠️, Parece que no tienes la librería tabulate instalada en python")
    print("No te preocupes es sencillo instalarla")
    print("Simplemente ejecuta el siguiente comando en tu terminal:")
    print("pip install tabulate")
    sys.exit(1)

HOST = '127.0.0.1' #PONER LA IP DEL SERVIDOR SI SE VA A EJECUTAR POR RED
PUERTO = 5000
LIMITE_CREDITOS = 50000

def configurar_reino():
    """Muestra el menú principal y gestiona la configuración del reino."""
    nombre_reino = input("Ingrese el nombre del reino: ")
    reino_actual = reino.Reino(nombre_reino)
    print(f"Reino '{nombre_reino}' creado exitosamente.")

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar Naves")
        print("2. Agregar Mandalorianos")
        print("3. Ver Reino y Enviar")
        print("4. Salir\n")
        print(f"Créditos gastados: {reino_actual.creditos_gastados} / {LIMITE_CREDITOS}\n")

        opcion = input("Seleccionar opción: ")


        if opcion == "1":
            if not reino_actual:
                print("Error: Primero debes crear un reino (Opción 1).")
                continue
            gestionar_naves(reino_actual)

        elif opcion == "2":
            if not reino_actual:
                print("Error: Primero debes crear un reino (Opción 1).")
                continue
            gestionar_mandalorianos(reino_actual)

        elif opcion == "3":
            if not reino_actual:
                print("No hay datos para mostrar.")
            else:
                mostrar_reino(reino_actual)
                confirmar = input("¿Deseas enviar estos datos al servidor? (s/n): ")
                if confirmar.lower() == 's':
                    enviar_al_servidor(reino_actual)
                    break

        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

def gestionar_naves(reino_obj):
    """Submenú para la selección de naves."""
    mostrar_catalogo_naves()
    opc = input("Selecciona nave: ")

    tipo_nave = {
        "1": EstrellaMuerte,
        "2": Ejecutor,
        "3": HalconMilenario,
        "4": NaveRealNaboo,
        "5": CazaEstelarJedi
    }

    if opc in tipo_nave:
        try:
            cantidad = int(input("¿Cuántas unidades?: "))
            for _ in range(cantidad):
                nueva_nave = tipo_nave[opc]()
                if (reino_obj.creditos_gastados + nueva_nave.coste) > LIMITE_CREDITOS:
                    print(f"¡ALERTA! Límite de {LIMITE_CREDITOS} excedido.")
                    break
                reino_obj.agregar_nave(nueva_nave)
            print(f"Créditos actuales: {reino_obj.creditos_gastados}")
        except ValueError:
            print("Error: Introduce un número válido.")

def gestionar_mandalorianos(reino_obj):
    """Submenú para la selección de mandalorianos."""
    mostrar_catalogo_mandalorianos()
    opc = input("Selecciona el nivel de mandaloriano: ")

    tipo_mandaloriano = {
        "1": MandalorianoNivel1,
        "2": MandalorianoNivel2,
        "3": MandalorianoNivel3,
        "4": MandalorianoNivel4,
        "5": MandalorianoNivel5
    }

    if opc in tipo_mandaloriano:
        try:
            cantidad = int(input("¿Cuántas unidades?: "))
            for _ in range(cantidad):
                m_instancia = tipo_mandaloriano[opc]()
                if (reino_obj.creditos_gastados + m_instancia.coste) > LIMITE_CREDITOS:
                    print("¡ALERTA! Límite de créditos excedido.")
                    break
                reino_obj.agregar_mandaloriano(m_instancia)
        except ValueError:
            print("Error: Introduce un número válido.")

def mostrar_reino(reino_obj):
    """Muestra el estado actual del reino."""
    print(f"\n--- ESTADO DE: {reino_obj.nombre} ---")
    print(f"Naves: {len(reino_obj.naves)}")
    print(f"Mandalorianos: {len(reino_obj.mandalorianos)}")
    print(f"Coste Total: {reino_obj.creditos_gastados} / {LIMITE_CREDITOS}")

def enviar_al_servidor(reino_obj):
    """Serializa y envía los datos al servidor central."""
    datos = {
        "nombre": reino_obj.nombre,
        "naves": [vars(n) for n in reino_obj.naves],
        "mandalorianos": [vars(m) for m in reino_obj.mandalorianos],
        "coste_total": reino_obj.creditos_gastados
    }

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
            cliente_socket.connect((HOST, PUERTO))
            mensaje = json.dumps(datos)
            cliente_socket.sendall(mensaje.encode('utf-8'))
            print("☑ Configuración enviada. ¡Esperando inicio de guerra!")
    except ConnectionRefusedError:
        print("X Error: Servidor no disponible.")
    except Exception as e:
        print(f"X Error inesperado: {e}")

def mostrar_catalogo_naves():
    """
    Muestra una tabla con todas las naves disponibles y sus estadísticas base.
    """

    tipos_naves = [
        CazaEstelarJedi(),
        NaveRealNaboo(),
        HalconMilenario(),
        Ejecutor(),
        EstrellaMuerte()
    ]

    tabla = []

    i = 5
    for nave in tipos_naves:
        tabla.append([
            i,
            nave.nombre,
            nave.vida,
            nave.ataque,
            nave.defensa,
            nave.velocidad,
            nave.coste
        ])
        i -= 1

    encabezados = ["OPCIÓN", "NAVE", "VIDA", "ATAQUE", "DEFENSA", "VELOCIDAD", "COSTE"]

    print("\n🚀 CATÁLOGO DE NAVES 🚀\n")
    print(tabulate(tabla, headers=encabezados, tablefmt="fancy_grid"))
    print()
    
def mostrar_catalogo_mandalorianos():
    """
    Muestra una tabla con todas los mandalorianos disponibles y sus estadísticas base.
    """

    tipos_mandalorianos = [
        MandalorianoNivel5(),
        MandalorianoNivel4(),
        MandalorianoNivel3(),
        MandalorianoNivel2(),
        MandalorianoNivel1()
    ]

    tabla = []

    i = 5
    for mandaloriano in tipos_mandalorianos:
        tabla.append([
            i,
            mandaloriano.nombre,
            mandaloriano.vida,
            mandaloriano.ataque,
            mandaloriano.defensa,
            mandaloriano.velocidad,
            mandaloriano.coste
        ])
        i -= 1

    encabezados = ["OPCIÓN", "MANDALORIANO", "VIDA", "ATAQUE", "DEFENSA", "VELOCIDAD", "COSTE"]

    print("\n🥷 CATÁLOGO DE MANDALORIANOS 🥷\n")
    print(tabulate(tabla, headers=encabezados, tablefmt="fancy_grid"))
    print()

if __name__ == "__main__":
    configurar_reino()
