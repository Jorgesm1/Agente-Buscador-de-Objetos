## Agente Buscador de Objetos

Este agente se mueve en una cuadrícula de 5x5 para buscar un objeto colocado aleatoriamente. El agente se acerca al objeto paso a paso, mostrando la cuadrícula en cada movimiento.

### Funcionamiento

1. **Cuadrícula**:
   - La cuadrícula es una matriz de 5x5.
   - El agente (`A`) comienza en la posición `(0, 0)`.
   - El objeto (`O`) se coloca aleatoriamente en una posición de la cuadrícula.

2. **Movimiento del Agente**:
   - El agente se mueve hacia el objeto, ajustando su posición en fila y columna en cada paso.
   - En cada movimiento, se muestra la cuadrícula actualizada.

3. **Finalización**:
   - Cuando el agente encuentra el objeto, se muestra un mensaje de éxito.

### Ejecución

Para ejecutar el programa, usa el siguiente comando:

```bash
python buscador_objetos.py