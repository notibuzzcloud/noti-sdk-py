#!/bin/bash

# Script para ejecutar ejemplos del SDK de NotiBuzz
# Uso: ./run_example.sh <nombre_del_ejemplo>
# Ejemplo: ./run_example.sh list_sessions

set -e

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Verificar que se proporcionó un argumento
if [ -z "$1" ]; then
    echo -e "${RED}❌ Error: Debes proporcionar el nombre del ejemplo${NC}"
    echo "Uso: ./run_example.sh <nombre_del_ejemplo>"
    echo "Ejemplos disponibles:"
    echo "  - list_sessions"
    echo "  - send_text"
    exit 1
fi

EXAMPLE_NAME=$1
EXAMPLE_FILE="examples/${EXAMPLE_NAME}.py"

# Verificar que el archivo existe
if [ ! -f "$EXAMPLE_FILE" ]; then
    echo -e "${RED}❌ Error: El archivo ${EXAMPLE_FILE} no existe${NC}"
    exit 1
fi

# Verificar que las variables de entorno están configuradas
if [ -z "$NOTI_URL" ] || [ -z "$NOTI_KEY" ]; then
    echo -e "${YELLOW}⚠️  Advertencia: NOTI_URL o NOTI_KEY no están configuradas${NC}"
    echo "Puedes configurarlas con:"
    echo "  export NOTI_URL='tu_url'"
    echo "  export NOTI_KEY='tu_key'"
    echo ""
    echo "O crear un archivo .env con:"
    echo "  NOTI_URL=tu_url"
    echo "  NOTI_KEY=tu_key"
    echo ""
    read -p "¿Deseas continuar de todos modos? (s/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        exit 1
    fi
fi

# Cargar variables de .env si existe
if [ -f .env ]; then
    echo -e "${GREEN}📝 Cargando variables de .env...${NC}"
    export $(cat .env | grep -v '^#' | xargs)
fi

# Verificar que Python está instalado
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo -e "${RED}❌ Error: Python no está instalado${NC}"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

# Verificar que el SDK está instalado
echo -e "${GREEN}🔍 Verificando instalación del SDK...${NC}"
if ! $PYTHON_CMD -c "import noti_sdk_py" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  El SDK no está instalado. Instalando en modo desarrollo...${NC}"
    pip install -e . > /dev/null 2>&1
    echo -e "${GREEN}✅ SDK instalado${NC}"
fi

# Ejecutar el ejemplo
echo -e "${GREEN}🚀 Ejecutando ejemplo: ${EXAMPLE_NAME}${NC}"
echo ""
$PYTHON_CMD "$EXAMPLE_FILE"

