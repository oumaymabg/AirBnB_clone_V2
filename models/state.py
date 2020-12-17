#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ Task 6 """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """ Task 6 """
        ls = []
        for x in models.storage.all(City).values():
            if x.state_id == self.id:
                ls.append(x)
        return ls
