A = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

# Inicializamos el producto máximo con un valor muy pequeño.
max_product = float('-inf')
num1 = num2 = None  # Inicializamos los números que generan el producto máximo.

# Creamos un par de ciclos anidados.
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        # Calculamos el producto de cada par.
        product = A[i] * A[j]
        # Actualizamos el producto máximo si encontramos uno mayor.
        if product > max_product:
            max_product = product
            num1, num2 = A[i], A[j]  # Almacenamos los números que generan el producto máximo.

# Imprimimos el producto máximo y los números involucrados.
print(f"El producto máximo es {max_product}, generado por los números {num1} y {num2}.")
