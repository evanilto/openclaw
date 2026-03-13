#!/bin/sh

export PGPASSWORD="hospital123"

QUERY="$1"

# bloqueia comandos perigosos
case "$QUERY" in
  *INSERT*|*UPDATE*|*DELETE*|*DROP*|*ALTER*)
    echo "Only SELECT queries are allowed"
    exit 1
    ;;
esac

psql -h fila-db \
     -U hospital \
     -d hospital \
     -t -A -q \
     -c "$QUERY"
