import random

class AgenteBuscador:
    def __init__(self):
        self.filas = 5
        self.columnas = 5
        self.cuadricula = [[None for _ in range(self.columnas)] for _ in range(self.filas)]
        self.agente_pos = (0, 0)  # Posición inicial del agente
        self.objeto_pos = self.colocar_objeto()  # Posición aleatoria del objeto

    def colocar_objeto(self):
        """Coloca el objeto en una posición aleatoria de la cuadrícula."""
        fila = random.randint(0, self.filas - 1)
        columna = random.randint(0, self.columnas - 1)
        return (fila, columna)

    def mostrar_cuadricula(self):
        """Muestra la cuadrícula con la posición del agente y el objeto."""
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if (fila, columna) == self.agente_pos:
                    print("A", end=" ")  # Representa al agente
                elif (fila, columna) == self.objeto_pos:
                    print("O", end=" ")  # Representa al objeto
                else:
                    print(".", end=" ")  # Espacio vacío
            print()  # Nueva línea después de cada fila
        print()  # Espacio entre movimientos

    def mover_agente(self):
        """Mueve al agente hacia el objeto."""
        while self.agente_pos != self.objeto_pos:
            self.mostrar_cuadricula()
            fila_agente, columna_agente = self.agente_pos
            fila_objeto, columna_objeto = self.objeto_pos

            # Mover hacia la fila del objeto
            if fila_agente < fila_objeto:
                fila_agente += 1
            elif fila_agente > fila_objeto:
                fila_agente -= 1

            # Mover hacia la columna del objeto
            if columna_agente < columna_objeto:
                columna_agente += 1
            elif columna_agente > columna_objeto:
                columna_agente -= 1

            self.agente_pos = (fila_agente, columna_agente)
            print(f"El agente se mueve a: {self.agente_pos}")

        # Mostrar la cuadrícula final cuando el agente encuentra el objeto
        self.mostrar_cuadricula()
        print("¡El agente ha encontrado el objeto!")

if __name__ == "__main__":
    agente = AgenteBuscador()
    agente.mover_agente()