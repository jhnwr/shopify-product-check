from sqlmodel import SQLModel, create_engine

# UIsing SQLite here but can easily use PostgreSQL by changing the url
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# The engine is the interface to our database so we can execute SQL commands
engine = create_engine(sqlite_url)


# using the engine we create the tables we need if they aren't already done
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
