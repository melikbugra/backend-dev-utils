from sqlmodel import Field, SQLModel, create_engine, Session
from sqlalchemy.engine.base import Engine

from backend_dev_utils.design_patterns.singletons.named_singleton.named_singleton_base import (
    NamedSingletonBase,
)


class MultipleDatabaseHandler(NamedSingletonBase):
    def __init__(
        self,
        name: str,
        database_uri: str,
        echo: bool = False,
        create_tables: bool = False,
    ) -> None:
        self.name = name
        self.engine: Engine = create_engine(database_uri, echo=echo)
        self.database_uri = database_uri

        if create_tables:
            SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        with Session(self.engine) as session:
            yield session
