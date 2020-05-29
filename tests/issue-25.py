from os import getenv

import alembic.config
import psycopg2
import pytest
from sqlalchemy.engine.url import make_url

def db_name(uri):
    u = make_url(uri)
    return u.database


def uri_without_db(pg_uri):
    u = make_url(pg_uri)
    u.database = ""
    uri = f"{u}"
    return uri


def do_up(revision):
    alembic_args = ["upgrade", revision]
    alembic.config.main(argv=alembic_args)


def do_down(revision):
    alembic_args = ["downgrade", revision]
    alembic.config.main(argv=alembic_args)


@pytest.fixture(scope="function", autouse=True)
def manage_test_db():
    uri = getenv("PGURI")
    conn = psycopg2.connect(uri_without_db(uri))
    conn.autocommit = True  # run ddl stmt w/out xact
    cur = conn.cursor()
    db = db_name(uri)

    cur.execute(f"create database {db}")
    do_up("head")
    yield
    do_down("base")
    cur.execute(f"drop database {db}")

    conn.close()


@pytest.fixture
def conn():
    uri = getenv("PGURI")
    conn = psycopg2.connect(uri)
    yield conn
    conn.close()


def test_success(conn):
    pass
