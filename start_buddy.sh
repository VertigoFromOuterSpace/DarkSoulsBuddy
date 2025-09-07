#!/bin/bash

echo "Dark Souls Buddy - Launcher"
echo "================================"
cd "$(dirname "$0")"

if [ -d ".venv" ]; then
  echo "Ativando ambiente virtual..."
  source .venv/bin/activate
else
  echo "Ambiente virtual .venv não encontrado. Executando com python do sistema."
fi


echo "Iniciando Dark Souls Buddy (Qt)..."
python3 qt_buddy.py

echo "Buddy encerrado."
