# API de Productos con FastAPI

Esta es una API RESTful simple para la gestión de productos, construida con FastAPI y SQLAlchemy, que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

## Requisitos Previos

Asegúrate de tener instalado Python 3.8+ en tu sistema.

## Instalación

1.  **Clona el repositorio (o descomprime el proyecto):**

    Si estás usando git:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd api-productos
    ```

2.  **Crea y activa un entorno virtual:**

    Es una buena práctica trabajar dentro de un entorno virtual para aislar las dependencias del proyecto.

    *   En macOS y Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   En Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Instala las dependencias:**

    Instala todas las librerías necesarias que se encuentran en el archivo `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

## Cómo ejecutar la aplicación

Una vez que hayas instalado las dependencias, puedes iniciar el servidor de desarrollo con Uvicorn desde la raíz del proyecto:

```bash
uvicorn main:app --reload
```

*   `main`: se refiere al archivo `main.py`.
*   `app`: es el objeto `FastAPI` creado dentro de `main.py`.
*   `--reload`: hace que el servidor se reinicie automáticamente cada vez que realices un cambio en el código.

La API estará disponible en `http://127.0.0.1:8000`.

## Documentación Interactiva de la API

FastAPI genera automáticamente una documentación interactiva de la API. Puedes acceder a ella en tu navegador a través de las siguientes URLs una vez que la aplicación esté en ejecución:

*   **Swagger UI:** `http://127.0.0.1:8000/docs`
*   **ReDoc:** `http://127.0.0.1:8000/redoc`

Desde estas interfaces puedes probar cada uno de los endpoints de forma interactiva.

## Endpoints de la API

### Productos

*   **`GET /productos`**
    *   **Descripción:** Obtiene una lista de todos los productos.
    *   **Respuesta exitosa (200):** Un arreglo de objetos de producto.

*   **`GET /productos/{producto_id}`**
    *   **Descripción:** Obtiene un producto específico por su ID.
    *   **Respuesta exitosa (200):** Un objeto de producto.
    *   **Respuesta de error (404):** Si el producto con el `producto_id` especificado no existe.

*   **`POST /productos`**
    *   **Descripción:** Crea un nuevo producto.
    *   **Cuerpo de la solicitud:** Un objeto JSON con `nombre` y `precio`.
        ```json
        {
          "nombre": "Nuevo Producto",
          "precio": 99.99
        }
        ```
    *   **Respuesta exitosa (200):** El objeto del producto recién creado, incluyendo su nuevo `id`.

*   **`PUT /productos/{producto_id}`**
    *   **Descripción:** Actualiza un producto existente por su ID.
    *   **Cuerpo de la solicitud:** Un objeto JSON con los campos `nombre` y `precio` a actualizar.
        ```json
        {
          "nombre": "Producto Actualizado",
          "precio": 129.99
        }
        ```
    *   **Respuesta exitosa (200):** El objeto del producto actualizado.
    *   **Respuesta de error (404):** Si el producto no existe.

*   **`DELETE /productos/{producto_id}`**
    *   **Descripción:** Elimina un producto por su ID.
    *   **Respuesta exitosa (200):** Devuelve el objeto del producto que fue eliminado.
    *   **Respuesta de error (404):** Si el producto no existe.

## Estructura del Proyecto

```
.
├── database.py         # Configuración de la conexión a la base de datos con SQLAlchemy.
├── dtos.py             # Modelos de datos Pydantic (schemas) para validación.
├── main.py             # Archivo principal de FastAPI, define los endpoints.
├── models.py           # Modelos de la base de datos SQLAlchemy (ORM).
├── productos/
│   └── crud.py         # Lógica de negocio (CRUD) para los productos.
├── requirements.txt    # Lista de dependencias de Python.
└── sql_app.db          # Archivo de la base de datos SQLite (se crea al ejecutar).
```