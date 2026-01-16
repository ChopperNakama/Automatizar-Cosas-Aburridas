import Auto.Test.test as test

def start():
    tm, d, m, es_unica, mayor = preguntas()
    
    if tm == "MN":
        if es_unica:
            if mayor:
                test.insertar_una_fila_mn_mayor_3000(d, m)
            else:
                test.insertar_una_fila_mn(d, m)
        else:
            rep = int(input("Ingrese la cantidad: "))
            if mayor:
                test.insertar_varias_filas_mn_mayor_3000(d, m, rep)
            else:
                test.insertar_varias_filas_mn(d, m, rep)
    elif tm == "ME":
        if es_unica:
            if mayor:
                test.insertar_una_fila_me_mayor_1000(d,m) 
            else:
                test.insertar_una_fila_me(d,m) 
        else:
            rep = int(input("Ingresa la cantidad: "))
            if mayor:
                test.insertar_varias_filas_me_mayor_1000(d,m,rep)
            else:
                test.insertar_varias_filas_me(d,m,rep)

def preguntas():
    tipo_moneda = input("Es ME o MN: ").strip().upper()
    dia = input("Ingresa el día: ")
    mes = input("Ingresa el mes: ")
    es_unica = input("Es única? (1=Si/0=No): ") == "1"

    mayor = False
    if tipo_moneda == "ME":
        mayor = input("Es mayor de 1000? (1=Si/0=No): ") == "1"
    elif tipo_moneda == "MN":
        mayor = input("Es mayor de 3000? (1=Si/0=No): ") == "1"

    return tipo_moneda, dia, mes, es_unica, mayor