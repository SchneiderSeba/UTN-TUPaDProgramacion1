print("➖➖➖➖➖➖ Ta - Te - Ti ➖➖➖➖➖➖➖➖")

Matriz_3x3 = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]

turn = 'x'
Raid_Done = False

def check_win():
    for i in range(3):
        if (Matriz_3x3[i][0] == Matriz_3x3[i][1] == Matriz_3x3[i][2] != "-"):
            return True
        if (Matriz_3x3[0][i] == Matriz_3x3[1][i] == Matriz_3x3[2][i] != "-"):
            return True
    if (Matriz_3x3[0][0] == Matriz_3x3[1][1] == Matriz_3x3[2][2] != "-") or \
       (Matriz_3x3[0][2] == Matriz_3x3[1][1] == Matriz_3x3[2][0] != "-"):
        return True
    return False

while not Raid_Done:
    for row in Matriz_3x3:
        print(" ".join(row))

    row = int(input(f"Turno de '{turn.upper()}'. Ingrese fila (1-3): ")) - 1
    col = int(input(f"\nTurno de '{turn.upper()}'. Ingrese columna (1-3): ")) - 1

    if Matriz_3x3[row][col] == '-':
        Matriz_3x3[row][col] = turn
        if check_win():
            for row in Matriz_3x3:
                print(" ".join(row))
                        
            print(f"\n¡Felicidades! El jugador '{turn.upper()}' ha ganado.")
            Raid_Done = True   

        turn = 'o' if turn == 'x' else 'x'
    else:
        print("\nEsa posición ya está ocupada. Intente de nuevo.")

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")