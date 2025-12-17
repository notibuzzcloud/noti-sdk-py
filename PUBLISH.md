# Guía de Publicación

Esta guía explica cómo publicar `noti-sdk-py` en PyPI y GitHub.

## Prerrequisitos

1. Tener una cuenta en [PyPI](https://pypi.org/) (Python Package Index)
2. Tener una cuenta en [TestPyPI](https://test.pypi.org/) (opcional, para pruebas)
3. Tener una cuenta en [GitHub](https://github.com/)
4. Tener acceso al repositorio `notibuzzcloud/noti-sdk-py`
5. Instalar herramientas de publicación:
   ```bash
   pip install --upgrade build twine
   ```

## Preparación

### 1. Verificar pyproject.toml y setup.py

Asegúrate de que los archivos de configuración tengan:
- ✅ Nombre único en PyPI (`noti-sdk-py`)
- ✅ Versión correcta (`1.0.1`)
- ✅ Descripción clara
- ✅ Keywords relevantes
- ✅ Repository URL correcta
- ✅ License especificada (MIT)
- ✅ Dependencias correctas (`requests>=2.28.0`)

### 2. Verificar archivos incluidos

El archivo `MANIFEST.in` controla qué archivos se incluyen en el paquete. Por defecto, se incluyen:
- `README.md`
- `LICENSE`
- Archivos Python en `noti_sdk_py/`

### 3. Limpiar builds anteriores

```bash
cd noti-sdk-py
rm -rf build/ dist/ *.egg-info/
```

### 4. Verificar que el código funciona

```bash
# Instalar en modo desarrollo
pip install -e .

# Probar los ejemplos
python examples/list_sessions.py
```

## Publicar en PyPI

### Primera publicación

#### Paso 1: Crear cuenta en PyPI

1. Ve a [pypi.org/account/register](https://pypi.org/account/register/)
2. Crea una cuenta
3. Verifica tu email

#### Paso 2: Configurar credenciales (Opcional pero recomendado)

Crea un archivo `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> **Nota**: PyPI ahora usa API tokens en lugar de contraseñas. Ve a [pypi.org/manage/account/](https://pypi.org/manage/account/) → "API tokens" para crear uno.

#### Paso 3: Construir los paquetes

```bash
cd noti-sdk-py

# Limpiar builds anteriores
rm -rf build/ dist/ *.egg-info/

# Construir source distribution (sdist) y wheel
python -m build
```

Esto generará:
- `dist/noti-sdk-py-1.0.1.tar.gz` (source distribution)
- `dist/noti_sdk_py-1.0.1-py3-none-any.whl` (wheel)

#### Paso 4: Verificar el paquete (Recomendado)

```bash
# Verificar que el paquete esté bien formado
twine check dist/*
```

#### Paso 5: Probar en TestPyPI (Opcional pero recomendado)

```bash
# Subir a TestPyPI primero para probar
twine upload --repository testpypi dist/*

# Probar instalación desde TestPyPI
pip install --index-url https://test.pypi.org/simple/ noti-sdk-py
```

#### Paso 6: Publicar en PyPI

```bash
# Publicar en PyPI oficial
twine upload dist/*
```

O si configuraste `~/.pypirc`:

```bash
twine upload dist/*
```

Ingresa tu username (o `__token__`) y password (o API token) cuando se solicite.

### Actualizaciones futuras

1. **Actualizar versión en pyproject.toml y setup.py:**

   Edita manualmente:
   - `pyproject.toml`: `version = "1.0.1"`
   - `setup.py`: `version="1.0.1"`

   O usa bump2version (instalar: `pip install bump2version`):
   ```bash
   # Versión patch (1.0.1 -> 1.0.2)
   bump2version patch
   
   # Versión minor (1.0.1 -> 1.1.0)
   bump2version minor
   
   # Versión major (1.0.1 -> 2.0.0)
   bump2version major
   ```

2. **Actualizar CHANGELOG.md** con los cambios

3. **Construir y publicar:**
   ```bash
   # Limpiar
   rm -rf build/ dist/ *.egg-info/
   
   # Construir
   python -m build
   
   # Verificar
   twine check dist/*
   
   # Publicar
   twine upload dist/*
   ```

## Publicar en GitHub

### Crear repositorio

1. Ve a [GitHub](https://github.com/new)
2. Crea un nuevo repositorio llamado `noti-sdk-py`
3. No inicialices con README, .gitignore o LICENSE (ya los tenemos)

### Configurar Git

```bash
cd noti-sdk-py

# Si aún no tienes el repositorio inicializado
git init

# Agregar remoto
git remote add origin https://github.com/notibuzzcloud/noti-sdk-py.git

# Agregar archivos
git add .

# Commit inicial
git commit -m "Initial commit: noti-sdk-py v1.0.1"

# Push a GitHub
git branch -M main
git push -u origin main
```

### Crear release en GitHub

1. Ve a tu repositorio en GitHub
2. Click en "Releases" → "Create a new release"
3. Tag: `v1.0.1`
4. Title: `v1.0.1 - SDK Synchronization and Documentation Updates`
5. Description: Copia el contenido de CHANGELOG.md para v1.0.1
6. Publicar release

## Verificación

### Verificar en PyPI

```bash
pip search noti-sdk-py  # Nota: pip search está deshabilitado
```

O visita: https://pypi.org/project/noti-sdk-py/

### Verificar instalación

```bash
# Instalar desde PyPI
pip install noti-sdk-py

# O con pip3
pip3 install noti-sdk-py
```

Luego en un proyecto de prueba:

```python
from noti_sdk_py import configure_client, list_sessions
# Debería funcionar sin errores
```

## Checklist antes de publicar

- [ ] `pyproject.toml` tiene información correcta
- [ ] `setup.py` tiene información correcta
- [ ] Versión actualizada en ambos archivos
- [ ] `README.md` está completo y actualizado
- [ ] `LICENSE` está presente
- [ ] `MANIFEST.in` está configurado correctamente
- [ ] `CHANGELOG.md` está actualizado (si existe)
- [ ] Código funciona correctamente (`pip install -e .` y probar ejemplos)
- [ ] Ejemplos funcionan correctamente
- [ ] Documentación está completa
- [ ] No hay archivos innecesarios en el paquete
- [ ] `twine check dist/*` pasa sin errores

## Comandos útiles

```bash
# Ver qué archivos se incluirán en el paquete
python -m build --sdist
tar -tzf dist/noti-sdk-py-*.tar.gz | head -20

# Construir solo source distribution
python -m build --sdist

# Construir solo wheel
python -m build --wheel

# Verificar el paquete antes de publicar
twine check dist/*

# Probar el paquete localmente antes de publicar
pip install dist/noti_sdk_py-*.whl

# O instalar desde el source distribution
pip install dist/noti-sdk-py-*.tar.gz

# Ver información del paquete construido
python -m build --sdist
python -m build --wheel
pip show -f noti-sdk-py  # Después de instalar
```

## Despublicar (Solo en emergencias)

⚠️ **IMPORTANTE**: Solo puedes eliminar un paquete si:
- No tiene descargas
- O fue publicado hace menos de 72 horas

```bash
# Eliminar una versión específica (solo si cumple condiciones)
# Debes hacerlo desde la interfaz web de PyPI:
# https://pypi.org/manage/project/noti-sdk-py/releases/
```

## Notas importantes

- ⚠️ **No publiques versiones con errores**: Una vez publicada, es muy difícil eliminar una versión
- ⚠️ **Usa versiones semánticas**: Sigue [Semantic Versioning](https://semver.org/)
- ⚠️ **Actualiza CHANGELOG**: Mantén un registro de cambios
- ⚠️ **Prueba antes de publicar**: Siempre prueba el paquete localmente y en TestPyPI
- ⚠️ **Verifica con twine check**: Siempre ejecuta `twine check dist/*` antes de publicar
- ⚠️ **Nombres de paquete**: Los nombres en PyPI son únicos globalmente. Si `noti-sdk-py` está ocupado, necesitarás otro nombre.

## Solución de problemas

### Error: "Package already exists"

El nombre del paquete ya está en uso. Necesitas cambiar el nombre en `pyproject.toml` y `setup.py`.

### Error: "Invalid distribution"

Ejecuta `twine check dist/*` para ver los errores específicos.

### Error: "HTTP 403 Forbidden"

Verifica que tu API token tenga los permisos correctos o que tu username/password sean correctos.

### Error: "Failed to upload"

Verifica tu conexión a internet y que PyPI esté disponible.

## Flujo completo de publicación

```bash
# 1. Actualizar versión (manual o con bump2version)
# Editar pyproject.toml y setup.py

# 2. Limpiar
rm -rf build/ dist/ *.egg-info/

# 3. Construir
python -m build

# 4. Verificar
twine check dist/*

# 5. Probar localmente (opcional)
pip install dist/noti_sdk_py-*.whl

# 6. Probar en TestPyPI (opcional pero recomendado)
twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ noti-sdk-py

# 7. Publicar en PyPI
twine upload dist/*

# 8. Verificar instalación
pip install noti-sdk-py
python -c "from noti_sdk_py import configure_client; print('✅ OK')"
```

