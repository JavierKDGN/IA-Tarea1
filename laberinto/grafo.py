from collections import deque

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

    def buscar_camino_dfs(self, inicio: tuple[int,int], meta: tuple[int,int]):
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

            if celda_actual in visited:
                continue

            visited.add(celda_actual)
            print(f"{celda_actual} -> {num_pasos}")

            if celda_actual == meta:
                return num_pasos

            vecinos = self.get_vecinos(celda_actual)

            for vecino in vecinos:
                if vecino in visited:
                    continue
                else:
                    stack.append((vecino, num_pasos + 1))

        # Si no se encuentra solucion, se retorna "no hay solucion"
        return -1

    def buscar_camino_bfs(self, inicio: tuple[int,int], meta: tuple[int,int]):
        """
        Busca un camino desde la celda inicial hasta la meta.
        BFS debido a que el costo es igual de un nodo hacia sus vecinos.
        Retornara el numero de pasos mas corto hasta la meta (int),
        ya que BFS es optimo cuando los costos son iguales
        """
        i_0, j_0 = inicio
        i_n, j_n = meta

        if not (0 <= i_0 < self.m and 0 <= j_0 < self.n):
            raise IndexError("Inicio fuera de rango")
        if not (0 <= i_n < self.m and 0 <= j_n < self.n):
            raise IndexError("Meta fuera de rango")

        # La cola guardara:
        # (celda, num_pasos)
        cola = deque([(inicio, 0)])

        # set para no repetir movimientos en caso de ciclo
        visited = set()

        while cola:
            (celda_actual, num_pasos) = cola.popleft()

            print(f"{celda_actual} -> {num_pasos}")


            if celda_actual == meta:
                return num_pasos

            vecinos = self.get_vecinos(celda_actual)

            for vecino in vecinos:
                if vecino in visited:
                    continue
                else:
                    visited.add(celda_actual)
                    cola.append((vecino, num_pasos + 1))

        # Si no se encuentra solucion, se retorna "no hay solucion"
        return "no hay solucion"



laberinto_saltarin = LaberintoSaltarin(laberinto)

print(laberinto_saltarin.buscar_camino_dfs((0,0),(1,3)))
print(laberinto_saltarin.buscar_camino_bfs((0,0),(1,3)))
