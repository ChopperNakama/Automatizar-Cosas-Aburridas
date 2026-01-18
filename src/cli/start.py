import logica.funciones as funciones

def start(d,m,t,De):
    tm, mayor = preguntas(t)
    
    if tm == "MN":
        if mayor:
            funciones.insertar_un_registro_mn_mayor_3000_final(d,m,De,t)
        else:
            funciones.insertar_un_registro_mn_final(d,m,De,t)
    elif tm == "ME":
        if mayor:
            funciones.insertar_un_registro_me_mayor_1000_final(d,m,De,t)
        else:
            funciones.insertar_un_registro_me_final(d,m,De,t)
def preguntas(total):
    # tipo_moneda = input("Es ME o MN: ").strip().upper() para agilizar pq estoy en MN
    tipo_moneda = "ME"

    mayor = False
    if tipo_moneda == "ME":
        mayor = total>=1000
    elif tipo_moneda == "MN":
        mayor = total>=3000

    return tipo_moneda, mayor