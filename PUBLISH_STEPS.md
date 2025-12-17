# Pasos para Publicar noti-sdk-py v1.0.1

## ✅ Verificación Pre-Publicación

Todos los archivos han sido actualizados correctamente:

- ✅ `setup.py`: versión `1.0.1`
- ✅ `pyproject.toml`: versión `1.0.1`
- ✅ `noti_sdk_py/__init__.py`: versión `1.0.1`
- ✅ `CHANGELOG.md`: actualizado con todos los cambios de v1.0.1
- ✅ `README.md`: completo con todos los ejemplos
- ✅ Ejemplos: todos creados y en inglés

## Pasos para Publicar

### 1. Instalar herramientas necesarias

```bash
cd /notibuzz/v1/client/noti-sdk-py
pip install --upgrade build twine
```

### 2. Limpiar builds anteriores

```bash
rm -rf build/ dist/ *.egg-info/
```

### 3. Construir los paquetes

```bash
python -m build
```

Esto generará:
- `dist/noti-sdk-py-1.0.1.tar.gz` (source distribution)
- `dist/noti_sdk_py-1.0.1-py3-none-any.whl` (wheel)

### 4. Verificar el paquete

```bash
twine check dist/*
```

Debería mostrar: `Checking dist/noti-sdk-py-1.0.1.tar.gz: PASSED`

### 5. (Opcional) Probar en TestPyPI primero

```bash
# Subir a TestPyPI
twine upload --repository testpypi dist/*

# Probar instalación desde TestPyPI
pip install --index-url https://test.pypi.org/simple/ noti-sdk-py==1.0.1
```

### 6. Publicar en PyPI

**Opción A: Con API Token (Recomendado)**

1. Obtén tu API token de PyPI:
   - Ve a https://pypi.org/manage/account/
   - Crea un nuevo API token con scope "Entire account" o solo para el proyecto `noti-sdk-py`

2. Publica usando el token:

```bash
twine upload dist/*
```

Cuando se solicite:
- Username: `__token__`
- Password: `pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (tu token)

**Opción B: Con archivo de configuración**

Crea `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Luego ejecuta:

```bash
twine upload dist/*
```

### 7. Verificar publicación

1. Visita: https://pypi.org/project/noti-sdk-py/
2. Verifica que la versión 1.0.1 esté disponible
3. Prueba la instalación:

```bash
pip install --upgrade noti-sdk-py
python -c "import noti_sdk_py; print(f'Version: {noti_sdk_py.__version__}')"
```

Debería mostrar: `Version: 1.0.1`

## Cambios en v1.0.1

### Changed
- Synchronized SDK with latest Bridge API changes
- Removed deprecated endpoints: `chats_archive`, `chats_unarchive`, `chats_unread`
- Removed standalone `send_list` endpoint (now handled via `send_message` with type 'list')
- Updated documentation: translated `README.md` and `QUICK_START.md` to English
- Enhanced `README.md` with comprehensive examples covering all endpoints
- Added complete example suite mirroring `noti-sdk-js` structure

### Added
- Complete example files organized by category (sessions, profile, chatting, status, chats, contacts)
- Examples for all message types: file, voice, video, poll, location, contact-vcard, list, link-preview, forward
- Examples for all status types: text, image, voice, video, delete
- Examples for all chat operations: get message, delete message, unpin message, overview POST
- Examples for contact operations: get about, block, unblock
- Section in README linking to examples directory

### Fixed
- SDK now matches Bridge API implementation exactly
- `send_list` functionality properly integrated into `send_message` endpoint
- All examples are now in English and reflect the latest API changes

## Comandos Rápidos (Todo en uno)

```bash
cd /notibuzz/v1/client/noti-sdk-py

# Limpiar
rm -rf build/ dist/ *.egg-info/

# Construir
python -m build

# Verificar
twine check dist/*

# Publicar (reemplaza con tu token)
twine upload dist/*
# Username: __token__
# Password: pypi-tu-token-aqui
```

## Notas Importantes

- ⚠️ Una vez publicada, la versión no se puede eliminar fácilmente
- ⚠️ Asegúrate de probar localmente antes de publicar: `pip install -e .`
- ⚠️ Verifica que `twine check dist/*` pase sin errores
- ⚠️ Considera probar primero en TestPyPI si es tu primera publicación

## Troubleshooting

### Error: "HTTP 403 Forbidden"
- Verifica que tu API token tenga los permisos correctos
- Asegúrate de usar `__token__` como username

### Error: "Package already exists"
- Verifica que la versión sea diferente a la anterior
- Si necesitas actualizar, usa una nueva versión (ej: 1.0.2)

### Error: "Invalid distribution"
- Ejecuta `twine check dist/*` para ver detalles
- Verifica que `MANIFEST.in` incluya todos los archivos necesarios

