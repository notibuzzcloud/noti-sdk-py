# Guía para Probar el SDK Localmente

Esta guía explica cómo instalar y probar el SDK de Python localmente antes de publicarlo.

## Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Acceso a una instancia de NotiBuzz Bridge con API Key

## Instalación en Modo Desarrollo

### Opción 1: Instalación Editable (Recomendada)

Esta opción instala el SDK en modo "editable", lo que significa que los cambios en el código se reflejan inmediatamente sin necesidad de reinstalar:

```bash
cd noti-sdk-py
pip install -e .
```

O si estás usando Python 3 específicamente:

```bash
pip3 install -e .
```

### Opción 2: Instalación desde el Directorio

```bash
cd noti-sdk-py
pip install .
```

### Opción 3: Usar PYTHONPATH (Sin Instalación)

Si prefieres no instalar el paquete, puedes agregar el directorio al PYTHONPATH:

```bash
export PYTHONPATH="${PYTHONPATH}:/Documents/notibuzz/noti-sdk-py"
```

## Configuración de Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto o exporta las variables en tu terminal:

### Opción 1: Archivo .env (Recomendado)

Crea un archivo `.env` en `noti-sdk-py/`:

```bash
cd noti-sdk-py
cat > .env << EOF
NOTI_URL=https://tu-bridge-url.com
NOTI_KEY=tu_api_key_aqui
NOTI_SESSION_NAME=default
EOF
```

Luego carga las variables:

```bash
export $(cat .env | xargs)
```

### Opción 2: Exportar Directamente

```bash
export NOTI_URL="https://tu-bridge-url.com"
export NOTI_KEY="tu_api_key_aqui"
export NOTI_SESSION_NAME="default"
```

### Opción 3: Modificar los Ejemplos Directamente

Puedes editar los archivos de ejemplo y reemplazar los valores por defecto:

```python
configure_client({
    'noti_url': 'https://tu-bridge-url.com',  # Cambia esto
    'noti_api_key': 'tu_api_key_aqui'  # Cambia esto
})
```

## Ejecutar los Ejemplos

### Ejemplo 1: Listar Sesiones

```bash
cd noti-sdk-py
python examples/list_sessions.py
```

O con Python 3 específicamente:

```bash
python3 examples/list_sessions.py
```

### Ejemplo 2: Enviar Mensaje de Texto

```bash
python examples/send_text.py
```

**Nota**: Asegúrate de cambiar el `chat_id` en `send_text.py` por un ID real antes de ejecutarlo.

## Verificar la Instalación

Puedes verificar que el SDK está instalado correctamente:

```bash
python -c "import noti_sdk_py; print(noti_sdk_py.__version__)"
```

O probar la importación:

```bash
python -c "from noti_sdk_py import configure_client, list_sessions; print('✅ SDK instalado correctamente')"
```

## Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'noti_sdk_py'"

**Solución**: Asegúrate de haber instalado el SDK:

```bash
cd noti-sdk-py
pip install -e .
```

### Error: "API Key is required"

**Solución**: Configura las variables de entorno:

```bash
export NOTI_URL="tu_url"
export NOTI_KEY="tu_key"
```

### Error: "HTTP 401 Unauthorized"

**Solución**: Verifica que tu API Key sea correcta y tenga los permisos necesarios.

### Error: "Connection refused" o "Failed to connect"

**Solución**: Verifica que la URL del Bridge sea correcta y que el servicio esté disponible.

## Desarrollo con Cambios en Tiempo Real

Si instalaste en modo editable (`pip install -e .`), cualquier cambio que hagas en el código se reflejará inmediatamente sin necesidad de reinstalar. Esto es ideal para desarrollo.

## Desinstalar

Si necesitas desinstalar el SDK:

```bash
pip uninstall noti-sdk-py
```

## Próximos Pasos

- Revisa los [ejemplos](../examples/) para más casos de uso
- Consulta el [README](README.md) para documentación completa
- Lee la [documentación de la API](../docs/) si está disponible

