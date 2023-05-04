# Copyright (c) 2023 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# example_db_operations.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create an engine to connect to a database
engine = create_engine('sqlite:///example.db')

# create a session factory
Session = sessionmaker(bind=engine)

# create a base class for declarative models
Base = declarative_base()

# define a model class for a table
class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# create the table in the database
Base.metadata.create_all(engine)

# create a session to interact with the database
session = Session()

# add a new person to the table
person = Person(name='Nikhil', age=30)
session.add(person)
session.commit()

# retrieve all people from the table
people = session.query(Person).all()
for person in people:
    print(person.name, person.age)
    
# update a person's age
person = session.query(Person).filter_by(name='Nikhil').first()
person.age = 31
session.commit()

# delete a person from the table
person = session.query(Person).filter_by(name='Nikhil').first()
session.delete(person)
session.commit()

# close the session
session.close()