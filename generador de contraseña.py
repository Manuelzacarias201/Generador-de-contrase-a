import random
import string

def transformar_contraseña(frase, seguridad=2):
    # Convertir la frase a una lista de caracteres para poder modificarla
    caracteres = list(frase)
    
    # Nivel de seguridad: 1 (básico), 2 (medio), 3 (alto)
    if nivel_seguridad >= 1:
        # Reemplazar algunas letras por números o caracteres similares
        sustituciones = {
            'a': '@',
            'e': '3',
            'i': '1',
            'o': '0',
            's': '$',
            'l': '1',
            't': '7'
        }
        for i in range(len(caracteres)):
            if caracteres[i].lower() in sustituciones:
                caracteres[i] = sustituciones[caracteres[i].lower()]
    
    if nivel_seguridad >= 2:
        # Añadir números aleatorios al principio o al final
        caracteres.insert(0, str(random.randint(0, 9)))
        caracteres.append(str(random.randint(0, 9)))
    
    if nivel_seguridad >= 3:
        # Añadir caracteres especiales aleatorios
        caracteres_especiales = list(string.punctuation)
        caracteres.insert(0, random.choice(caracteres_especiales))
        caracteres.append(random.choice(caracteres_especiales))
    
    # Convertir la lista de caracteres de nuevo a una cadena
    nueva_contraseña = ''.join(caracteres)
    return nueva_contraseña

# Ejemplo de uso
frase_usuario = input("Ingresa una palabra o frase: ")
nivel_seguridad = int(input("Elige el nivel de seguridad (1: básico, 2: medio, 3: alto): "))
contraseña_generada = transformar_contraseña(frase_usuario, seguridad=nivel_seguridad)
print(f"Tu nueva contraseña es: {contraseña_generada}")