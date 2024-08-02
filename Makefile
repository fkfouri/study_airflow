help:
	@echo "This"

install:
	sh ./scripts/install_airflow.sh

start:
	sh ./scripts/run_airflow.sh

conn:
	airflow connections add 'study_postgres' \
		--conn-type 'postgres' \
		--conn-host '${POSTGRES_HOST}' \
		--conn-schema '${POSTGRES_DB}' \
		--conn-login '${POSTGRES_USER}' \
		--conn-password '${POSTGRES_PASSWORD}' \
		--conn-port '${POSTGRES_PORT}'

stop:
	sh ./scripts/stop_airflow.sh