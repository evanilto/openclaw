#!/bin/bash
set -e

echo "Reiniciando containers..."

docker compose restart

echo "Containers reiniciados."
