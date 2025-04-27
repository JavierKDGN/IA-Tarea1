"""
Laberinto(m,n,fi,ci,fd,cd,lab)
m: filas
n: columnas
fi: fila inicial
ci: columa inicial
fd: fila destino
cd: columna destino
lab: laberinto
"""

laberinto = [
    [3, 4, 1, 3, 1],
    [3, 3, 3, 0, 2],
    [3, 1, 2, 2, 3],
    [4, 2, 3, 3, 3],
    [4, 1, 4, 3, 2]
]

"""
En el laberinto superior:
m = 5
n = 5
Partimos en (0,0)
Meta en (1,3)
"""

class LaberintoSaltarin:

    def __init__(self, lab: list[list[int]]):
        """
        Args:
              lab: list[list[int]] Matriz de laberinto
        """

        self.lab = lab
        if not lab or not lab[0]:
            raise ValueError("Laberinto vacio")

        self.m = len(lab)
        self.n = len(lab[0])

    def get_vecinos(self, vertice: tuple[int,int]) -> list[tuple[int, int]]:

        # Unpacking de la tupla
        i, j = vertice

        if not (0 <= i < self.m and 0 <= j < self.n):
            return []

        peso = self.lab[i][j]
        vecinos = []

        # Defino la meta con peso 0 para que los algoritmos se detengan
        if peso > 0:
            direcciones = [(0, peso), (0, -peso), (peso, 0), (-peso, 0)]
            for di, dj in direcciones:
                # Revisamos si las nuevas celdas estan dentro del rango del laberinto
                if 0 <= i + di < self.m and 0 <= j + dj < self.n:
                    vecinos.append((i + di, j + dj))

        return vecinos


laberinto_saltarin = LaberintoSaltarin(laberinto)

print(laberinto_saltarin.get_vecinos((0, 3)))