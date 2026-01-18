# 🤖 Automatizar Cosas Aburridas

> Automatización de tareas repetitivas de digitación en StarSoft usando Python y PyAutoGUI

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

---

## 📋 Descripción

Este proyecto nace de la necesidad de optimizar tareas repetitivas en el trabajo de digitación. Como humanos, somos propensos a cometer errores al ingresar datos manualmente (números, letras, etc.). Este script automatiza el proceso de registro de movimientos en el sistema **StarSoft**, reduciendo errores y ahorrando tiempo valioso.

### 🎯 Objetivo

Automatizar la entrada de datos en StarSoft para:
- ✅ Reducir errores humanos en la digitación
- ⚡ Acelerar procesos repetitivos
- 🕐 Liberar tiempo para tareas más importantes
- 📊 Procesar múltiples registros desde archivos CSV

---

## ✨ Características

- 🔄 **Lectura automática** de archivos CSV con información de movimientos
- 🖱️ **Control automático** de teclado y mouse mediante PyAutoGUI
- 💱 **Soporte para múltiples monedas** (MN - Moneda Nacional, ME - Moneda Extranjera)
- 💰 **Detección de montos mayores** con confirmaciones adicionales
- 📝 **Procesamiento por lotes** de múltiples registros
- ⚙️ **Configuración flexible** de parámetros

---

## 🛠️ Requisitos

### Sistema Operativo
- Windows (probado y validado)

### Software
- Python 3.8 o superior
- StarSoft (debe estar instalado y configurado)

### Dependencias Python
```bash
pyautogui
csv (biblioteca estándar)
```

---

## 📦 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/ChopperNakama/Automatizar-Cosas-Aburridas.git
   cd Automatizar-Cosas-Aburridas
   ```

2. **Instalar dependencias**
   ```bash
   pip install pyautogui
   ```

3. **Preparar el archivo de datos**
   - Crear una carpeta `data/` en la raíz del proyecto
   - Colocar tu archivo `archivo.csv` en `data/archivo.csv`

---

## 🚀 Uso

### Formato del archivo CSV

El archivo CSV debe tener el siguiente formato:

```csv
Fecha,Descripción,Cargo,Detalle
2025-01-15,Compra de materiales,1500.00,Material de oficina
2025-01-16,Servicio de internet,850.50,Internet mensual
```

**Campos:**
- `Fecha`: Formato YYYY-MM-DD
- `Descripción`: Descripción del movimiento
- `Cargo`: Monto numérico del movimiento
- `Detalle`: Detalle adicional del registro

### Ejecutar el script

```bash
cd src
python main.py
```

### ⚠️ Importante antes de ejecutar

1. **StarSoft debe estar abierto** y en la pantalla correcta
2. **No muevas el mouse** ni uses el teclado durante la ejecución
3. **Espera 4 segundos** después de iniciar el script (tiempo de preparación)
4. Asegúrate de que las **coordenadas de la pantalla** coincidan con tu configuración

---

## 📁 Estructura del Proyecto

```
Automatizar-Cosas-Aburridas/
│
├── src/
│   ├── main.py              # Punto de entrada principal
│   ├── cli/
│   │   └── start.py         # Lógica de inicio y decisiones
│   └── logica/
│       └── funciones.py     # Funciones de automatización con PyAutoGUI
│
├── data/
│   └── archivo.csv          # Archivo de datos de entrada (crear)
│
└── README.md                # Este archivo
```

### 📄 Descripción de módulos

- **`main.py`**: Lee el archivo CSV y procesa cada registro
- **`cli/start.py`**: Determina el tipo de moneda y si el monto supera límites
- **`logica/funciones.py`**: Ejecuta la automatización usando PyAutoGUI

---

## 🔧 Configuración

### Límites de montos

En `src/cli/start.py` se definen los límites para montos mayores:

```python
if tipo_moneda == "ME":
    mayor = total >= 1000  # Moneda Extranjera
else:  # MN
    mayor = total >= 3000  # Moneda Nacional
```

### Tipo de moneda predeterminado

```python
tipo_moneda = "ME"   # Cambiar a "MN" para Moneda Nacional
```

---

## 🔍 Tecnologías Utilizadas

- **Python 3**: Lenguaje de programación principal
- **PyAutoGUI**: Automatización de GUI (teclado y mouse)
- **CSV**: Procesamiento de archivos de datos
- **Time**: Gestión de tiempos de espera

---

## 📝 Notas Importantes

1. ⚠️ **Ventana activa**: StarSoft debe estar en primer plano antes de ejecutar
2. 🖥️ **Resolución de pantalla**: Las coordenadas pueden variar según la resolución
3. ⏱️ **Tiempos de espera**: Ajustados para un funcionamiento óptimo, pueden necesitar calibración
4. 🔒 **Datos sensibles**: No incluyas información confidencial en el repositorio
5. 🧪 **Pruebas**: Se recomienda probar primero con pocos registros

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o tienes sugerencias:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autor

**ChopperNakama**

- GitHub: [@ChopperNakama](https://github.com/ChopperNakama)

---

## 🙏 Agradecimientos

- Gracias a la comunidad de PyAutoGUI por esta increíble librería
- A todos los que enfrentan tareas repetitivas y buscan automatizarlas
- Al poder de Python para hacer la vida más fácil

---

<div align="center">
  
**¡Si este proyecto te ayudó, considera darle una ⭐ en GitHub!**

*Hecho con ❤️ y Python*

</div>
