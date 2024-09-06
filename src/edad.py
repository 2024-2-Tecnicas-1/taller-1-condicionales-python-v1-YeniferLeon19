from datetime import datetime
def evaluar(dia, mes, anno):
  
    fecha_actual = datetime.now()
    dia_actual = fecha_actual.day
    mes_actual = fecha_actual.month
    anno_actual = fecha_actual.year

    edad = anno_actual - anno

    if (mes > mes_actual) or (mes == mes_actual and dia > dia_actual):
        edad -= 1
    return f"Usted tiene {edad} años"

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
