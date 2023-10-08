import variables as var
import numpy as np
import random

def crear_tablero(tamaño=(10,10)):
    '''
    Esta función crea tableros.

    Tan solo has de introducir dos parámetros para crear un tablero a tu gusto.
    Si no introduces ningún argumento, el tamaño por defecto será de 10x10.
    Por defecto, las casillas estarán en blanco. Este atributo no se puede modificar.
    '''
    return np.full(tamaño, ".")


def actualizar_tablero_reflejo(tablero_original, tablero_reflejo):
    for fila in range(len(tablero_original)):
        for columna in range(len(tablero_original[0])):
            if tablero_original[fila][columna] == "X" or tablero_original[fila][columna] == "-":
                tablero_reflejo[fila][columna] = tablero_original[fila][columna]


def mostrar_tableros(tablero_connor, tablero_terminator_original, tablero_terminator_reflejo):
    '''
    Esta función imprime los tableros por pantalla en el inicio de forma que verás los tres tableros posibles.
    Tiene 3 argumentos:
    1. El tablero de Connor, la jugadora.
    2. El tablero de Terminator, la máquina.
    3. El tablero de Terminator reflejo. Este tablero no mostrará los barcos, solo los disparos que lance Connor.
    '''
    print("\nTablero de Connor:")
    for fila in tablero_connor:
        print(" ".join(fila))
    
    print("\nTablero de Terminator:")
    for fila in tablero_terminator_original:
        print(" ".join(fila))

    print("\nTablero reflejo de Terminator:")
    for fila in tablero_terminator_reflejo:
        print(" ".join(fila))



def crear_barco_random(eslora, tablero):
    '''
    Esta función sirve para crear barcos aleatorios en nuestro tablero.

    Tiene dos parámetros:
    1. Eslora: Esta es la longitud del barco, es decir, cuántas casillas va a ocupar en el tablero.
    2. Tablero: El tablero donde se coloca el barco.

    El barco se colocará en el tablero de forma aleatoria eligiendo su situación y la orientación en la que crece (N, S, E, O).

    Además, se asegurará de que el barco no excedan los límites del tablero y de que las coordenadas del barco son consecutivas. Una maravilla de función, oiga.
    '''
    barco_random = []

    orientacion = random.choice(["N", "S", "E", "O"])

    fila_random = random.randint(0, 9)
    columna_random = random.randint(0, 9)


    if orientacion == "N":
        while fila_random - eslora + 1 < 0:
            fila_random = random.randint(0, 9)
        for i in range(eslora):
            barco_random.append((fila_random - i, columna_random))
    elif orientacion == "S":
        while fila_random + eslora - 1 > 9:
            fila_random = random.randint(0, 9)
        for i in range(eslora):
            barco_random.append((fila_random + i, columna_random))
    elif orientacion == "E":
        while columna_random + eslora - 1 > 9:
            columna_random = random.randint(0, 9)
        for i in range(eslora):
            barco_random.append((fila_random, columna_random + i))
    elif orientacion == "O":
        while columna_random - eslora + 1 < 0:
            columna_random = random.randint(0, 9)
        for i in range(eslora):
            barco_random.append((fila_random, columna_random - i))
    else:
        print("La orientación que has introducido no es válida.")

    if all(tablero[fila][columna] == "."
        for fila, columna in barco_random):
        return barco_random
    else:
        return crear_barco_random(eslora, tablero)


def colocar_barco(barco, tablero):
    '''
    Esta función sirve para colocar tus barcos en el tablero.
    Sirve tanto para barcos custom como para barcos generados de manera aleatoria.
    
    Tiene dos parámetros:
    1. Barco. Introduce aquí la variable del barco que desees añadir.
    2. Tablero. Di en qué tablero lo quieres añadir.
    '''
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero


def colocar_barcos_random(tablero, esloras_posibles):
    '''
    Esta función sirve para colocar tus barcos random en el tablero.

    Tiene dos parámetros:
    1. Tablero: el tablero donde se colocarán los barcos.
    2. Esloras_posibles: es una lista de esloras posibles para los barcos aleatorios, se puede meter como lista en la función o usando una variable tipo lista.

    Los barcos se colocarán en el tablero de forma aleatoria eligiendo su situación y la orientación en la que crece (N, S, E, O).

    Además, se asegurará de que los barcos no excedan los límites del tablero y de que las coordenadas de los barcos sean consecutivas.
    '''

    for eslora in esloras_posibles:
        barco = crear_barco_random(eslora, tablero)
        for casilla in barco:
            tablero[casilla] = "O"

    return tablero



def disparar_connor(tablero_connor, tablero_terminator_original, vidas_connor, vidas_terminator):
    '''
    La finalidad de esta función es atacar a tu contrincante disparando a un punto concreto.
    
    Tiene cuatro parámetros.
    1. Tablero connor: es el tablero del jugador. Lo añadimos porque después vamos a llamar de forma interna a la función de disparos de Terminator y necesitamos pedirle el argumento de inicio.
    2. Tablero de terminator original: este es el tablero al que atacará esta función.
    3. Vidas connor: necesita saber cuántas vidas tiene para actualizarlas después de cada "Tocado" y terminar la partida cuando llegue a 0.
    4. Vidas terminator: necesita saber cuántas vidas tiene para actualizarlas después de cada "Tocado" y terminar la partida cuando llegue a 0.
    '''
    disparos_terminator = []

    while vidas_connor > 0 and vidas_terminator > 0:
        print("Connor, es el momento de elegir las coordenadas para disparar a Terminator.\n")
    
        fila_disparo = int(input("Introduce la fila de la coordenada a la que deseas atacar"))
        columna_disparo = int(input("Ahora, introduce la columna de la coordenada a la que deseas atacar"))
        casilla = (fila_disparo, columna_disparo)
        print(f"Tu disparo a la casilla {casilla} está en camino. Suerte, Sarah.\n")

        if tablero_terminator_original[casilla] == ".":
            print("Agüita. Has fallado. ¡Es el turno del cyborg!\n")
            tablero_terminator_original[casilla] = "~"
            print(tablero_terminator_original)
            disparar_terminator(tablero_connor, disparos_terminator, vidas_connor)

        elif tablero_terminator_original[casilla] == "O":
            tablero_terminator_original[casilla] = "X"
            print(tablero_terminator_original)
            vidas_terminator -= 1
            print(f"¡¡Tocado!! ¡Bien, Connor! El cyborg está cada vez más débil, solo tiene {vidas_terminator} vidas. ¡Sigue así!\n")

        if vidas_connor == 0:
            print("Terminator ha vencido. Connor, has perdido todas tus vidas.\nSkynet se ha unido a ChatGPT para terminar con todo.\nSayonara, baby.")
            break
        elif vidas_terminator == 0:
            print("Terminator ha perdido todas sus vidas.\nSarah Connor, ¡enhorabuena, has vencido al Cyborg!\nEs hora de decirle: sayonara, baby.")
            break



def disparar_terminator(tablero, disparos_terminator, vidas_connor):
    '''
    Esta función genera disparos de manera aleatoria.

    Tiene tres argumentos de entrada:
    1. Tablero: es el tablero de Connor, al que vamos a atacar.
    2. Disparos_terminator: acceso a una lista que estará en la función de disparos de Connor. Se actualiza con cada disparo de Terminator, de forma que jamás disparará dos veces al mismo sitio.
    3. Vidas connor: necesita saber cuántas vidas tiene para actualizarlas después de cada "Tocado" y terminar la partida cuando llegue a 0.
    
    No se ejecuta directamente si no que es ejecutada desde los disparos de Connor.
    '''
    while True:
        fila = random.randint(0, len(tablero) - 1)
        columna = random.randint(0, len(tablero[0]) - 1)
        casilla = (fila, columna)

        if casilla not in disparos_terminator:
            disparos_terminator.append(casilla)

            if tablero[casilla] == ".":
                print("Terminator ha fallado y ha dado en el agüita, ¡bien! Es tu turno, Connor.\n")
                tablero[casilla] = "~"
                break

            else:
                print("¡Maldicón! Terminator ha dado a uno de tus barcos, vuelve a ser tu turno... ¡suerte!\n")
                tablero[casilla] = "X"
                vidas_connor -= 1



def mensaje_bienvenida():
    print("¡Te damos la super bienvenida a Hundir la Flota versión: Sarah Connor vs. Terminator!\n")
    print("Para jugar, deberás seguir unas sencillas instrucciones:")
    print("1. Deberás elegir un modo de juego: demo o partida real.")
    print("2. En el modo demo, se jugará una partida rápida con barcos predefinidos.")
    print("3. En el modo partida real, podrás colocar tus propios barcos en el tablero.")
    print("4. Después, alternarás turnos para disparar y hundir los barcos del oponente.")
    print("5. Gana quien hunda todos los barcos del oponente primero.\n")
    print("Diviértete y... ¡¡Corre Sarah Connor, te persigue el Cyborg!!")


