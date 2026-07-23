nombre = input("Nombre del jugador: ")

victorias = int(input("Victorias: "))
empates = int(input("Empates: "))
derrotas = int(input("Derrotas: "))

puntaje = victorias * 3 + empates

print("\nJugador:", nombre)
print("Puntaje final:", puntaje)