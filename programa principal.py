# parcial de Programación II
import random

#definiendo las funciones usadas en el programa principal
# Generar ventas diarias para tres productos
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
# --

# --- Programa Principal ---
numero_de_dias = 0
# Titulo de programa
print("----- Analisis de Ventas -----")
'''
1. Registrar y mostrar las ventas generadas de cada producto y por cada día.
'''
numero_de_dias = int(input("Ingrese el número de días a analizar: "))
productoA = generar_ventas_diarias(numero_de_dias)[0]
productoB = generar_ventas_diarias(numero_de_dias)[1]
productoC = generar_ventas_diarias(numero_de_dias)[2]
# Mostrar las ventas diarias de cada producto
# las ventas de los productos se muestran de forma tabular
print("\nVentas Diarias:")
print("Día\tProducto A\tProducto B\tProducto C")
for dia in range(numero_de_dias):
    print(f"{dia + 1}\t{productoA[dia]}\t\t{productoB[dia]}\t\t{productoC[dia]}")
    