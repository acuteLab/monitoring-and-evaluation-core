from __future__ import with_statement
import os
import urllib
import sqlalchemy
from sqlalchemy import create_engine, engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from alembic import context
from alembic.config import Config
from alembic.script import ScriptDirectory
from logging.config import fileConfig
from tld import get_tld
from fastapi import HTTPException, Request
from starlette.config import Config


def get_tenant():

    # print(request.scope.url)
    try:
        full_path = get_tld("http://127.0.0.1/", as_object=True)
        schema_data = full_path.subdomain
        if schema_data == "http://127.0.0.1/" or schema_data == "localhost":
            schema_data = "public"
        # 'some.subdomain'
        full_path.domain
        # 'google'
        full_path.tld
        # 'co.uk'
        full_path.fld
        # 'google.co.uk'

        return schema_data
    except:
        raise HTTPException(status_code=400, detail="Failed to get schema name")


def active_schema(schema_name):
    return declarative_base(metadata=sqlalchemy.MetaData(schema=schema_name))

env = Config(".env")
host_server = env("HOST_SERVER",)
db_server_port = urllib.parse.quote_plus(env("DB_SERVER_PORT"))
database_name = env("DB_NAME",)
db_username = urllib.parse.quote_plus(str(env("DB_USERNAME")))
db_password = urllib.parse.quote_plus(str(env("DB_PASSWORD")))
ssl_mode = urllib.parse.quote_plus(str("prefer"))

# DATABASE_URL = "postgres://zkteplgdncoixb:b4a322577402b490544372faaed79bef705600cee792cddc84fb4c4dade170a1@ec2-52-71-153-228.compute-1.amazonaws.com:5432/de58k6g9i6etkq"

DATABASE_URL = "postgresql://{}:{}@{}:{}/{}?sslmode={}".format(
    db_username, db_password, host_server, db_server_port, database_name, ssl_mode
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
schema_name = "public"
Base = active_schema(schema_name)
# metadata=sqlalchemy.MetaData(schema="coding")

def create_tables():
    return Base.metadata.create_all(engine)