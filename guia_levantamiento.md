# Guía de Levantamiento — Django Práctico 3

Guía paso a paso para instalar dependencias, configurar y ejecutar el proyecto Django 6 con SQLite3.

---

## Requisitos

- Python 3.10+
- pip (gestor de paquetes de Python)

---

## 1. Clonar o ubicarse en el proyecto

```bash
cd /ruta/del/proyecto/django-practico3
```

---

## 2. Crear y activar el entorno virtual

```bash
# Crear el entorno virtual
python -m venv venv

# Activar (Linux/macOS)
source venv/bin/activate

# Activar (Windows - PowerShell)
venv\Scripts\activate

# Activar (Windows - CMD)
venv\Scripts\activate.bat
```

Verás `(venv)` al inicio del prompt, indicando que el entorno virtual está activo.

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Esto instala Django y las dependencias necesarias.

---

## 4. Aplicar migraciones

```bash
python django_project/manage.py migrate
```

Crea la base de datos SQLite3 (`db.sqlite3`) con las tablas del sistema.

---

## 5. (Opcional) Crear superusuario para el admin

```bash
python django_project/manage.py createsuperuser
```

Te pedirá nombre de usuario, email y contraseña.

---

## 6. Ejecutar el servidor de desarrollo

```bash
python django_project/manage.py runserver
```

Salida esperada:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

Django version 6.0.5, using settings 'django_practico3.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

## 7. Navegar por el sitio

| URL | Descripción |
|---|---|
| `http://127.0.0.1:8000/` | Página de inicio |
| `http://127.0.0.1:8000/contacto/` | Formulario de contacto con validación backend |
| `http://127.0.0.1:8000/admin/` | Panel de administración (requiere superusuario) |

---

## Estructura del proyecto

```
django-practico3/
├── venv/                          # Entorno virtual
├── django_project/                # Proyecto Django
│   ├── manage.py                  # CLI de Django
│   ├── db.sqlite3                 # Base de datos SQLite (se crea con migrate)
│   ├── django_practico3/          # Configuración del proyecto
│   │   ├── settings.py            # Configuración (apps, db, templates)
│   │   ├── urls.py                # URLs raíz
│   │   └── ...
│   └── core/                      # App principal
│       ├── views.py               # Vistas (lógica de negocio)
│       ├── forms.py               # Formulario con validación backend
│       ├── urls.py                # URLs de la app
│       └── templates/
│           ├── base.html          # Plantilla base (header, navbar, footer)
│           └── core/
│               ├── index.html     # Página de inicio
│               └── contacto.html  # Formulario de contacto
├── tutorial_plantillas.md         # Tutorial conceptual de plantillas
├── guia_levantamiento.md          # Esta guía
└── requirements.txt               # Dependencias del proyecto
```

---

## Detalles técnicos

### Base de datos

SQLite3 se configura por defecto en `django_practico3/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### Formulario con validación backend

El formulario se define en `core/forms.py` usando `django.forms.Form`. Incluye:

- Validación de tipo de campo (email válido, longitud mínima/máxima).
- Validación personalizada con `clean_nombre()` y `clean_mensaje()`.
- Validadores como `RegexValidator` y `EmailValidator`.

### Plantillas con herencia

- `base.html` -> Contiene header, navbar y footer comunes.
- `index.html` y `contacto.html` -> Heredan de `base.html` y solo definen su contenido único mediante bloques `{% block %}`.
