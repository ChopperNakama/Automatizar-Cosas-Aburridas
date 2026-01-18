import logica.funciones as funciones


def start(d, m, t, De):
    """
    Punto de entrada principal.
    Decide tipo de moneda y si el monto es mayor,
    luego inserta el registro correspondiente.
    """

    tipo_moneda, mayor = preguntas(t)

    # es_mn es True solo si la moneda es MN
    es_mn = tipo_moneda == "MN"

    funciones.insertar_registro(
        dia=d,
        mes=m,
        detalle=De,
        total=t,
        es_mn=es_mn,
        monto_mayor=mayor
    )


def preguntas(total):
    """
    Determina el tipo de moneda y si el monto
    supera el límite permitido.
    """

    # Fijado por ahora para agilizar
    tipo_moneda = "ME"   # "MN" o "ME"

    if tipo_moneda == "ME":
        mayor = total >= 1000
    else:  # MN
        mayor = total >= 3000

    return tipo_moneda, mayor
