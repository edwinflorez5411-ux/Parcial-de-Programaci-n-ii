# parcial de Programación II
# autor: Edwin Florez Jimenez
# fecha: 19 de octubre de 2025
import random

# Se definen las funciones usadas en el programa principal
# estan fueron creadas para realizar las tareas del programa
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
# para encontrar los dias con mayor y menor ventas
def encontrar_dias_extremos(ventas_productoA, ventas_productoB, ventas_productoC):
    mayor_venta = -1
    menor_venta = float('inf')
    dia_mayor = -1
    dia_menor = -1
    producto_mayor = ""
    producto_menor = ""
    
    for dia in range(len(ventas_productoA)):
        # Verificar producto A
        if ventas_productoA[dia] > mayor_venta:
            mayor_venta = ventas_productoA[dia]
            dia_mayor = dia + 1
            producto_mayor = "Producto A"
        if ventas_productoA[dia] < menor_venta:
            menor_venta = ventas_productoA[dia]
            dia_menor = dia + 1
            producto_menor = "Producto A"
        # Verificar producto B
        if ventas_productoB[dia] > mayor_venta:
            mayor_venta = ventas_productoB[dia]
            dia_mayor = dia + 1
            producto_mayor = "Producto B"
        if ventas_productoB[dia] < menor_venta:
            menor_venta = ventas_productoB[dia]
            dia_menor = dia + 1
            producto_menor = "Producto B"
        # Verificar producto C
        if ventas_productoC[dia] > mayor_venta:
            mayor_venta = ventas_productoC[dia]
            dia_mayor = dia + 1
            producto_mayor = "Producto C"
        if ventas_productoC[dia] < menor_venta:
            menor_venta = ventas_productoC[dia]
            dia_menor = dia + 1
            producto_menor = "Producto C"
    
    print(f"\nDía con mayor venta: Día {dia_mayor} del {producto_mayor} con {mayor_venta} unidades.")
    print(f"Día con menor venta: Día {dia_menor} del {producto_menor} con {menor_venta} unidades.")
#

# --- Programa Principal ---
# Titulo de programa
numero_de_dias = 0
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
encontrar_dias_extremos(productoA, productoB, productoC)
'''
4. Consulta de venta en un dias específico
'''
solicitud_de_consulta = str(input("\n¿Desea consultar las ventas de un día? (si o no): "))
# Validar la entrada del usuario
while solicitud_de_consulta not in ['si', 'no']:
    print("Entrada inválida. Por favor ingrese 'si' o 'no'.")
    solicitud_de_consulta = str(input("¿Desea consultar las ventas de un día? (si/no): "))
# Salida del programa si no desea consultar
if solicitud_de_consulta == 'no':
    print("Gracias por usar el programa de análisis de ventas.")

# Consulta de ventas en un día específico
if solicitud_de_consulta == 'si':
    dia_consulta = int(input(f"Ingrese el día a consultar (1-{numero_de_dias}): "))
    while True:
        if 1 <= dia_consulta <= numero_de_dias:
            print(f"Ventas del Día {dia_consulta}:")
            print(f"Producto A: {productoA[dia_consulta - 1]}")
            print(f"Producto B: {productoB[dia_consulta - 1]}")
            print(f"Producto C: {productoC[dia_consulta - 1]}")
            break
        print(f"Día inválido. Debe estar entre 1 y {numero_de_dias}.")
        try:
            dia_consulta = int(input(f"Ingrese el día a consultar (1-{numero_de_dias}): "))
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")