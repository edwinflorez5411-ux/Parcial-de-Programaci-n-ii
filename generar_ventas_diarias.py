import random
def generar_ventas_diarias(numero_de_dias: int) -> list:
    productoA = []
    productoB = []
    productoC = []
    
    for dia in range(numero_de_dias):
        ventaA = random.randint(0, 50)
        ventaB = random.randint(0, 50)
        ventaC = random.randint(0, 50)
        
        productoA.append(ventaA)
        productoB.append(ventaB)
        productoC.append(ventaC)
        
    return productoA, productoB, productoC