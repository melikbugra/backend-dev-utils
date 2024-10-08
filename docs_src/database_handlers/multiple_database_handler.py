from backend_dev_utils import MultipleDatabaseHandler

first_db = MultipleDatabaseHandler(
    name="first_db", database_uri="sqlite:///:memory:", echo=True, create_tables=True
)

session = first_db.get_session()
