FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y make postgresql postgresql-contrib

# RUN pip install pip --upgrade
# RUN pip install poetry

# ENV POETRY_NO_INTERACTION=1 \
#     POETRY_VIRTUALENVS_IN_PROJECT=true \
#     POETRY_VIRTUALENVS_CREATE=1 \
#     POETRY_CACHE_DIR=/tmp/poetry_cache
    
# RUN echo "Config virtualenvs" && \
#     poetry config virtualenvs.in-project true 


WORKDIR /workspaces/study_airflow

ENV AIRFLOW_VERSION=2.6.3 \
    AIRFLOW_HOME=/workspaces/study_airflow/airflow
    
ENV CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.11.txt"

RUN pip install apache-airflow[virtualenv,postgres]==${AIRFLOW_VERSION} --constraint ${CONSTRAINT_URL}

RUN echo 'alias la="ls -lah"' >> /home/vscode/.bashrc \
    && echo "complete -W \"\`grep -oE '^[a-zA-Z0-9_.-]+:([^=]|$)' ?akefile | sed 's/[^a-zA-Z0-9_.-]*$//'\`\" make" >> /home/vscode/.bashrc

COPY requirements.txt /tmp/pip-tmp/

RUN pip install pip --upgrade && \
    pip --no-cache-dir install -r /tmp/pip-tmp/requirements.txt && \
    rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>



