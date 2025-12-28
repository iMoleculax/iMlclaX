#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

# Usa o Python da virtualenv
/_iBlogXW/bin/python manage.py collectstatic --noinput
/_iBlogXW/bin/python manage.py makemigrations --noinput
/_iBlogXW/bin/python manage.py migrate --noinput
#python manage.py runserver 192.168.1.170:8000 - Tentou com esse ip, mas não funcionou
# Sobe o servidor Django
/_iBlogXW/bin/python manage.py runserver 0.0.0.0:8888









