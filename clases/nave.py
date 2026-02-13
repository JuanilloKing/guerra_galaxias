""" Naves espaciales del juego """


class Nave:
    """Clase la cual herederá sus atributos a las demas naves"""

    def __init__(self, nombre, ataque, defensa, velocidad, coste):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.coste = coste


class EstrellaMuerte(Nave):
    """Nave que representa la estrella de la muerte"""

    def __init__(self, nombre, ataque, defensa, velocidad, coste):
        super().__init__(nombre, ataque, defensa, velocidad, coste)
        self.nombre = "Estrella de la Muerte"
        self.ataque = 80
        self.defensa = 90
        self.vida = 1500
        self.velocidad = 20
        self.coste = 4500


class Ejecutor(Nave):
    """Nave que representa ejecutor"""

    def __init__(self, nombre, ataque, defensa, velocidad, coste):
        super().__init__(nombre, ataque, defensa, velocidad, coste)
        self.nombre = "Ejecutor"
        self.ataque = 70
        self.defensa = 80
        self.vida = 1200
        self.velocidad = 35
        self.coste = 4000


class HalconMilenario(Nave):
    """Nave que representa el halcón milenario"""

    def __init__(self, nombre, ataque, defensa, velocidad, coste):
        super().__init__(nombre, ataque, defensa, velocidad, coste)
        self.nombre = "Halcon Milenario"
        self.ataque = 60
        self.defensa = 50
        self.vida = 800
        self.velocidad = 70
        self.coste = 2500


class NaveRealNaboo(Nave):
    """Nave que representa la nave real de Naboo"""

    def __init__(self, nombre, ataque, defensa, velocidad, coste):
        super().__init__(nombre, ataque, defensa, velocidad, coste)
        self.nombre = "Nave Real de Naboo"
        self.ataque = 40
        self.defensa = 60
        self.vida = 600
        self.velocidad = 50
        self.coste = 2000


class CazaEstelarJedi(Nave):
    """Nave caza estelar jedi"""

    def __init__(self, nombre, ataque, defensa, velocidad, coste):
        super().__init__(nombre, ataque, defensa, velocidad, coste)
        self.nombre = "Caza Estellar Jedi"
        self.ataque = 50
        self.defensa = 40
        self.vida = 400
        self.velocidad = 80
        self.coste = 1500
