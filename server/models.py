from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData,Integer,Float,String,Column
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model,SerializerMixin):
    __tablename__="earthquakes"
    id=Column(Integer,primary_key=True)
    magnitude=Column(Float)
    location=Column(String)
    year=Column(Integer)
# Add models here
    def __repr__(self):
        return f'{self.id},{self.magnitude},{self.location},{self.year}' 