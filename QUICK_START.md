# Quick Start - Probar el SDK Localmente

## Pasos Rápidos

### 1. Instalar el SDK en modo desarrollo

```bash
cd noti-sdk-py
pip install -e .
```

### 2. Configurar variables de entorno

```bash
export NOTI_URL="https://tu-bridge-url.com"
export NOTI_KEY="tu_api_key"
export NOTI_SESSION_NAME="default"
```

O crea un archivo `.env`:

```bash
cat > .env << EOF
NOTI_URL=https://tu-bridge-url.com
NOTI_KEY=tu_api_key
NOTI_SESSION_NAME=default
EOF

# Cargar variables
export $(cat .env | xargs)
```

### 3. Ejecutar un ejemplo

```bash
# Listar sesiones
python examples/list_sessions.py

# Enviar mensaje (cambia el chat_id primero)
python examples/send_text.py
```

### 4. O usar el script helper

```bash
chmod +x run_example.sh
./run_example.sh list_sessions
```

## Verificar Instalación

```bash
python -c "from noti_sdk_py import configure_client; print('✅ OK')"
```

## Solución Rápida de Problemas

| Error | Solución |
|-------|----------|
| `ModuleNotFoundError` | Ejecuta `pip install -e .` |
| `API Key is required` | Configura `NOTI_URL` y `NOTI_KEY` |
| `HTTP 401` | Verifica que tu API Key sea correcta |

Para más detalles, ver [TESTING.md](TESTING.md)

