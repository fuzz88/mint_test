#!/bin/sh

echo "Starting app.py with $(python -V)..."

export DATABASE_FILE=/opt/database/names.db

gunicorn --chdir /opt/app -b 0.0.0.0:8081 -k  uvicorn.workers.UvicornWorker --log-level warning app:app