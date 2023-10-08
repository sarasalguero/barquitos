import funciones as fn
import variables as var
import numpy as np
import random


def jugar_hundir_la_flota():
    fn.mensaje_bienvenida()

    modo_juego = input("Elige un modo de juego (demo/partida real): ").lower()

    if modo_juego not in ["demo", "partida real"]:
        print("Modo de juego no válido. Elige 'demo' o 'partida real'.")
        return


    tablero_connor = fn.crear_tablero()
    tablero_terminator_original = fn.crear_tablero()
    tablero_terminator_reflejo = fn.crear_tablero()

    if modo_juego == "demo":
        vidas_connor = 2
        vidas_terminator = 2

        fn.colocar_barcos_random(tablero_terminator_original, var.esloras_demo)
        fn.colocar_barcos_random(tablero_connor, var.esloras_demo)

    else:
        vidas_connor = 20
        vidas_terminator = 20
        
        fn.colocar_barcos_random(tablero_terminator_original, var.esloras_reales)
        fn.colocar_barcos_random(tablero_connor, var.esloras_reales)


    while True:
        fn.mostrar_tableros(tablero_connor, tablero_terminator_original, tablero_terminator_reflejo)
        fn.disparar_connor(tablero_connor, tablero_terminator_original, vidas_connor, vidas_terminator)
        
        if vidas_connor == 0:
            print("¡Has perdido!")
            break
        elif vidas_terminator == 0:
            print("¡Has ganado!")
            break
        break

fn.jugar_hundir_la_flota()