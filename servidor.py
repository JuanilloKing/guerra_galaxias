"""
Gestiona la conexión de los reinos, la recepción de datos y la batalla
"""

import socket
import json
import clases.reino as reino

# Constantes del proyecto
HOST = '10.7.14.31'
PORT = 5000
TIEMPO_CONEXION = 10
MAX_CREDITOS = 100000


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
        data = conexion.recv(4096).decode('utf-8')
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
