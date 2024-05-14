import random

def obtener_numero_secreto(inicio, fin):
    """Genera un número aleatorio entre inicio y fin."""
    return random.randint(inicio, fin)

def solicitar_intento():
    """Solicita un intento al usuario y valida la entrada."""
    GRIS = '\033[90m'
    ROJO_CLARO = '\033[91m'
    RESET = '\033[0m'
    while True:
        try:
            guess = int(input(f"{GRIS}Ingresa un número: {RESET}"))
            if 0 <= guess <= 100:
                return guess
            else:
                print(f"{ROJO_CLARO}El número debe estar entre 0 y 100. Intenta de nuevo.{RESET}")
        except ValueError:
            print(f"{ROJO_CLARO}Por favor, introduce un número válido.{RESET}")

def calcular_porcentaje(intentos):
    """Calcula el porcentaje en función del número de intentos."""
    porcentaje = 12.35 + intentos * 0.121  # Ajusta el incremento del porcentaje según los intentos
    return min(porcentaje, 14.56)  # Limita el máximo porcentaje a 14.56%

def juego_adivinanza():
    """Ejecuta el juego de adivinanza de números."""
    inicio, fin = 1, 100
    numero_secreto = obtener_numero_secreto(inicio, fin)
    intentos = 0
    adivinado = False

    print(f"""    
   █▀▄ █▀▀ █▀ ▄▀█ █▀▀ █ ▄▀█   ▀█▀ █░█   █ █▄░█ ▀█▀ █░█ █ █▀▀ █ █▀█ █▄░█
   █▄▀ ██▄ ▄█ █▀█ █▀░ █ █▀█   ░█░ █▄█   █ █░▀█ ░█░ █▄█ █ █▄▄ █ █▄█ █░▀█
          

¿PODRÁS ADIVINAR EL NÚMERO SECRETO ENTRE {inicio} y {fin} EN MENOS DE 10 INTENTOS?
--------------------------------------------------------------------------
          """)

    while not adivinado:
        guess = solicitar_intento()
        intentos += 1

        if guess == numero_secreto:
            adivinado = True
        elif guess < numero_secreto:
            print("\033[92m| El número es mayor ↑. Intentalo de nuevo.\033[0m")  # Verde claro
        else:
            print("\033[34m| El número es menor ↓. Intentalo de nuevo.\033[0m")  # Azul

        if intentos >= 10:  # Si se superan los 10 intentos, el juego termina
            print("""\033[93m
      █▀▀█ █──█ 　 █▀▀▄ █▀▀█ █ 
      █──█ █▀▀█ 　 █──█ █──█ ▀ 
      ▀▀▀▀ ▀──▀ 　 ▀──▀ ▀▀▀▀ ▄
          
No lo has conseguido. No te preocupes. 
El 30% de la población no lo consigue
    > Inténtalo de nuevo <   \033[0m
                  
                  """)  # Amarillo claro
            return  # Salir de la función y terminar el juego

    # Código ANSI para aproximar el color naranja
    ORANGE = '\033[38;5;214m'
    RESET = '\033[0m'

    porcentaje = calcular_porcentaje(intentos)

    print(f"""{ORANGE}

░█──░█ █▀▀█ █───█ █ 　 ░█─── █▀▀█ 　 █── █▀▀█ █▀▀▀ █▀▀█ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █ 
░█░█░█ █──█ █▄█▄█ ▀ 　 ░█─── █──█ 　 █── █──█ █─▀█ █▄▄▀ █▄▄█ ▀▀█ ──█── █▀▀ ▀ 
░█▄▀▄█ ▀▀▀▀ ─▀─▀─ ▄ 　 ░█▄▄█ ▀▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀─▀▀ ▀──▀ ▀▀▀ ──▀── ▀▀▀ ▄
   
        Adivinaste el número secreto {numero_secreto} en {intentos} intentos
    >Solo el {porcentaje:.2f}% de la población mundial es capaz de hacerlo{RESET}<
          
          """)

# Ejecuta el juego
juego_adivinanza()
