help:
	@echo "This"

install:
	sh ./scripts/install_airflow.sh

start:
	sh ./scripts/run_airflow.sh

stop:
	sh ./scripts/stop_airflow.sh