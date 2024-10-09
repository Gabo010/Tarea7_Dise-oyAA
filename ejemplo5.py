def cifrado_cesar(texto, desplazamiento=5):
    resultado = ""

    # Recorremos cada caracter en el texto
    for char in texto:
        # Verificamos si el caracter es una letra
        if char.isalpha():
            # Calculamos el desplazamiento
            desplazado = ord(char) + desplazamiento

            # Si es mayúscula y se pasa de 'Z'
            if char.isupper():
                if desplazado > ord('Z'):
                    desplazado -= 27         #para incluir 'ñ'
            # Si es minúscula y se pasa de 'z'
            else:
                if desplazado > ord('z'):
                    desplazado -= 27  #para incluir 'ñ'

            # Convertimos el número desplazado de vuelta a un caracter
            resultado += chr(desplazado)
        else:
            # Si no es letra, se deja igual
            resultado += char

    return resultado

def descifrado_cesar(texto, desplazamiento=5):
    resultado = ""

    # Recorremos cada caracter en el texto
    for char in texto:
        # Verificamos si el caracter es una letra
        if char.isalpha():
            # Calculamos el desplazamiento inverso
            desplazado = ord(char) - desplazamiento

            # Si es mayúscula y se pasa de 'A'
            if char.isupper():
                if desplazado < ord('A'):
                    desplazado += 27   #para incluir 'ñ'
            # Si es minúscula y se pasa de 'a'
            else:
                if desplazado < ord('a'):
                    desplazado += 27    #para incluir 'ñ'

            # Convertimos el número desplazado de vuelta a un caracter
            resultado += chr(desplazado)
        else:
            # Si no es letra, se deja igual
            resultado += char

    return resultado

# Ejemplo de uso
texto_claro = ("Que pacho,soy Cristhian Carmona de la materia de analisis de algoritmos del 1561,"
               "tengo 20 y me gusta mucho Gears of War")
texto_cifrado = cifrado_cesar(texto_claro)
print(f"Texto Cifrado: {texto_cifrado}")

# Descifrar el texto cifrado
texto_descifrado = descifrado_cesar(texto_cifrado)
print(f"Texto Descifrado: {texto_descifrado}")

