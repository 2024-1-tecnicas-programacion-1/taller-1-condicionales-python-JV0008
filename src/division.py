def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Divisio
    cociente = int(dividendo / divisor)
    residuo = int(dividendo % divisor)
    if residuo == 0:
        respuesta = "La división es exacta. \n" \
                    "Cociente: " + str(cociente) + "\n" \
                    "Residuo: " + str(residuo)
    else:
        respuesta = "La división no es exacta. \n" \
                    "Cociente: " + str(cociente) + "\n" \
                    "Residuo: " + str(residuo)
  

    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
