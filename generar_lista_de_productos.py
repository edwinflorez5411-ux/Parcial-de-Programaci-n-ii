import random

def generar_lista_de_productos(numeros_de_dias):
    productoA = []
    productoB = []
    productoC = []
    
    for dia in range(numeros_de_dias):
        productoA.append(random.randint(0, 100))
        productoB.append(random.randint(0, 100))
        productoC.append(random.randint(0, 100))
    
    return productoA, productoB, productoC