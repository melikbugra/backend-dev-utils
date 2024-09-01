# conftest.py

import pytest
from sqlmodel import SQLModel, create_engine
from backend_dev_utils.database_handlers.single_database_handler import (
    SingleDatabaseHandler,
)
from backend_dev_utils.database_handlers.multiple_database_handler import (
    MultipleDatabaseHandler,
)


@pytest.fixture()
def setup_single_db():
    db_handler = SingleDatabaseHandler(
        database_uri="sqlite:///:memory:", create_tables=False
    )

    yield db_handler

    SQLModel.metadata.drop_all(db_handler.engine)


@pytest.fixture()
def setup_single_db_with_tables():
    db_handler = SingleDatabaseHandler(
        database_uri="sqlite:///:memory:", create_tables=True
    )

    SQLModel.metadata.create_all(db_handler.engine)

    yield db_handler

    SQLModel.metadata.drop_all(db_handler.engine)


@pytest.fixture()
def setup_multiple_db():
    db_handler = MultipleDatabaseHandler(
        name="db", database_uri="sqlite:///:memory:", create_tables=False
    )

    yield db_handler

    SQLModel.metadata.drop_all(db_handler.engine)


@pytest.fixture()
def setup_multiple_db_with_tables():
    db_handler = MultipleDatabaseHandler(
        name="db", database_uri="sqlite:///:memory:", create_tables=True
    )

    SQLModel.metadata.create_all(db_handler.engine)

    yield db_handler

    SQLModel.metadata.drop_all(db_handler.engine)
