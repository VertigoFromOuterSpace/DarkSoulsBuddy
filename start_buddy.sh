#!/bin/bash
# Launcher definitivo para o Dark Souls Buddy (usando a versão Qt)

echo "🏰 Dark Souls Buddy - Launcher"
echo "================================"

# Navega para o diretório onde o script está localizado
cd "$(dirname "$0")"

# Ativa o ambiente virtual (venv) se ele existir
if [ -d ".venv" ]; then
  echo "🐍 Ativando ambiente virtual..."
  source .venv/bin/activate
else
  echo "⚠️ Ambiente virtual .venv não encontrado. Executando com python do sistema."
fi

# Executa a versão PyQt do buddy, que é mais robusta
echo "🚀 Iniciando Dark Souls Buddy (Qt)..."
python3 qt_buddy.py

echo "👋 Buddy encerrado."