# parcial de Programación II
# autor: Edwin Florez Jimenez
# fecha: 19 de octubre de 2025
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
# Calcular el promedio de ventas por dia
def calcular_ventas_por_dia(ventas_productoA, ventas_productoB, ventas_productoC):
    #usando zip para iterar sobre las tres listas simultaneamente
    for (v_a, v_b, v_c) in zip(ventas_productoA, ventas_productoB, ventas_productoC):
        ventas_totales_dia = v_a + v_b + v_c
    # --
    print("\nVentas totales por día:")
    print("Día\tVentas Totales")
    for dia in range(len(ventas_productoA)):
        ventas_totales_dia = ventas_productoA[dia] + ventas_productoB[dia] + ventas_productoC[dia]
        print(f"{dia + 1}\t{ventas_totales_dia}")

# --- Programa Principal ---
numero_de_dias = 0
# Titulo de programa
print("----- Analisis de Ventas -----")
'''
1. Registrar y mostrar las ventas generadas de cada producto y por cada día.
'''
numero_de_dias = int(input("Ingrese el número de días a analizar: "))
# validar que el número de días sea positivo
while numero_de_dias <= 0:
    print("Por favor, ingrese un número de días válido (mayor que 0).")
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
'''
2.
Calcular el total de ventas de cada producto en el período analizado
Obtener el promedio diario de ventas
'''
# Total de ventas
total_ventas_A = sum(productoA)
total_ventas_B = sum(productoB)
total_ventas_C = sum(productoC)
# mostrar totales
print("\nTotal de ventas de los productos:")
print(f"Producto A: {total_ventas_A}")
print(f"Producto B: {total_ventas_B}")
print(f"Producto C: {total_ventas_C}")
# Promedio de ventas por día
calcular_ventas_por_dia(productoA, productoB, productoC)

'''
3. Identificar los días con mayor y menor cantidad de ventas
indicando a qué producto pertenecen dichos valores
'''
