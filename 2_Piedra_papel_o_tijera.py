import random

def obtener_opcion_maquina():
    opciones = ["piedra", "papel", "tijera"]
    opcion = random.choice(opciones)
    return opcion

def determinar_ganador(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (
        (jugador == "piedra" and maquina == "tijera") or
        (jugador == "papel" and maquina == "piedra") or
        (jugador == "tijera" and maquina == "papel")
    ):
        return "\033[92mGanaste a la máquina ^_^\033[0m"
    else:
        return "\033[36mLa máquina te ha ganado -_-\033[0m"

print("""\033[38;5;214m
░█▀▀█ ─▀─ █▀▀ █▀▀▄ █▀▀█ █▀▀█ 　 █▀▀█ █▀▀█ █▀▀█ █▀▀ █── 　 █▀▀█ 　 ▀▀█▀▀ ─▀─ ──▀ █▀▀ █▀▀█ █▀▀█ 
░█▄▄█ ▀█▀ █▀▀ █──█ █▄▄▀ █▄▄█ 　 █──█ █▄▄█ █──█ █▀▀ █── 　 █──█ 　 ──█── ▀█▀ ──█ █▀▀ █▄▄▀ █▄▄█ 
░█─── ▀▀▀ ▀▀▀ ▀▀▀─ ▀─▀▀ ▀──▀ 　 █▀▀▀ ▀──▀ █▀▀▀ ▀▀▀ ▀▀▀ 　 ▀▀▀▀ 　 ──▀── ▀▀▀ █▄█ ▀▀▀ ▀─▀▀ ▀──▀
          
                         ¿SERÁS CAPAZ DE GANAR A LA MÁQUINA?\033[0m""")

rondas_jugadas = 0
rondas_ganadas_jugador = 0
rondas_ganadas_maquina = 0

while True:
    rondas_jugadas += 1
    
    print(f"""\033[90m
|| Ronda {rondas_jugadas} ||\033[0m""")
    print("\033[90mElige una opción \033[0m\033[94m(piedra, papel, tijera)\033[0m")
    jugador = input().lower()
    
    if jugador not in ["piedra", "papel", "tijera"]:
        print("¡Opción inválida! Elige nuevamente.")
        continue

    maquina = obtener_opcion_maquina()
    print(f"\033[92m--> Has elegido: {jugador}\033[0m")

    resultado = determinar_ganador(jugador, maquina)
    print(f"""\033[36m--> La máquina eligió: {maquina}\033[0m          
          """)
    print(f"Resultado: {resultado}")

    if resultado == "Ganaste a la máquina ^_^":
        rondas_ganadas_jugador += 1
    elif resultado == "La máquina te ha ganado -_-":
        rondas_ganadas_maquina += 1

    jugar_nuevamente = input("\033[38;5;214m¿Quieres jugar de nuevo? (s/n):\033[0m ")
    if jugar_nuevamente.lower() != "s":
        break

print(f"\033[90mHas jugado {rondas_jugadas} rondas: Has ganado {rondas_ganadas_jugador} y la máquina ha ganado {rondas_ganadas_maquina}.\033[0m")
