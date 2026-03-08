# Publicar noti-sdk-py en PyPI

## Requisitos

- Cuenta en [PyPI](https://pypi.org/account/register/)
- API token en [pypi.org/manage/account/](https://pypi.org/manage/account/) → API tokens (recomendado; ya no se usa contraseña)

## Instalar herramientas

```bash
pip install --upgrade build twine
```

Si después de instalar `twine` no se reconoce el comando, usa `python -m twine` en lugar de `twine`.

## Publicar (flujo mínimo)

### 1. Subir versión

Editar a mano la misma versión en:

- `pyproject.toml` → `version = "1.0.2"`
- `setup.py` → `version="1.0.2"`

Opcional: actualizar `CHANGELOG.md`.

### 2. Limpiar, construir y comprobar

```bash
cd noti-sdk-py   # o la ruta del repo

rm -rf build/ dist/ *.egg-info/
python -m build
python -m twine check dist/*
```

### 3. Subir a PyPI

```bash
python -m twine upload dist/*
```

Te pedirá usuario y contraseña. Usa:

- **Username:** `__token__`
- **Password:** tu API token de PyPI (p. ej. `pypi-AgEI...`)

### 4. Probar instalación

```bash
pip install noti-sdk-py
python -c "from noti_sdk_py import configure_client; print('OK')"
```

## Opcional: credenciales en `~/.pypirc`

Para no escribir el token en cada publicación:

```ini
[pypi]
username = __token__
password = pypi-TU_TOKEN_AQUI
```

Luego basta con: `python -m twine upload dist/*`

## Opcional: probar antes en TestPyPI

```bash
python -m twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ noti-sdk-py
```

## Checklist rápido

- [ ] Versión igual en `pyproject.toml` y `setup.py`
- [ ] `CHANGELOG.md` actualizado
- [ ] `python -m build` y `python -m twine check dist/*` sin errores
- [ ] Token PyPI con permiso de publicación
