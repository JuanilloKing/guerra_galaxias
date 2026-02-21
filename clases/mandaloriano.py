
class Mandaloriano:
    """Clase la cual herederá sus atributos los demas mandalorianos"""

    def __init__(self, nombre, ataque, defensa, vida, velocidad, coste):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.velocidad = velocidad
        self.coste = coste


class MandalorianoNivel1(Mandaloriano):
    """Clase que representa a un mandaloriano de nivel 1"""

    def __init__(self):
        super().__init__("Nivel 1", 20, 15, 100, 60, 800)


class MandalorianoNivel2(Mandaloriano):
    """Clase que representa a un mandaloriano de nivel 2"""

    def __init__(self):
        super().__init__("Nivel 2", 25, 20, 120, 50, 1000)


class MandalorianoNivel3(Mandaloriano):
    """Clase que representa a un mandaloriano de nivel 3"""

    def __init__(self):
        super().__init__("Nivel 3", 30, 25, 140, 40, 1200)


class MandalorianoNivel4(Mandaloriano):
    """Clase que representa a un mandaloriano de nivel 4"""

    def __init__(self):
        super().__init__("Nivel 4", 35, 30, 160, 30, 1500)


class MandalorianoNivel5(Mandaloriano):
    """Clase que representa a un mandaloriano de nivel 5"""

    def __init__(self):
        super().__init__("Nivel 5", 40, 35, 180, 20, 2000)
