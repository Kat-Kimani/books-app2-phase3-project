from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Create the engine and session
engine = create_engine("sqlite:///db/restaurants.db")
Session = sessionmaker(bind=engine)
session = Session()
