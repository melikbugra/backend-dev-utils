import pytest
from sqlmodel import SQLModel, create_engine
from backend_dev_utils.database_handlers.single_database_handler import (
    SingleDatabaseHandler,
)
from backend_dev_utils.database_handlers.multiple_database_handler import (
    MultipleDatabaseHandler,
)
from tests.unit.database_handlers.test_multiple_database_handler import TestModel2
from tests.unit.database_handlers.test_single_database_handler import TestModel


@pytest.fixture()
def setup_single_db():
    unique_db_name = f"sqlite:///:memory:"
    db_handler = SingleDatabaseHandler(database_uri=unique_db_name, create_tables=False)

    yield db_handler

    SQLModel.metadata.drop_all(db_handler.engine)


@pytest.fixture()
def setup_single_db_with_tables():
    unique_db_name = f"sqlite:///:memory:"
    db_handler = SingleDatabaseHandler(database_uri=unique_db_name, create_tables=True)

    yield db_handler

    SQLModel.metadata.drop_all(db_handler.engine)


@pytest.fixture()
def setup_multiple_db():
    unique_db_name = f"sqlite:///:memory:"
    db_handler = MultipleDatabaseHandler(
        name="db", database_uri=unique_db_name, create_tables=False
    )

    yield db_handler

    SQLModel.metadata.drop_all(db_handler.engine)


@pytest.fixture()
def setup_multiple_db_with_tables():
    unique_db_name = f"sqlite:///:memory:"
    db_handler = MultipleDatabaseHandler(
        name="db", database_uri=unique_db_name, create_tables=True
    )

    yield db_handler

    SQLModel.metadata.drop_all(db_handler.engine)


@pytest.fixture(autouse=True)
def reset_named_singleton():
    yield
    for db_name in ["db", "db1", "db2"]:
        try:
            MultipleDatabaseHandler.reset_instance(name=db_name)
        except Exception:
            pass


@pytest.fixture(autouse=True)
def reset_single_singleton():
    yield
    try:
        SingleDatabaseHandler.reset_instance()
    except Exception:
        pass
