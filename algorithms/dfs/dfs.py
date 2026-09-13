def dfs(raiz, objetivo):
    print("En este momento estoy en el nodo que tiene como valor " + raiz.valor)
    if raiz.valor == objetivo:
        print("En este momento estoy en el nodo que tiene como valor " + raiz.valor)
        return raiz
    
    izquierda = dfs(raiz.izquierda, objetivo)
    derecha = dfs(raiz.derecha, objetivo)
    if izquierda != None:
        return izquierda
    if derecha != None:
        return derecha
    
    """
    for valor in range(0, len(raiz.hijos)):
        nodo_resultado = dfs(raiz.hijos[valor], objetivo)
        if nodo_resultado != None:
            return nodo_resultado
    """
    return None