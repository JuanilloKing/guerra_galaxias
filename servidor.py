"""
Gestiona la conexión de los reinos, la recepción de datos y la batalla
"""

import socket
import json
import clases.reino as reino

# Constantes del proyecto
HOST = '127.0.0.1'
PORT = 5000
TIEMPO_CONEXION = 20
MAX_CREDITOS = 100000

def mostrar_configuraciones(reino1_data, reino2_data):
    """
    Esta funcion mostrará por pantalla todos los datos y configuraciones de cada reino
    
    reino1_data(diccionario): Diccionario con los datos del reino1
    reino2_data(diccionario): Diccionario con los datos del reino2
    """
    
    #Conteo de naves y mandalorianos de ambos reinos
    tipos_de_nave = [
        "Estrella de la muerte",
        "Ejecutor",
        "Halcon Milenario",
        "Nave Real de Naboo",
        "Caza Estelar Jedi"
    ]
    tipos_de_mandalorianos = [
        "Nivel 1",
        "Nivel 2",
        "Nivel 3",
        "Nivel 4",
        "Nivel 5"
    ]
    
    conteo_naves_reino1 = contar_naves_por_tipo(tipos_de_nave, reino1_data)
    conteo_naves_reino2 = contar_naves_por_tipo(tipos_de_nave, reino2_data)
    
    conteo_mandalorianos_reino1 = contar_mandalorianos_por_tipo(tipos_de_mandalorianos, reino1_data)
    conteo_mandalorianos_reino2 = contar_mandalorianos_por_tipo(tipos_de_mandalorianos, reino2_data)
    
    #Mostrar configuraciones reino 1
    print("==========================================")
    print("📝 CONFIGURACIÓN REINO 1")
    print("==========================================")
    print(f"Nombre del reino: **{reino1_data['nombre']}**")
    for tipo_de_nave in tipos_de_nave:
        if conteo_naves_reino1[tipo_de_nave] >= 1:
            print(f"Número de Naves ({tipo_de_nave}): {conteo_naves_reino1[tipo_de_nave]}")
    for tipo_de_mandaloriano in tipos_de_mandalorianos:
        if conteo_mandalorianos_reino1[tipo_de_mandaloriano] >= 1:
            print(f"Número de Mandalorianos ({tipo_de_mandaloriano}): {conteo_mandalorianos_reino1[tipo_de_mandaloriano]}")
    print(f"Coste total: {reino1_data['coste_total']}")
    print()
    #Mostrar configuraciones reino 1
    print("==========================================")
    print("📝 CONFIGURACIÓN REINO 2")
    print("==========================================")
    print(f"Nombre del reino: **{reino2_data['nombre']}**")
    for tipo_de_nave in tipos_de_nave:
        if conteo_naves_reino2[tipo_de_nave] >= 1:
            print(f"Número de Naves ({tipo_de_nave}): {conteo_naves_reino2[tipo_de_nave]}")
    for tipo_de_mandaloriano in tipos_de_mandalorianos:
        if conteo_mandalorianos_reino2[tipo_de_mandaloriano] >= 1:
            print(f"Número de Mandalorianos ({tipo_de_mandaloriano}): {conteo_mandalorianos_reino2[tipo_de_mandaloriano]}")
    print(f"Coste total: {reino2_data['coste_total']}")
    print()
    
    return

def contar_naves_por_tipo(tipos, reino):
    """
    Cuenta cuántas naves de cada tipo posee un reino.

    Args:
        tipos (list): Lista con los nombres de los tipos de nave.
        reino (dict): Diccionario con toda la información del reino.

    Returns:
        dict: Diccionario con el tipo de nave como clave y la cantidad como valor.
    """
    conteo = {}
    for tipo in tipos:
        conteo[tipo] = sum(1 for nave in reino.get("naves", []) if nave.get("nombre", "") == tipo)
    return conteo

def contar_mandalorianos_por_tipo(tipos, reino):
    """
    Cuenta cuantos mandalorianos de cada tipo posee un reino

    Args:
        tipos (_list_): lista de los tipos de mandalorianos
        reino (_dict_): Diccionario con toda la información del reino
    
    Returns:
        dict: Diccionario con el tipo de mandaloriano como clave y la cantidad como valor
    """
    conteo = {}
    for tipo in tipos:
        conteo[tipo] = sum(1 for mandaloriano in reino.get("mandalorianos", []) if mandaloriano.get("nombre", "") == tipo)
    return conteo

def iniciar_batalla(reino1_data, reino2_data):
    """
    Lógica de simulación de batalla entre dos reinos.
    Aquí es donde comparas ataques, defensas y vidas.
    """
    print(
        f"\n--- BATALLA: {reino1_data['nombre']} VS {reino2_data['nombre']} ⚔️ ---")

    # TODO: añadir logica de batallla


def recibir_datos_reino(conexion):
    """Recibe los datos del socket y los convierte de JSON a diccionario."""
    try:
        data = conexion.recv(16384).decode('utf-8')
        return json.loads(data)
    except json.JSONDecodeError:
        print("Error al decodificar los datos del reino.")
        return None


def ejecutar_servidor():
    """Función principal que mantiene el servidor en ejecución."""
    while True:
        print("\n=== SERVIDOR LA GUERRA DE LAS GALAXIAS (2026) ===")
        print("1. Iniciar Guerra")
        print("2. Finalizar Servidor")
        opcion = input("Seleccionar opción para continuar: ")

        if opcion == "1":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.bind((HOST, PORT))
                server_socket.listen(2)
                server_socket.settimeout(TIEMPO_CONEXION)

                reinos_conectados = []

                try:
                    print("🔥 INICIANDO GUERRA GALÁCTICA 🔥")

                    while len(reinos_conectados) < 2:
                        print(f"Esperando conexión del Reino {len(reinos_conectados) + 1}")
                        conn, addr = server_socket.accept()
                        print(
                            f"Reino {len(reinos_conectados) + 1} conectado desde {addr}")

                        datos = recibir_datos_reino(conn)
                        if datos:
                            # Valida que los creditos no superen el límite permitido
                            if datos['coste_total'] > MAX_CREDITOS:
                                print(
                                    f"X RECHAZADO: {datos['nombre']} excede los créditos.")
                                conn.close()
                                continue

                            reinos_conectados.append(datos)
                            print(f"Reino '{datos['nombre']}' conectado.")
                    mostrar_configuraciones(reinos_conectados[0], reinos_conectados[1])
                    iniciar_batalla(reinos_conectados[0], reinos_conectados[1])

                except socket.timeout:
                    print(
                        "\n[!] X TIMEOUT - No se conectaron suficientes reinos.")
                    print("Reiniciando servidor automáticamente...\n")
                    continue  # Vuelve al menu

        elif opcion == "2":
            print("Apagando servidor...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar_servidor()
