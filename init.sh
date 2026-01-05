#!/bin/bash
# Script de inicialização do ambiente Docker

# Garante que o próprio script tenha permissão de execução
chmod +x "$0"

echo "🔧 Ajustando permissões do pgAdmin..."
sudo mkdir -p ./data/pgadmin/sessions
sudo chown -R 5050:5050 ./data/pgadmin


echo "✅ Ambiente pronto. Agora rode: docker compose up --build"
