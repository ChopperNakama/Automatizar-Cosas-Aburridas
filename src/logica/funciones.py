import pyautogui
import time


def insertar_registro(
    dia,
    mes,
    detalle,
    total,
    es_mn=True,
    monto_mayor=False
):
    """
    Inserta un registro usando pyautogui.

    es_mn=True  -> Movimiento Nacional
    es_mn=False -> Movimiento Extranjero

    monto_mayor=True -> requiere confirmaciones extra
    """

    fecha = f"{dia}{mes}2025"

    time.sleep(4)

    pyautogui.hotkey("alt", "n")
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(0.3)

    pyautogui.typewrite(fecha, interval=0.03)
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.3)

    # Diferencia MN / ME
    if es_mn:
        pyautogui.press("down")

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.3)

    pyautogui.typewrite(detalle, interval=0.03)
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.press("f1")
    pyautogui.typewrite("1041", interval=0.05)

    if not es_mn:
        pyautogui.press("down")

    time.sleep(0.7)
    pyautogui.press("enter")

    time.sleep(2)
    for _ in range(6):
        pyautogui.press("enter")
        time.sleep(0.15)

    pyautogui.typewrite(str(total), interval=0.05)
    time.sleep(0.7)

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.typewrite("999", interval=0.05)
    time.sleep(0.7)

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.hotkey("alt", "s")
    time.sleep(0.3)
    pyautogui.hotkey("alt", "s")
    time.sleep(0.3)

    # Diferencia por monto mayor
    if monto_mayor:
        pyautogui.hotkey("tab")
        pyautogui.press("enter")
        pyautogui.press("enter")
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(1)
    else:
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.7)
