#!/usr/bin/python3
""" Storage sqlalchemy model Task 6 """
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
password = getenv("HBNB_MYSQL_PWD")
hbnb_env = getenv("HBNB_ENV")


class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize instances"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, password, host, database), pool_pre_ping=True)
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all function Task 6 """
        ls = []
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            ls = self.__session.query(cls).all()
        else:
            ls += self.__session.query(User).all()
            ls += self.__session.query(State).all()
            ls += self.__session.query(City).all()
            ls += self.__session.query(Amenity).all()
            ls += self.__session.query(Place).all()
            ls += self.__session.query(Review).all()

        new = {}
        for x in ls:
            tag = x.__class__.__name__ + "." + x.id
            new[tag] = x
        return new

    def new(self, obj):
        """ new funtion Task 6 """
        self.__session.add(obj)

    def save(self):
        """ save funtion Task 6 """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete funtion Task 6 """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload funtion Task 6 """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
