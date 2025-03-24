import random

def ahorcado():
    palabras = ["python", "programacion", "juego", "ordenador", "teclado", "raton"]
    palabra_secreta = random.choice(palabras).lower()
    intentos_maximos = 6
    intentos = 0
    letras_adivinadas = []
    
    print("¡Bienvenido a 'Ahorcado'!")
    print("Estoy pensando en una palabra. Intenta adivinarla letra por letra.")
    
    while True:
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "
        
        print("\nPalabra:", palabra_mostrada)
        intento = input("Ingresa una letra: ").lower()
        
        if intento in letras_adivinadas:
            print("Ya has intentado esa letra. Intenta nuevamente.")
        elif intento in palabra_secreta:
            letras_adivinadas.append(intento)
            if len(letras_adivinadas) == len(set(palabra_secreta)):
                print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
                break
        else:
            intentos += 1
            print("Letra incorrecta.")
            if intentos == intentos_maximos:
                print("¡Oh no! Has agotado todos tus intentos.")
                print("La palabra secreta era:", palabra_secreta)
                break
    
    print("\n¡Gracias por jugar!")

ahorcado()
