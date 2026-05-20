# Tutorial de Plantillas en Django

## ¿Qué son las plantillas?

Las **plantillas (templates)** son archivos HTML con sintaxis especial de Django que permiten generar páginas web dinámicas. Separan la lógica de presentación (HTML + CSS) de la lógica de negocio (Python).

Django usa su propio motor de plantillas (*Django Template Language* o DTL) que ofrece etiquetas (`{% %}`), variables (`{{ }}`) y filtros (`{{ var|filter }}`).

---

## Principio DRY y Herencia de Plantillas

**DRY (Don't Repeat Yourself)** -> "No te repitas". En lugar de escribir el mismo header, navbar y footer en cada página, creamos una plantilla base y las demás páginas *heredan* de ella.

### Herencia con `{% extends %}`

La herencia permite que una plantilla hija herede toda la estructura de la plantilla base y solo redefina los bloques que necesite.

### Bloques con `{% block %}`

Los bloques son secciones que la plantilla base declara como reemplazables:

```html
{% block nombre_del_bloque %}
    contenido por defecto (opcional)
{% endblock %}
```

La plantilla hija los rellena con su propio contenido:

```html
{% extends 'base.html' %}
{% block nombre_del_bloque %}
    contenido específico de esta página
{% endblock %}
```

---

## Estructura del proyecto

```
templates/
├── base.html              # Plantilla base (header, navbar, footer, bloques)
└── core/
    ├── index.html          # Página de inicio (hereda de base.html)
    └── contacto.html       # Página con formulario (hereda de base.html)
```

---

## base.html — la plantilla raíz

`base.html` contiene el esqueleto HTML completo y los elementos comunes a todas las páginas:

| Elemento | Descripción |
|---|---|
| `{% load static %}` | Carga archivos estáticos |
| `{% block title %}` | Título de la página (cada página lo personaliza) |
| **Header/Navbar** | Barra de navegación con Bootstrap, con enlaces a Inicio y Contacto |
| `{% block content %}` | Contenido principal (cada página lo define) |
| **Footer** | Pie de página con copyright |

### Fragmento de base.html

```html
<!DOCTYPE html>
{% load static %}
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Django Práctico 3{% endblock %}</title>
</head>
<body>
    <header>
        <!-- Navbar común -->
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <!-- Footer común -->
    </footer>
</body>
</html>
```

### ¿Por qué usar base.html?

- **DRY**: El navbar y footer se escriben una sola vez.
- **Consistencia**: Todas las páginas tienen la misma estructura visual.
- **Mantenibilidad**: Cambiar el navbar en un solo lugar lo actualiza en todo el sitio.

---

## Navbar y Footer

### Navbar (barra de navegación)

Se coloca dentro de `<header>` en `base.html`. Contiene los enlaces de navegación del sitio. En este proyecto usa Bootstrap:

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="{% url 'index' %}">Django Práctico 3</a>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'index' %}">Inicio</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'contacto' %}">Contacto</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

### Footer (pie de página)

Se coloca al final del `<body>` en `base.html`. Puede contener copyright, enlaces legales, etc.:

```html
<footer class="bg-dark text-white text-center py-3 mt-5">
    <div class="container">
        <p class="mb-0">&copy; 2026 Django Práctico 3</p>
    </div>
</footer>
```

---

## index.html — página de inicio

Hereda de `base.html` y rellena `{% block title %}` y `{% block content %}`:

```html
{% extends 'base.html' %}

{% block title %}Inicio | Django Práctico 3{% endblock %}

{% block content %}
    <h1>Bienvenido</h1>
    <p>Contenido específico de la página de inicio.</p>
{% endblock %}
```

---

## contacto.html — página con formulario

También hereda de `base.html`. Renderiza un formulario de Django con validación backend:

```html
{% extends 'base.html' %}

{% block content %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Enviar</button>
    </form>
{% endblock %}
```

### Conceptos clave del formulario

- `{% csrf_token %}` -> Protección contra CSRF (obligatorio en formularios POST de Django).
- `{{ form }}` -> Renderiza el formulario definido en `forms.py`.
- `novalidate` en el `<form>` -> Desactiva la validación HTML5 del navegador para que solo valide el backend.
- Los errores de validación se muestran campo por campo.

---

## Patrón MTV (Model-Template-View)

Django sigue el patrón **MTV**, una variación del MVC:

| Capa | Archivo | Responsabilidad |
|---|---|---|
| **Model** | `models.py` | Define la estructura de datos (no usado en este ejercicio básico) |
| **Template** | `templates/*.html` | Presentación visual (HTML + DTL) |
| **View** | `views.py` | Lógica de negocio: procesa requests, valida formularios, renderiza templates |

### Flujo de una petición

```
Usuario → URL (urls.py) → View (views.py) → Template (HTML) → Respuesta al usuario
```

1. El usuario visita `/contacto/`.
2. `urls.py` dirige la petición a `views.contacto`.
3. La vista crea el formulario, lo valida (si es POST), y pasa datos al template.
4. El template hereda de `base.html` y renderiza el HTML completo.
5. El usuario ve la página renderizada.

---

## Resumen

- Las **plantillas** separan la presentación de la lógica.
- La **herencia** con `{% extends %}` y `{% block %}` evita repetir código (DRY).
- `base.html` contiene la estructura común: header, navbar, footer.
- Cada página hija solo define su contenido específico.
- El **patrón MTV** organiza el código en Modelos, Templates y Vistas.
- Los **formularios con validación backend** aseguran datos limpios y seguros.
