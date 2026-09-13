# Evaluación Django - Cristobal Montecinos

Proyecto de la Evaluación Sumativa N° 01 de Programación Back End. Implementa dos aplicaciones Django independientes, cada una con dos vistas HTML funcionales:

- `catalogo/`: inicio del catálogo e inventario de productos.
- `agenda/`: agenda diaria y resumen semanal.

## Ejecución local

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Rutas disponibles:

- `/` y `/productos/`
- `/agenda/` y `/agenda/semana/`
- `/admin/`

## Flujo Git de la evaluación

Las ramas de trabajo solicitadas son `montecinoscristobalrama1` y `montecinoscristobalrama2`. La primera representa el desarrollo de `catalogo` y la segunda el de `agenda`; ambas deben publicarse y fusionarse mediante Pull Requests hacia `main` en GitHub.

### Rama 1: `montecinoscristobalrama1`

Incluye la aplicación `catalogo`, con las vistas `catalogo:inicio` y `catalogo:productos`, sus templates, estilos y pruebas de integración.

### Rama 2: `montecinoscristobalrama2`

Incluye la aplicación `agenda`, con las vistas `agenda:inicio` y `agenda:semana`, sus templates, estilos y pruebas de integración.

Antes de realizar commits, configura tu identidad local:

```powershell
git config user.name "Cristobal Montecinos"
git config user.email "TU_CORREO_DE_GITHUB"
```

## Respuestas de reflexión

1. Si no se ejecuta `git pull` antes de crear una rama, esta puede partir desde una versión desactualizada de `main`. Luego pueden aparecer conflictos, faltar cambios importantes o ser necesario rebasar la rama antes del Pull Request.
2. Si `.venv/` ya fue subida, primero se agrega `.venv/` al `.gitignore`; después se elimina del índice sin borrar el entorno local con `git rm -r --cached .venv`, se hace commit y se ejecuta `git push`. Si hubo secretos, también deben revocarse y reemplazarse.
3. Varias aplicaciones pequeñas separan responsabilidades, reducen el acoplamiento y facilitan que cada parte sea probada, mantenida y reutilizada. Una aplicación masiva hace más difícil ubicar errores y coordinar cambios.
