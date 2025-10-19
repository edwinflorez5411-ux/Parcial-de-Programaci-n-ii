# Parcial de Programación II
# Autor: Edwin Florez Jimenez
# Fecha: 19 de octubre de 2025

import random

# Constantes
VENTA_MINIMA = 0
VENTA_MAXIMA = 50
PRODUCTOS = ['A', 'B', 'C']


def generar_ventas_diarias(numero_de_dias):
    """
    Genera ventas aleatorias para tres productos durante un período determinado.
    
    Args:
        numero_de_dias (int): Número de días a simular
        
    Returns:
        tuple: Tres listas con las ventas de productos A, B y C
    """
    producto_a = [random.randint(VENTA_MINIMA, VENTA_MAXIMA) for _ in range(numero_de_dias)]
    producto_b = [random.randint(VENTA_MINIMA, VENTA_MAXIMA) for _ in range(numero_de_dias)]
    producto_c = [random.randint(VENTA_MINIMA, VENTA_MAXIMA) for _ in range(numero_de_dias)]
    
    return producto_a, producto_b, producto_c


def calcular_ventas_totales_por_dia(ventas_a, ventas_b, ventas_c):
    """
    Calcula y muestra las ventas totales de todos los productos por día.
    
    Args:
        ventas_a (list): Ventas del producto A
        ventas_b (list): Ventas del producto B
        ventas_c (list): Ventas del producto C
    """
    print("\n" + "="*40)
    print("VENTAS TOTALES POR DÍA")
    print("="*40)
    print(f"{'Día':<10}{'Ventas Totales':>20}")
    print("-"*40)
    
    for dia, (v_a, v_b, v_c) in enumerate(zip(ventas_a, ventas_b, ventas_c), 1):
        ventas_totales = v_a + v_b + v_c
        print(f"{dia:<10}{ventas_totales:>20}")


def encontrar_dias_extremos(ventas_a, ventas_b, ventas_c):
    """
    Identifica los días con mayor y menor ventas individuales.
    
    Args:
        ventas_a (list): Ventas del producto A
        ventas_b (list): Ventas del producto B
        ventas_c (list): Ventas del producto C
    """
    mayor_venta = -1
    menor_venta = float('inf')
    info_mayor = {}
    info_menor = {}
    
    # Combinar todas las ventas con su información
    todas_ventas = [
        (dia + 1, 'A', ventas_a[dia]) for dia in range(len(ventas_a))
    ] + [
        (dia + 1, 'B', ventas_b[dia]) for dia in range(len(ventas_b))
    ] + [
        (dia + 1, 'C', ventas_c[dia]) for dia in range(len(ventas_c))
    ]
    
    # Encontrar extremos
    for dia, producto, venta in todas_ventas:
        if venta > mayor_venta:
            mayor_venta = venta
            info_mayor = {'dia': dia, 'producto': producto, 'cantidad': venta}
        if venta < menor_venta:
            menor_venta = venta
            info_menor = {'dia': dia, 'producto': producto, 'cantidad': venta}
    
    print("\n" + "="*40)
    print("DÍAS CON VENTAS EXTREMAS")
    print("="*40)
    print(f"Mayor venta: Día {info_mayor['dia']} - Producto {info_mayor['producto']} - {info_mayor['cantidad']} unidades")
    print(f"Menor venta: Día {info_menor['dia']} - Producto {info_menor['producto']} - {info_menor['cantidad']} unidades")


def mostrar_ventas_diarias(ventas_a, ventas_b, ventas_c):
    """
    Muestra las ventas diarias de todos los productos en formato tabular.
    
    Args:
        ventas_a (list): Ventas del producto A
        ventas_b (list): Ventas del producto B
        ventas_c (list): Ventas del producto C
    """
    print("\n" + "="*60)
    print("VENTAS DIARIAS POR PRODUCTO")
    print("="*60)
    print(f"{'Día':<10}{'Producto A':>15}{'Producto B':>15}{'Producto C':>15}")
    print("-"*60)
    
    for dia in range(len(ventas_a)):
        print(f"{dia + 1:<10}{ventas_a[dia]:>15}{ventas_b[dia]:>15}{ventas_c[dia]:>15}")


def solicitar_numero_dias():
    """
    Solicita y valida el número de días a analizar.
    
    Returns:
        int: Número de días válido (mayor que 0)
    """
    while True:
        try:
            dias = int(input("\nIngrese el número de días a analizar: "))
            if dias > 0:
                return dias
            print("❌ Error: El número de días debe ser mayor que 0.")
        except ValueError:
            print("❌ Error: Ingrese un número entero válido.")


def consultar_dia_especifico(ventas_a, ventas_b, ventas_c, numero_dias):
    """
    Permite consultar las ventas de un día específico.
    
    Args:
        ventas_a (list): Ventas del producto A
        ventas_b (list): Ventas del producto B
        ventas_c (list): Ventas del producto C
        numero_dias (int): Número total de días analizados
    """
    while True:
        respuesta = input("\n¿Desea consultar las ventas de un día específico? (si/no): ").lower().strip()
        
        if respuesta == 'no':
            print("\n✓ Gracias por usar el programa de análisis de ventas.")
            return
        
        if respuesta == 'si':
            break
        
        print("❌ Entrada inválida. Por favor ingrese 'si' o 'no'.")
    
    while True:
        try:
            dia = int(input(f"Ingrese el día a consultar (1-{numero_dias}): "))
            
            if 1 <= dia <= numero_dias:
                print("\n" + "="*40)
                print(f"VENTAS DEL DÍA {dia}")
                print("="*40)
                print(f"Producto A: {ventas_a[dia - 1]} unidades")
                print(f"Producto B: {ventas_b[dia - 1]} unidades")
                print(f"Producto C: {ventas_c[dia - 1]} unidades")
                print(f"Total del día: {ventas_a[dia - 1] + ventas_b[dia - 1] + ventas_c[dia - 1]} unidades")
                break
            
            print(f"❌ Error: El día debe estar entre 1 y {numero_dias}.")
        except ValueError:
            print("❌ Error: Ingrese un número entero válido.")


def main():
    """Función principal del programa."""
    print("="*60)
    print(" "*15 + "ANÁLISIS DE VENTAS")
    print("="*60)
    
    # 1. Solicitar número de días
    numero_dias = solicitar_numero_dias()
    
    # 2. Generar ventas (CORRECCIÓN: una sola llamada)
    ventas_a, ventas_b, ventas_c = generar_ventas_diarias(numero_dias)
    
    # 3. Mostrar ventas diarias
    mostrar_ventas_diarias(ventas_a, ventas_b, ventas_c)
    
    # 4. Calcular y mostrar totales
    total_a = sum(ventas_a)
    total_b = sum(ventas_b)
    total_c = sum(ventas_c)
    
    print("\n" + "="*40)
    print("TOTAL DE VENTAS POR PRODUCTO")
    print("="*40)
    print(f"Producto A: {total_a} unidades")
    print(f"Producto B: {total_b} unidades")
    print(f"Producto C: {total_c} unidades")
    print(f"Total general: {total_a + total_b + total_c} unidades")
    
    # 5. Mostrar ventas totales por día
    calcular_ventas_totales_por_dia(ventas_a, ventas_b, ventas_c)
    
    # 6. Identificar días extremos
    encontrar_dias_extremos(ventas_a, ventas_b, ventas_c)
    
    # 7. Consulta de día específico
    consultar_dia_especifico(ventas_a, ventas_b, ventas_c, numero_dias)


if __name__ == "__main__":
    main()