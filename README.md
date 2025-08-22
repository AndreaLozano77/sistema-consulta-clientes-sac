# Sistema de Consulta de Clientes - SAC

Sistema web para consultar información de clientes por número de documento, desarrollado para **Rios del desierto SAS**.

## Funcionalidades Implementadas

- Consulta de clientes por número de documento
- Formulario web con tipos de documento (CC, NIT, Pasaporte)
- API REST para búsquedas
- Exportación de datos a CSV
- Base de datos SQLite con modelos Cliente y Compra
- Interfaz web responsive y funcional

## Tecnologías Utilizadas

- **Backend:** Django 5.x (Python)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Base de datos:** SQLite
- **ORM:** Django ORM

## Requisitos del Sistema

- Python 3.8 o superior
- Django 5.x
- Navegador web moderno

## Guía de Instalación

### 1. Clonar el repositorio
```bash
git clone [URL_DEL_REPOSITORIO]
cd proyecto_sac
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install django
```

### 4. Configurar base de datos
```bash
cd cliente_sac
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear datos de prueba (opcional)
```bash
python manage.py shell
```
Ejecutar los comandos de creación de datos del archivo `datos_prueba.py`

### 6. Ejecutar el servidor
```bash
python manage.py runserver
```

### 7. Acceder a la aplicación
Abrir navegador en: `http://127.0.0.1:8000/`

## Datos de Prueba

El sistema incluye los siguientes clientes de prueba:

| Tipo | Documento | Nombre | Total Compras |
|------|-----------|--------|---------------|
| CC | 12345678 | Juan Carlos Pérez González | $700,000 |
| CC | 87654321 | María Fernanda López Rivera | $7,500,000 |
| NIT | 900123456 | Empresa ABC S.A.S. | $50,000 |

## Uso del Sistema

1. **Consultar Cliente:**
   - Seleccionar tipo de documento
   - Ingresar número de documento
   - Hacer clic en "Buscar Cliente"

2. **Exportar Datos:**
   - Realizar una búsqueda exitosa
   - Hacer clic en "Exportar a CSV"
   - El archivo se descargará automáticamente

## API Endpoints

- `GET /` - Página principal con formulario
- `POST /api/buscar-cliente/` - Buscar cliente por documento
- `GET /exportar/<id>/` - Exportar datos del cliente en CSV

## Estructura del Proyecto

```
proyecto_sac/
├── venv/                    # Entorno virtual
├── cliente_sac/            # Proyecto Django
│   ├── manage.py
│   ├── cliente_sac/        # Configuración principal
│   └── consultas/          # Aplicación principal
│       ├── models.py       # Modelos Cliente y Compra
│       ├── views.py        # Lógica de negocio
│       ├── urls.py         # URLs de la app
│       └── templates/      # Templates HTML
├── README.md
└── requirements.txt
```

## Ambiente Productivo

Para desplegar en producción:

1. Configurar `DEBUG = False` en `settings.py`
2. Configurar `ALLOWED_HOSTS` con el dominio
3. Usar servidor web como Nginx + Gunicorn
4. Configurar base de datos PostgreSQL (recomendado)
5. Configurar archivos estáticos con `collectstatic`

## Funcionalidades Pendientes

- Reporte de fidelización de clientes (>$5M último mes)
- Exportación a Excel
- Autenticación de usuarios
- Interfaz de administración avanzada

## Desarrollador

Proyecto desarrollado como parte del ejercicio técnico para **Rios del desierto SAS**.

**Tiempo de desarrollo:** 2 horas (funcionalidad básica)

---

*Sistema funcional entregado - Listo para pruebas y evaluación*