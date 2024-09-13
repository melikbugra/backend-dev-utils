import pytest
from assertpy import assert_that
from sqlmodel import SQLModel, Field, create_engine, Session, select
from sqlalchemy.engine.base import Engine
from sqlalchemy import inspect

from backend_dev_utils.database_handlers.multiple_database_handler import (
    MultipleDatabaseHandler,
)


class TestModel2(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str


def test_named_singleton_behavior(setup_multiple_db: MultipleDatabaseHandler):
    db_handler1 = MultipleDatabaseHandler(name="db1", database_uri="sqlite:///:memory:")
    db_handler2 = MultipleDatabaseHandler(name="db1", database_uri="sqlite:///:memory:")
    db_handler3 = MultipleDatabaseHandler(name="db2", database_uri="sqlite:///:memory:")

    assert_that(db_handler1).is_equal_to(db_handler2)
    assert_that(db_handler2).is_not_equal_to(db_handler3)
    assert_that(db_handler1.name).is_equal_to("db1")
    assert_that(db_handler2.name).is_equal_to("db1")
    assert_that(db_handler3.name).is_equal_to("db2")


def test_create_tables(setup_multiple_db_with_tables: MultipleDatabaseHandler):
    db_handler = setup_multiple_db_with_tables

    inspector = inspect(db_handler.engine)
    tables = inspector.get_table_names()
    assert_that(tables).contains("testmodel2")


def test_get_session(setup_multiple_db_with_tables: MultipleDatabaseHandler):
    db_handler: MultipleDatabaseHandler = setup_multiple_db_with_tables

    session_generator = db_handler.get_session()
    with next(session_generator) as session:
        assert_that(session).is_instance_of(Session)

        new_instance = TestModel2(name="Test")
        session.add(new_instance)
        session.commit()

        statement = select(TestModel2).where(TestModel2.name == "Test")
        result = session.exec(statement).first()

        assert_that(result).is_not_none()
        assert_that(result.name).is_equal_to("Test")


def test_engine_initialization(setup_multiple_db: MultipleDatabaseHandler):
    db_handler = setup_multiple_db

    assert_that(db_handler.engine).is_instance_of(Engine)
    assert_that(db_handler.database_uri).starts_with("sqlite:///")


def test_reset_instance():
    db_handler1 = MultipleDatabaseHandler(name="db1", database_uri="sqlite:///:memory:")

    MultipleDatabaseHandler.reset_instance(name="db1")

    db_handler2 = MultipleDatabaseHandler(name="db1", database_uri="sqlite:///:memory:")

    assert_that(db_handler1).is_not_equal_to(db_handler2)
