import pytest
from assertpy import assert_that
from sqlmodel import SQLModel, Field, Session, select
from sqlalchemy.engine.base import Engine
from sqlalchemy import inspect

from backend_dev_utils.database_handlers.single_database_handler import (
    SingleDatabaseHandler,
)


class TestModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str


def test_singleton_behavior(setup_single_db: SingleDatabaseHandler):
    db_handler1 = SingleDatabaseHandler(database_uri="sqlite:///:memory:")
    db_handler2 = SingleDatabaseHandler(database_uri="sqlite:///:memory:")

    assert_that(db_handler1).is_equal_to(db_handler2)


def test_engine_initialization(setup_single_db: SingleDatabaseHandler):
    db_handler = setup_single_db

    assert_that(db_handler.engine).is_instance_of(Engine)
    assert_that(db_handler.database_uri).starts_with("sqlite:///")


def test_create_tables(setup_single_db_with_tables: SingleDatabaseHandler):
    db_handler = setup_single_db_with_tables

    inspector = inspect(db_handler.engine)
    tables = inspector.get_table_names()
    assert_that(tables).contains("testmodel")


def test_not_create_tables(setup_single_db: SingleDatabaseHandler):
    db_handler = setup_single_db

    inspector = inspect(db_handler.engine)
    tables = inspector.get_table_names()
    assert_that(tables).does_not_contain("testmodel")


def test_get_session(setup_single_db_with_tables):
    db_handler: SingleDatabaseHandler = setup_single_db_with_tables

    session_generator = db_handler.get_session()
    with next(session_generator) as session:
        assert_that(session).is_instance_of(Session)

        new_instance = TestModel(name="Test")
        session.add(new_instance)
        session.commit()

        statement = select(TestModel).where(TestModel.name == "Test")
        result = session.exec(statement).first()

        assert_that(result).is_not_none()
        assert_that(result.name).is_equal_to("Test")


def test_reset_instance():
    db_handler1 = SingleDatabaseHandler(database_uri="sqlite:///:memory:")

    SingleDatabaseHandler.reset_instance()

    db_handler2 = SingleDatabaseHandler(database_uri="sqlite:///:memory:")

    assert_that(db_handler1).is_not_equal_to(db_handler2)
