from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker

def db_connection():
    user = "admin"
    password = "bigfoot123"
    database = "pizza_api"
    host = "localhost"
    port = "5432"

    database_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"

    try:
        engine = create_engine(database_url)
        with engine.connect() as connection:
            print("connection success") # Log to check for db connection
            print(engine)   # Ensure that the db connection is correct
    except SQLAlchemyError as e:
        print(f"An error occuered: {e}")
    return engine

Base = declarative_base()
Session = sessionmaker()
    