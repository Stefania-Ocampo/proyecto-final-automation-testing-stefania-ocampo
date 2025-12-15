# Proyecto Final Automation Testing – Stefania Ocampo

## Propósito del proyecto
Desarrollar un framework de automatización de pruebas completo en Python,
que incluya pruebas de interfaz (UI) y pruebas de API, aplicando buenas
prácticas de testing automatizado.

---

##  Tecnologías utilizadas
- Python 3
- Pytest
- Selenium WebDriver
- Requests
- pytest-html
- Faker
- Git / GitHub

---

## Estructura del proyecto
pages/ -> Page Object Model (UI)
tests/
├─ ui/ -> Tests de interfaz
└─ api/ -> Tests de API
utils/ -> Lectura de datos y utilidades
data/ -> Archivos CSV de datos de prueba
reports/ -> Reportes HTML y screenshots
conftest.py -> Fixtures y hooks globales
pytest.ini -> Configuración de Pytest


---

##  Instalación
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Ejecución de pruebas
pytest

Reportes
Los reportes HTML se generan automáticamente en:

reports/report.html

Incluyen:
Estado de cada test
Duración
Capturas de pantalla en fallos UI

Tipos de pruebas implementadas
UI

Login en SauceDemo
Escenarios positivos y negativos
Page Object Model
Datos desde CSV

API

Tests sobre JSONPlaceholder
Métodos GET, POST y DELETE
Validación de respuestas y flujos encadenados

