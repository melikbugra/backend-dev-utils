from backend_dev_utils.database_handler.single_database_handler import (
    SingleDatabaseHandler,
)

db = SingleDatabaseHandler(
    database_uri="sqlite:///:memory:", echo=True, create_tables=True
)

session = db.get_session()
