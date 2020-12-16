#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
	cities = relationship("City", backref="state", cascade="all, delete")
    
    @property
    def cities(self):
        """ Task 6 """
        ls = []
        for x in models.storage.all(City).values():
            if x.state_id == self.id:
                ls.append(x)
        return ls