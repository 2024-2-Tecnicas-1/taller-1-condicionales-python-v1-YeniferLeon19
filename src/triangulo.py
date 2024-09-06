def evaluar(a, b, c):
    if a < (b + c) and b < (a + c) and c < (a + b):
        if a == b == c:
            return "El triángulo es equilátero"
        elif a == b or b == c or a == c:
            return "El triángulo es isósceles"
        else:
            return "El triángulo es escaleno"
    else:
        return "No es un triángulo válido"



if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
