Database Handlers are Singleton or NamedSingleton classes to handle database connections, engines and sessions using [SQLModel](https://sqlmodel.tiangolo.com/).


### SingleDatabaseHandler

SingleDatabaseHandler is a singleton to create a db instance. Once you create an instance of the db, it will be the only db that you can create. Even if you call the class again with different arguments - or no arguments, it will return you the first db instance. The parameter *echo* is the one from SQLModel, and if *create_tables* is True, all the tables will be created by SQLModel automatically during the initialization of the db instance. 

```python

{!./docs_src/database_handlers/single_database_handler.py!}

```


### MultipleDatabaseHandler

MultipleDatabaseHandler is almost the same with SingleDatabaseHandler, but it can handle multiple db instance with different names. It is a NamedSingleton (please see the NamedSingleton in DesignPatterns module).

```python

{!./docs_src/database_handlers/multiple_database_handler.py!}

```