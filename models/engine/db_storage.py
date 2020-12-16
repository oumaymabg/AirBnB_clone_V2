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


class DBStorage:
    """ Storage class Task 6 """
    __engine = None
    __session = None

    def __init__(self):
        """ init Task 6 """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
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
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
