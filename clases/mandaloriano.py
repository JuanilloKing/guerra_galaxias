"""Mandaloriano - Clase que representa a un mandaloriano en el juego"""


class Mandaloriano:
    """Clase la cual herederá sus atributos los demas mandalorianos"""

    def __init__(self, nombre, ataque, defensa, vida, velocidad, coste):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.velocidad = velocidad
        self.coste = coste


class Mandaloriano1(Mandaloriano):
    """Clase que representa a un mandaloriano de tipo 1"""

    def __init__(self):
        super().__init__("Mandaloriano1", 20, 15, 100, 60, 800)


class Mandaloriano2(Mandaloriano):
    """Clase que representa a un mandaloriano de tipo 2"""

    def __init__(self):
        super().__init__("Mandaloriano2", 25, 20, 120, 50, 1000)


class Mandaloriano3(Mandaloriano):
    """Clase que representa a un mandaloriano de tipo 3"""

    def __init__(self):
        super().__init__("Mandaloriano3", 30, 25, 140, 40, 1200)


class Mandaloriano4(Mandaloriano):
    """Clase que representa a un mandaloriano de tipo 4"""

    def __init__(self):
        super().__init__("Mandaloriano4", 35, 30, 160, 30, 1500)


class Mandaloriano5(Mandaloriano):
    """Clase que representa a un mandaloriano de tipo 5"""

    def __init__(self):
        super().__init__("Mandaloriano5", 40, 35, 180, 20, 2000)
