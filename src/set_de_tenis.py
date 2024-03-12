def evaluar(num_victorias_a, num_victorias_b):
    if num_victorias_a < 0 or num_victorias_b < 0 or num_victorias_b > 7 or num_victorias_a > 7 or num_victorias_b == num_victorias_a == 7 or (num_victorias_a == 7 and num_victorias_b <= 4) or (num_victorias_b == 7 and num_victorias_a <= 4):
        return'Inválido'
    elif num_victorias_a == 7 and num_victorias_b == 6:        
        return'Ganó A'
    elif num_victorias_b == 7 and num_victorias_a == 6:
        return'Ganó B'
    elif num_victorias_b <= 7 and num_victorias_a <= 7 and num_victorias_a - num_victorias_b >= 2 and num_victorias_a >= 6:
        return 'Ganó A'
    elif num_victorias_b <= 7 and num_victorias_a <= 7 and num_victorias_b - num_victorias_a >= 2 and num_victorias_b >= 6:
        return'Ganó B'
    elif num_victorias_a - num_victorias_b == 1 or num_victorias_b - num_victorias_a == 1 or num_victorias_a - num_victorias_b == 0 and num_victorias_b <= 7 and num_victorias_a <=7 and num_victorias_b != 7 and num_victorias_a != 7 or (num_victorias_a < 6) - num_victorias_b <= 2 or (num_victorias_b < 6) - num_victorias_a <=2:
        return'Aún no termina'  
    
        
    return "";

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)