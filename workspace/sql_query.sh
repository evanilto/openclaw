#!/bin/sh

export PGPASSWORD="hospital123"

QUERY="$1"

echo "$QUERY" | grep -iq "^select" || {
  echo "Only SELECT queries are allowed"
  exit 1
}

psql -h fila-db -U hospital -d hospital -t -c "$QUERY"