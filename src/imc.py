def evaluar(peso, estatura, edad):
    imc = peso / (estatura * estatura)
    if imc < 22.0 :
        if edad >= 45:
            return "medio"
        else:
            return "bajo"
    else:
        if edad >= 45:
            return "alto"
        else:
            return "medio"
if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
