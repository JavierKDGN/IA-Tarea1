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

    def buscar_camino_dfs(self, inicio: tuple[int,int], meta: tuple[int,int]) -> int:
        """
        Busca un camino desde la celda inicial hasta la meta
        DFS no es optimo por lo tanto no siempre encontrara el camino mas corto
        retornara el numero de pasos hasta la meta (int)
        """
        i_0, j_0 = inicio
        i_n, j_n = meta

        if not (0 <= i_0 < self.m and 0 <= j_0 < self.n):
            raise IndexError("Inicio fuera de rango")
        if not (0 <= i_n < self.m and 0 <= j_n < self.n):
            raise IndexError("Meta fuera de rango")

        # El stack guardara:
        # (celda, num_pasos)
        stack = [(inicio, 0)]

        # set para no repetir movimientos en caso de ciclo
        visited = set()

        while stack:
            (celda_actual, num_pasos) = stack.pop()

            if celda_actual == meta:
                return num_pasos

            if celda_actual in visited:
                continue

            visited.add(celda_actual)

            vecinos = self.get_vecinos(celda_actual)

            for vecino in vecinos:
                if vecino in visited:
                    continue
                else:
                    stack.append((vecino, num_pasos + 1))

        # Si no se encuentra solucion, se retorna -1
        return -1


laberinto_saltarin = LaberintoSaltarin(laberinto)

print(laberinto_saltarin.get_vecinos((0, 3)))