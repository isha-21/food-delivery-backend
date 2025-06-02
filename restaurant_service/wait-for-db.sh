#!/bin/sh
# wait-for-db.sh

set -e

host="$1"
user="$2"
password="$3"
database="$4"
shift 4
cmd="$@"

export PGPASSWORD="$password"

until psql -h "$host" -U "$user" -d "$database" -c '\q' 2>/dev/null; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

>&2 echo "Postgres is up - executing command"
exec "$@"
