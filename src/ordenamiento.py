def evaluar(numero1, numero2, numero3, numero4):
        
   num = [numero1, numero2, numero3, numero4]
   numOrd = sorted(num)
   return " ".join(map(str, numOrd))
   

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = float(input())
    print("Número 2:", end="")
    numero2 = float(input())
    print("Número 3:", end="")
    numero3 = float(input())
    print("Número 4:", end="")
    numero4 = float(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)