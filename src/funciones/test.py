import pyautogui
import time

def insertar_una_fila_mn(dia,mes):
    
    fecha = f"{dia}{mes}2025"

    time.sleep(5)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    pyautogui.hotkey("alt", "n")
    time.sleep(0.5)

    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.typewrite(fecha, interval=0.1)
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.3)
    pyautogui.press("down")

    pyautogui.press("enter")
    time.sleep(0.3)

    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")

    # Fin del encabezado

    pyautogui.press("enter")
    time.sleep(0.6)

    pyautogui.press("f1")
    time.sleep(0.4)
    pyautogui.typewrite("1041", interval=0.05)
    time.sleep(0.7)
    pyautogui.press("enter")

    time.sleep(2)
    for _ in range(6):
        pyautogui.press("enter")
        time.sleep(0.15)

    time.sleep(1.0)
    pyautogui.hotkey("alt", "tab")
    time.sleep(1.0)

    pyautogui.press("right")
    time.sleep(1)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.7)

    pyautogui.press("down")
    pyautogui.press("left")
    time.sleep(0.7)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1.5)

    pyautogui.moveTo(546, 478)
    pyautogui.click(button="right")
    time.sleep(0.5)

    for _ in range(4):
        pyautogui.press("down")
        time.sleep(0.3)

    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.typewrite("999", interval=0.05)
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.hotkey("alt", "s")
    time.sleep(0.5)
    pyautogui.hotkey("alt", "s")
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(1.0)

    pyautogui.hotkey("alt", "tab")
def insertar_una_fila_mn_mayor_3000(dia,mes):
    fecha = f"{dia}{mes}2025"

    time.sleep(5)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    pyautogui.hotkey("alt", "n")
    time.sleep(0.5)

    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.typewrite(fecha, interval=0.1)
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.3)
    pyautogui.press("down")

    pyautogui.press("enter")
    time.sleep(0.3)

    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.press("enter")

    # Fin del encabezado

    pyautogui.press("enter")
    time.sleep(0.6)

    pyautogui.press("f1")
    time.sleep(0.4)
    pyautogui.typewrite("1041", interval=0.05)
    time.sleep(0.7)
    pyautogui.press("enter")

    time.sleep(2)
    for _ in range(6):
        pyautogui.press("enter")
        time.sleep(0.15)

    time.sleep(1.0)
    pyautogui.hotkey("alt", "tab")
    time.sleep(1.0)

    pyautogui.press("right")
    time.sleep(1)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.7)

    pyautogui.press("down")
    pyautogui.press("left")
    time.sleep(0.7)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1.5)

    pyautogui.moveTo(546, 478)
    pyautogui.click(button="right")
    time.sleep(0.5)

    for _ in range(4):
        pyautogui.press("down")
        time.sleep(0.3)

    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.typewrite("999", interval=0.05)
    time.sleep(0.5)

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

    pyautogui.hotkey("alt", "tab")
def insertar_varias_filas_mn(dia,mes,rep):

    fecha = f"{dia}{mes}2025"

    time.sleep(4)
    for i in range(int(rep)):  # repetir 4 veces
        time.sleep(1)

        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.5)

        pyautogui.hotkey("alt", "tab")
        time.sleep(1)

        pyautogui.hotkey("alt", "n")
        time.sleep(0.5)

        pyautogui.press("enter")
        time.sleep(0.5)

        pyautogui.typewrite(fecha, interval=0.1)
        time.sleep(0.5)

        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.3)
        pyautogui.press("down")

        pyautogui.press("enter")
        time.sleep(0.3)

        pyautogui.press("enter")
        time.sleep(0.5)

        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)

        pyautogui.press("enter")
        pyautogui.press("enter")

        # Fin del encabezado

        pyautogui.press("enter")
        time.sleep(0.6)

        pyautogui.press("f1")
        time.sleep(0.4)
        pyautogui.typewrite("1041", interval=0.05)
        time.sleep(0.7)
        pyautogui.press("enter")

        time.sleep(2)
        for _ in range(6):
            pyautogui.press("enter")
            time.sleep(0.15)

        time.sleep(1.0)
        pyautogui.hotkey("alt", "tab")
        time.sleep(1.0)

        pyautogui.press("right")
        time.sleep(1)

        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.7)

        pyautogui.press("down")
        pyautogui.press("left")
        time.sleep(0.7)

        pyautogui.hotkey("alt", "tab")
        time.sleep(1.5)

        pyautogui.moveTo(546, 478)
        pyautogui.click(button="right")
        time.sleep(0.5)

        for _ in range(4):
            pyautogui.press("down")
            time.sleep(0.3)

        pyautogui.press("enter")
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.5)

        pyautogui.typewrite("999", interval=0.05)
        time.sleep(0.5)

        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.5)

        pyautogui.hotkey("alt", "s")
        time.sleep(0.5)
        pyautogui.hotkey("alt", "s")
        time.sleep(0.5)

        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(1.0)

        pyautogui.hotkey("alt", "tab")

        # espera larga entre ciclos para que todo se procese bien
        time.sleep(2)
def insertar_varias_filas_mn_mayor_3000(dia,mes,rep):
    fecha = f"{dia}{mes}2025"

    time.sleep(4)
    for i in range(int(rep)):  # repetir 4 veces
        time.sleep(1)

        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.5)

        pyautogui.hotkey("alt", "tab")
        time.sleep(1)

        pyautogui.hotkey("alt", "n")
        time.sleep(0.5)

        pyautogui.press("enter")
        time.sleep(0.5)

        pyautogui.typewrite(fecha, interval=0.1)
        time.sleep(0.5)

        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.3)
        pyautogui.press("down")

        pyautogui.press("enter")
        time.sleep(0.3)

        pyautogui.press("enter")
        time.sleep(0.5)

        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)

        pyautogui.press("enter")
        pyautogui.press("enter")

        # Fin del encabezado

        pyautogui.press("enter")
        time.sleep(0.6)

        pyautogui.press("f1")
        time.sleep(0.4)
        pyautogui.typewrite("1041", interval=0.05)
        time.sleep(0.7)
        pyautogui.press("enter")

        time.sleep(2)
        for _ in range(6):
            pyautogui.press("enter")
            time.sleep(0.15)

        time.sleep(1.0)
        pyautogui.hotkey("alt", "tab")
        time.sleep(1.0)

        pyautogui.press("right")
        time.sleep(1)

        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.7)

        pyautogui.press("down")
        pyautogui.press("left")
        time.sleep(0.7)

        pyautogui.hotkey("alt", "tab")
        time.sleep(1.5)

        pyautogui.moveTo(546, 478)
        pyautogui.click(button="right")
        time.sleep(0.5)

        for _ in range(4):
            pyautogui.press("down")
            time.sleep(0.3)

        pyautogui.press("enter")
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.5)

        pyautogui.typewrite("999", interval=0.05)
        time.sleep(0.5)

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

        pyautogui.hotkey("alt", "tab")

        # espera larga entre ciclos para que todo se procese bien
        time.sleep(2)
def insertar_una_fila_me(dia,mes):
    fecha = f"{dia}{mes}2025"

    time.sleep(5)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.3)

    pyautogui.hotkey("alt", "tab")
    time.sleep(0.7)

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

    pyautogui.hotkey("ctrl", "v")
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
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    pyautogui.press("right")
    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.7)

    pyautogui.press("down")
    pyautogui.press("left")
    time.sleep(0.3)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    pyautogui.moveTo(546, 478)
    pyautogui.click(button="right")
    time.sleep(0.7)

    for _ in range(4):
        pyautogui.press("down")
        time.sleep(0.25)

    pyautogui.press("enter")
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
    pyautogui.hotkey("alt", "tab")
def insertar_una_fila_me_mayor_1000(dia,mes):
    fecha = f"{dia}{mes}2025"

    time.sleep(5)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.3)

    pyautogui.hotkey("alt", "tab")
    time.sleep(0.7)

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

    pyautogui.hotkey("ctrl", "v")
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

    for _ in range(6):
        pyautogui.press("enter")
        time.sleep(0.15)

    time.sleep(1.2)
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    pyautogui.press("right")
    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.7)

    pyautogui.press("down")
    pyautogui.press("left")
    time.sleep(0.3)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    pyautogui.moveTo(546, 478)
    pyautogui.click(button="right")
    time.sleep(0.7)

    for _ in range(4):
        pyautogui.press("down")
        time.sleep(0.25)

    pyautogui.press("enter")
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
    time.sleep(1)
    pyautogui.hotkey("alt", "tab")
def insertar_varias_filas_me(dia,mes,rep):
    fecha = f"{dia}{mes}2025"
    time.sleep(4)
    for i in range(int(rep)):  # repetir 4 veces
        time.sleep(1)

        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.3)

        pyautogui.hotkey("alt", "tab")
        time.sleep(0.7)

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

        pyautogui.hotkey("ctrl", "v")
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
        pyautogui.hotkey("alt", "tab")
        time.sleep(1)

        pyautogui.press("right")
        time.sleep(0.5)

        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.7)

        pyautogui.press("down")
        pyautogui.press("left")
        time.sleep(0.3)

        pyautogui.hotkey("alt", "tab")
        time.sleep(1)

        pyautogui.moveTo(546, 478)
        pyautogui.click(button="right")
        time.sleep(0.7)

        for _ in range(4):
            pyautogui.press("down")
            time.sleep(0.25)

        pyautogui.press("enter")
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
        pyautogui.hotkey("alt", "tab")

        # espera larga entre ciclos para que todo se procese bien
        time.sleep(2)
def insertar_varias_filas_me_mayor_1000(dia,mes,rep):
    fecha = f"{dia}{mes}2025"
    time.sleep(4) 
    for _ in range(int(rep)):
        time.sleep(1)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.3)

        pyautogui.hotkey("alt", "tab")
        time.sleep(0.7)

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

        pyautogui.hotkey("ctrl", "v")
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
        pyautogui.hotkey("alt", "tab")
        time.sleep(1)

        pyautogui.press("right")
        time.sleep(0.5)

        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.7)

        pyautogui.press("down")
        pyautogui.press("left")
        time.sleep(0.3)

        pyautogui.hotkey("alt", "tab")
        time.sleep(1)

        pyautogui.moveTo(546, 478)
        pyautogui.click(button="right")
        time.sleep(0.7)

        for _ in range(4):
            pyautogui.press("down")
            time.sleep(0.25)

        pyautogui.press("enter")
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
        time.sleep(1)
        pyautogui.hotkey("alt", "tab")


        #A partir de mil sale el problema del otro yes or no
        time.sleep(2)