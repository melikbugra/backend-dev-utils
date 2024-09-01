from backend_dev_utils import SingleDatabaseHandler

db = SingleDatabaseHandler(
    database_uri="sqlite:///:memory:", echo=True, create_tables=True
)

session = db.get_session()


db2 = SingleDatabaseHandler()
