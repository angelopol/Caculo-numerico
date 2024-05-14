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
    
    # Calcular el determinante de a
    if np.linalg.det(a) == 0:
        raise ValueError("La matriz es singular, el sistema no tiene una solución única.")
    
    # Formar la matriz aumentada
    ab = np.hstack([a, b.reshape(-1, 1)])
    
    # Calcular el rango de la matriz a y la matriz aumentada ab
    rank_a = np.linalg.matrix_rank(a)
    rank_ab = np.linalg.matrix_rank(ab)
    
    if rank_a < rank_ab:
        raise ValueError("El sistema no tiene solución.")
    elif rank_a < n:
        raise ValueError("El sistema tiene infinitas soluciones.")
    
    # Aplicar eliminación hacia adelante
    for i in range(n):
        # Verificar que el elemento diagonal no sea cero
        if ab[i, i] == 0:
            raise ValueError("El elemento diagonal es igual a 0, lo que genera una indeterminaciòn por divisiòn entre cero.")
        
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