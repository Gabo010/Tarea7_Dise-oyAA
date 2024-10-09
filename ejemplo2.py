def min_monedas(claudiolares, S):
    valor_min = float('inf')  # Inicializamos con un valor grande.
    top_combinacion = None   # Guardaremos la mejor combinación.

    # Usaremos una lista que almacena combinaciones de monedas actuales.
    def pruebas(actual_com, total):
        nonlocal valor_min, top_combinacion

        # Si la suma es igual a S, verificamos si es mejor que la solución anterior.
        if total == S:
            if len(actual_com) < valor_min:
                valor_min = len(actual_com)
                top_combinacion = actual_com[:]
            return

        # Si la suma excede S, no continuamos con esta combinación.
        if total > S:
            return

        # Intentamos agregar cada moneda a la combinación actual y seguimos acumulando.
        for pejecoin in claudiolares:
            actual_com.append(pejecoin)
            pruebas(actual_com, total + pejecoin)
            actual_com.pop()  # Retiramos la moneda para probar otra combinación.

    # Iniciamos la búsqueda con una combinación vacía y suma de 0.
    pruebas([], 0)

    return top_combinacion, valor_min


# Ejemplo de uso:
coins = [1, 2, 5]
S = 33
resultado = min_monedas(coins, S)

if resultado[0]:
    print(f"La mínima cantidad de monedas necesarias es {resultado[1]}, con las monedas {resultado[0]}")
else:
    print("No es posible obtener la cantidad exacta con las monedas disponibles.")
