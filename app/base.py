from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/demo', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
Base.metadata.create_all(bind=engine, checkfirst=True)



