def evaluar(a, b, c):
    if a <0 or b < 0 or c < 0 or a + b < c or c + b < a or c + a < b:
        return "No es un triángulo válido"
    elif a == b and b == c and a == c:
        return "El triángulo es equilátero"
    elif a != b and a != c and b != c:
        return "El triángulo es escaleno"
    elif a == b or b == c or c == a:
        return "El triángulo es isóceles"     
    
    return "";

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)