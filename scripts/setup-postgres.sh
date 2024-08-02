#!/bin/bash

POSTGRES_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
echo "Creating database ${POSTGRES_DB}..."

psql ${POSTGRES_URL} -f scripts/setup-postgres.sql
psql ${POSTGRES_URL} -c "GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_USER};"
psql ${POSTGRES_URL} -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ${POSTGRES_USER};"
psql ${POSTGRES_URL} -c "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ${POSTGRES_USER};"
psql ${POSTGRES_URL} -f scripts/create_challenge_table.sql
psql ${POSTGRES_URL} -f scripts/create_table.sql
