import pyautogui
import time

def insertar_un_registro_mn_final(dia,mes,detalle,total):
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
    pyautogui.press("down")

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.3)

    pyautogui.typewrite(detalle,interval=0.03)
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.press("f1")
    pyautogui.typewrite("1041", interval=0.05)
    # pyautogui.press("down")
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

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.7)
def insertar_un_registro_mn_mayor_3000_final(dia,mes,detalle,total):
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
    pyautogui.press("down")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.3)

    pyautogui.typewrite(detalle,interval=0.03)
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.press("f1")
    pyautogui.typewrite("1041", interval=0.05)
    # pyautogui.press("down")
    time.sleep(0.7)
    pyautogui.press("enter")

    time.sleep(2)
    for _ in range(6):
        pyautogui.press("enter")
        time.sleep(0.15)

    pyautogui.typewrite(total, interval=0.05)
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
    time.sleep(0.5)
    pyautogui.hotkey("alt", "s")
    time.sleep(0.5)

    pyautogui.hotkey("tab")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(1.0)
def insertar_un_registro_me_final(dia,mes,detalle,total):
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

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.3)

    pyautogui.typewrite(detalle,interval=0.03)
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.press("f1")
    pyautogui.typewrite("1041", interval=0.05)
    pyautogui.press("down")
    time.sleep(0.7)
    pyautogui.press("enter")

    time.sleep(2)
    for _ in range(6):
        pyautogui.press("enter")
        time.sleep(0.15)

    time.sleep(1.2)

    pyautogui.typewrite(str(total), interval=0.05)
    time.sleep(1)

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

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.7)
def insertar_un_registro_me_mayor_1000_final(dia,mes,detalle,total):
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

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.3)

    pyautogui.typewrite(detalle,interval=0.03)
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.press("f1")
    pyautogui.typewrite("1041", interval=0.05)
    pyautogui.press("down")
    time.sleep(0.7)
    pyautogui.press("enter")

    time.sleep(2)
    for _ in range(6):
        pyautogui.press("enter")
        time.sleep(0.15)

    time.sleep(1.2)

    pyautogui.typewrite(str(total), interval=0.05)
    time.sleep(1)

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

    pyautogui.hotkey("tab")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(1)
