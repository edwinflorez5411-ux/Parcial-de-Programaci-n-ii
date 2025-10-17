def calcular_promedio(ventas: list) -> float:
    # Calcula el promedio de una lista de ventas
    if len(ventas) == 0:
        return 0
    total = sum(ventas)
    count = len(ventas)
    promedio = total / count
    return promedio