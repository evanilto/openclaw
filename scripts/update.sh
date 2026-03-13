#!/bin/bash

set -e

echo "Backup do banco..."
docker exec fila-db pg_dump -U hospital hospital > backup_$(date +%F).sql || true

echo "======================================"
echo "Atualizando ambiente OpenClaw"
echo "======================================"

echo ""
echo "1) Parando containers..."
docker compose down

echo ""
echo "2) Baixando novas imagens..."
docker compose pull

echo ""
echo "3) Rebuild da imagem customizada..."
docker compose build --pull

echo ""
echo "4) Subindo containers..."
docker compose up -d

echo ""
echo "5) Limpando imagens antigas..."
docker image prune -f

echo ""
echo "======================================"
echo "Atualização concluída!"
echo "======================================"
