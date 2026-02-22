"""
Gestiona la conexión de los reinos, la recepción de datos y la guerra
"""

#TODO: EL DUELO MIXTO SE EJECUTA CUANDO NO ES NECESARIO (A VECES), ARREGLAR
#TODO: MEJORAR ESTETICA DE LOS MENSAJES POR CONSOLA (AÑADIR EMOJIS ESPACIADO ETC)
#TODO: QUE EN UN MENSAJE FINAL CUANDO TERMINE LA GUERRA, SE DIGA QUIEN GANÓ

import socket
import json
import clases.reino as reino
import clases.nave as nave
import clases.mandaloriano as mandaloriano
import random as r
import time as t

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
        "Estrella de la Muerte",
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
    print(f"Coste total: {reino1_data['coste_total']}✓\n")

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
    print(f"Coste total: {reino2_data['coste_total']}✓\n")
    print("✅ Ambos Reinos configurados correctamente. ¡INICIANDO BATALLA!\n")

    
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

def iniciar_guerra(reino1_data, reino2_data):
    """
    Lógica de simulación de guerra entre dos reinos.
    """
    print("=== 🏟️ CAMPO DE GUERRA GALÁCTICO 🏟️ ===")
    print(f"=== GUERRA: {reino1_data['nombre']} vs {reino2_data['nombre']} ===\n")
    print("📊 ESTADO INICIAL:")
    mostrar_estado(reino1_data, reino2_data)
    
    #Bucle de turnos:
    batallaActual = 0
    while ambos_vivos(reino1_data, reino2_data):
        batallaActual += 1
        ejecucion_batalla(reino1_data, reino2_data, batallaActual)
        print(f"📊 ESTADO BATALLA {batallaActual}:")
        mostrar_estado(reino1_data, reino2_data)
    
        
        


def mostrar_estado(reino1, reino2):
    """Función donde se imprime el estado de ambos reinos

    Args:
        reino1 (dict): Diccionario donde se guardan todos los datos del reino1
        reino2 (dict): Diccionario donde se guardan todos los datos del reino2
    """
    try:
        from tabulate import tabulate
    except ImportError:
        print("ATENCIÓN, Parece que no tienes la librería tabulate instalada en python")
        print("No te preocupes es sencillo instalarla")
        print("Simplemente ejecuta el siguiente comando en tu terminal:")
        print("pip install tabulate")
    
    navesReino1 = sum(1 for nave in reino1["naves"] if nave["vida"] > 0)
    navesReino2 = sum(1 for nave in reino2["naves"] if nave["vida"] > 0)
    mandalorianosReino1 = sum(1 for mandaloriano in reino1["mandalorianos"] if mandaloriano["vida"] > 0)
    mandalorianosReino2 = sum(1 for mandaloriano in reino2["mandalorianos"] if mandaloriano["vida"] > 0)

    data = [
        [reino1["nombre"], navesReino1, mandalorianosReino1],
        [reino2["nombre"], navesReino2, mandalorianosReino2]
    ]

    headers = ["REINO", "NAVES", "MANDALORIANOS"]

    print(tabulate(data, headers, tablefmt="fancy_grid"))
    print()

def ambos_vivos(reino1, reino2) -> bool:
    reino1Vivo = False
    reino2Vivo = False
    
    for nave in reino1["naves"]:
        if nave["vida"] > 0:
            reino1Vivo = True
    for mandaloriano in reino1["mandalorianos"]:
        if mandaloriano["vida"] > 0:
            reino1Vivo = True
    for nave in reino2["naves"]:
        if nave["vida"] > 0:
            reino2Vivo = True
    for mandaloriano in reino2["mandalorianos"]:
        if mandaloriano["vida"] > 0:
            reino2Vivo = True
    
    return reino1Vivo and reino2Vivo
        
def ejecucion_batalla(reino1, reino2, numeroBatalla):
    t.sleep(0.6)
    print("------------------------")
    print(f"==BATALLA {numeroBatalla}==")
    print("------------------------")

    naveR1 = None
    naveR2 = None
    mandalorianoR1 = None
    mandalorianoR2 = None
    
    for n in reino1["naves"]:
        if n["vida"] > 0:
            naveR1 = n
            break
    for n in reino2["naves"]:
        if n["vida"] > 0:
            naveR2 = n
            break
    for m in reino1["mandalorianos"]:
        if m["vida"] > 0:
            mandalorianoR1 = m
            break
    for m in reino2["mandalorianos"]:
        if m["vida"] > 0:
            mandalorianoR2 = m
            break
    
    # Aire vs Aire
    if naveR1 is not None and naveR2 is not None:
        print(f"=== Duelo aéreo: {naveR1['nombre']} vs {naveR2['nombre']} ===")
        duelo_1v1(naveR1, naveR2)

    # Tierra vs Tierra
    if mandalorianoR1 is not None and mandalorianoR2 is not None:
        print(f"=== Duelo terrestre: Mandaloriano de {mandalorianoR1['nombre']} vs Mandaloriano de{mandalorianoR2['nombre']} ===")
        duelo_1v1(mandalorianoR1, mandalorianoR2)

    # Combate cruzado cuando a los reinos no les quedan combates aereo vs aereo y terrestre vs terrestre,
    # entonces por ultimo deberan combatir los aereos y terrestres que queden
    if naveR1 is not None and mandalorianoR2 is not None and (naveR2 is None or mandalorianoR1 is None): 
        print(f"=== Duelo mixto: {naveR1['nombre']} vs Mandaloriano de {mandalorianoR2['nombre']} ===")
        duelo_1v1(naveR1, mandalorianoR2)
    elif mandalorianoR1 is not None and naveR2 is not None and (mandalorianoR2 is None or naveR1 is None):
        print(f"=== Duelo mixto: Mandaloriano de {mandalorianoR1['nombre']} vs {naveR2['nombre']} ===")
        duelo_1v1(mandalorianoR1, naveR2)

def duelo_1v1(combatiente1, combatiente2):
    """Logica de los combates

    Args:
        combatiente1 (Dict): caracteristicas del primer combatiente
        combatiente2 (Dict): caracteristicas del segundo combatiente
    """
    #cual tendra su turno primero
    if combatiente1["velocidad"] > combatiente2["velocidad"]:
        primero, segundo = combatiente1, combatiente2
    elif combatiente1["velocidad"] < combatiente2["velocidad"]:
        primero, segundo = combatiente2, combatiente1
    
    numeroTurno = 0
    while combatiente1["vida"] > 0 and combatiente2["vida"] > 0:
        #Esta dentro del while para que cada turno cambie la prioridad para que sea justo
        if combatiente1["velocidad"] == combatiente2["velocidad"]:
            #Si las velocidades son las mismas, se elije uno aleatoriamente
            primero, segundo = r.choice([(combatiente1, combatiente2),
                                        (combatiente2, combatiente1)])
        numeroTurno += 1
        t.sleep(0.3)
        print(f"=== TURNO {numeroTurno} ===")
        #ataque del mas rapido
        print(f"{primero['nombre']}: {primero['vida']}HP ==> va a atacar a ==> {segundo['nombre']}: {segundo['vida']}HP")
        daño = ataque(primero, segundo)
        segundo["vida"] -= daño
        #Si lo mata, poner vida en cero para que no se quede en negativo (por si falla algo)
        if segundo["vida"] < 0:
            segundo["vida"] = 0
            print(f"{segundo['nombre']} ha sido eliminado!")
        print(f"Le ha inflingido {daño} puntos de daño! {segundo['nombre']}: {segundo['vida']}HP")
        
        #ataque del mas lento (si sigue vivo)
        if segundo["vida"] > 0:
            print(f"{segundo['nombre']} va a atacar a {primero['nombre']}")
            daño = ataque(segundo, primero)
            primero["vida"] -= daño
            if primero["vida"] < 0:
                primero["vida"] = 0
                print(f"{primero['nombre']} ha sido eliminado!")
            print(f"Le ha inflingido {daño} puntos de daño! {primero['nombre']}: {primero['vida']}HP")

            
        
        

def ataque(atacante, defensor)-> int:
    """Esta función usa las estadisticas de ataque y defensa, y mediante una fórmula calcula el daño

    Args:
        atacante (Dict): Diccionario con los datos y caracteristicas del atacante
        defensor (Dict): Diccionario con los datos y caracteristicas del atacante

    Returns:
        int: Daño inflingido
    """
    statAtaque = atacante["ataque"]
    statDefensa = max(1, defensor["defensa"]) #esto hace que no sea cero y hayan errores
    
    #Formula simple de daño, con variaciones
    return round((statAtaque / statDefensa) * 100 * r.uniform(0.8, 1.2))
    
            
    

            
        
    
    

    
    
            
            
    

    
    

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
                    iniciar_guerra(reinos_conectados[0], reinos_conectados[1])

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
