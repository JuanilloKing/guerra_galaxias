# La Guerra de las Galaxias 🚀

Este proyecto es un simulador de guerras entre reinos basado en el universo de Star Wars, el cual se puede ejecutar desde distintos equipos, ya que tiene una estructura cliente - servidor, usando los sockets de python

¡¡OJO!! De manera predefinida, el servidor y el cliente esta hecho para ejecutarse en local.
Para ejecutarse en red y poder jugar desde distintos dispositivos deberás entrar en los archivos cliente.py y servidor.py con algun editor de codigo como por ejemplo VisualStudio Code. Al principio de ambos archivos deberás cambiar la constante HOST = "127.0.0.1" y poner la IPv4 del dispositivo que ejecutará el servidor.

Si no sabes como ver la IPv4 del dispositivo aqui te dejo unos comandos que escribiras en tu cmd para que se muestre:

Windows: ipconfig

Linux y Mac:  ip a



## 📋 Descripción

Este proyecto implementa un juego de estrategia basado en la Guerra de las Galaxias donde dos jugadores pueden:
- Crear sus reinos con un presupuesto inicial de créditos
- Reclutar diferentes tipos de naves (Ejecutor, Halcón Milenario, Estrella de la Muerte, etc.)
- Reclutar unidades Mandalorian de diferentes niveles
- Participar en batallas contra otros reinos
- Gestionar recursos y estrategia militar

## 📁 Estructura del Proyecto

```
guerra_galaxias/
├── cliente.py              # Cliente que gestiona el reino y conexión con servidor
├── servidor.py             # Servidor que controla la lógica de batallas
├── README.md               # Archivo que estas leyendo, con toda la informacion que necesitas saber
├── clases/
│   ├── reino.py            # Clase Reino (gestiona recursos y unidades)
│   ├── nave.py             # Clases de diferentes tipos de naves
│   └── mandaloriano.py     # Clases Mandalorian de diferentes niveles
└── __pycache__/            # Caché de Python (ignorar)
```

## 🛠️ Requisitos

- **Python 3.8+** o superior
- **tabulate**: librería para visualización de datos en tablas

## 📦 Instalación

1. **Clonar o descargar el proyecto:**
   ```bash
   cd guerra_galaxias
   ```

2. **Instalar dependencias:**
   ```bash
   pip install tabulate
   ```

3. **Verificar que todos los archivos están en su lugar:**
   - `servidor.py`
   - `cliente.py`
   - `clases/reino.py`
   - `clases/nave.py`
   - `clases/mandaloriano.py`

## 🎮 Cómo Ejecutar

### 1. Iniciar el Servidor
En una terminal, ejecuta:
```bash
python servidor.py
```
El servidor se conectará en `127.0.0.1:5000` y esperará conexiones. (O la IP que seleccionaste)

### 2. Ejecutar los Clientes
En terminales separadas, ejecuta:
```bash
python cliente.py
```
Repite esto para cada jugador que participará en la batalla.

### 3. Configurar Reinos
Sigue las instrucciones en pantalla:
- Ingresa el nombre de tu reino
- Selecciona y compra naves
- Entrena unidades Mandalorian
- ¡Prepárate para la batalla!

## 🎯 Características Principales

- **Gestión de Recursos**: Presupuesto de créditos limitados (50,000)
- **Sistema de Naves**: Múltiples tipos con diferentes características
- **Unidades Mandalorian**: 5 niveles diferentes de guerreros
- **Combate Estratégico**: Simulación en tiempo real de batallas
- **Red Local**: Comunicación cliente-servidor vía socket

## 📝 Notas Técnicas

- La comunicación se realiza mediante sockets TCP/IP
- Los datos se envían en formato JSON
- El servidor gestiona la lógica de batalla y validaciones
- Tiempo máximo de conexión: 20 segundos

## 👥 Autores

Eduardo Sumariva Salgado | 2ºDAM

Carlos Fraidias Del Valle | 2ºDAM

## 📄 Licencia

Este proyecto es de uso educativo.

---

**¡Que gane la mejor estrategia! 🌟**
