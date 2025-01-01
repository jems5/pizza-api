from database import db_connection, Base
from model import User, Order

engine = db_connection()

Base.metadata.create_all(bind=engine)
