"""Servidor del juego"""

import socket
import threading
import time
import clases.reino as reino
HOST = "localhost"
PORT = 5000

def gestionar_servidor():
    """"Función que gestiona el servidor"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)
    server_socket.settimeout(20) # Timeout de 20 segundos

    print("=== SERVIDOR LA GUERRA DE LAS GALAXIAS (2026) ===")
    print("1. Iniciar Guerra")
    print("2. Finalizar Servidor")
    opcion = input("Seleccionar opción: ")
    if opcion == "1":
        clientes = []
        print("Esperando conexión de dos reinos...")

        try:
            while len(clientes) < 2:
                conn, addr = server_socket.accept()
                clientes.append(conn)
                print(f"Reino {len(clientes)} conectado.")

            # Aquí iría la lógica para recibir datos y simular batalla
            print("¡Iniciando Guerra!")
            

        except socket.timeout:
            print("X TIMEOUT - Reiniciando servidor...")
            gestionar_servidor()
