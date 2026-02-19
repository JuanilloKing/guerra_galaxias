"""Módulo que define la clase Reino"""


class Reino:
    """Clase reino donde se almacenan las naves y mandalorianos de cada jugador"""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.naves = []
        self.mandalorianos = []
        self.creditos_gastados = 0

    def agregar_nave(self, nave):
        """Añade una nave a la flota y actualiza el coste."""
        self.naves.append(nave)
        self.creditos_gastados += nave.coste

    def agregar_mandaloriano(self, mandaloriano):
        """Añade un guerrero a la legión y actualiza el coste."""
        self.mandalorianos.append(mandaloriano)
        self.creditos_gastados += mandaloriano.coste

    def esta_vivo(self) -> bool:
        """Verifica si al reino le queda alguna unidad con vida."""
        if not self.naves and not self.mandalorianos:
            return False
        else:
            return True
