""" Naves espaciales del juego """


class Nave:
    """Clase la cual herederá sus atributos a las demas naves"""

    def __init__(self, nombre, ataque, defensa, velocidad, coste, vida):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.coste = coste
        self.vida = vida


class EstrellaMuerte(Nave):
    """Nave que representa la estrella de la muerte"""

    def __init__(self):
        super().__init__("Estrella de la muerte", 80, 90, 20, 4500, 1500)



class Ejecutor(Nave):
    """Nave que representa ejecutor"""

    def __init__(self):
        super().__init__("Ejecutor", 70, 80, 35, 4000, 1200)



class HalconMilenario(Nave):
    """Nave que representa el halcón milenario"""

    def __init__(self):
        super().__init__("Halcon Milenario", 60, 50, 70, 2500, 800)

class NaveRealNaboo(Nave):
    """Nave que representa la nave real de Naboo"""

    def __init__(self):
        super().__init__("Nave Real de Naboo", 40, 60, 50, 2000, 600)



class CazaEstelarJedi(Nave):
    """Nave caza estelar jedi"""

    def __init__(self):
        super().__init__("Caza Estelar Jedi", 50, 40, 80, 1500, 400)
