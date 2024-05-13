import numpy as np

def GaussJordan(a, b):
    """
    Resuelve el sistema de ecuaciones lineales Ax = b usando el método de Gauss-Jordan.
    :param a: Matriz cuadrada de coeficientes (nxn).
    :param b: Vector de términos independientes (n).
    :return: Vector de soluciones x (n).
    """
    # Convertir a y b a arrays de numpy para facilitar las operaciones
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    
    # Obtener el número de filas
    n = len(b)
    
    # Formar la matriz aumentada
    ab = np.hstack([a, b.reshape(-1, 1)])
    
    # Aplicar eliminación hacia adelante
    for i in range(n):
        # Hacer el elemento diagonal 1
        ab[i] = ab[i] / ab[i, i]
        
        # Hacer los elementos debajo de la diagonal 0
        for j in range(i+1, n):
            ab[j] = ab[j] - ab[j, i] * ab[i]
    
    # Aplicar sustitución hacia atrás
    for i in range(n-1, -1, -1):
        # Hacer los elementos por encima de la diagonal 0
        for j in range(i-1, -1, -1):
            ab[j] = ab[j] - ab[j, i] * ab[i]
    
    # La última columna de la matriz aumentada es ahora la solución
    x = ab[:, -1]
    
    return x