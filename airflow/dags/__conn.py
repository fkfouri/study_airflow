from airflow.models import Connection
from airflow import settings
from os import getenv


def create_postgres_connection():
    conn = Connection(
        conn_id="study_postgres",
        conn_type="postgres",
        host=getenv("POSTGRES_HOST"),
        schema="postgres",
        login=getenv("POSTGRES_USER"),
        password=getenv("POSTGRES_PASSWORD"),
        port=5432,
    )
    session = settings.Session()
    existing_conn = (
        session.query(Connection).filter(Connection.conn_id == conn.conn_id).first()
    )
    if existing_conn:
        session.delete(existing_conn)
    session.add(conn)
    session.commit()
    session.close()


create_postgres_connection()
