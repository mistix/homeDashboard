# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy.types import Text

from lib.model import Base

__all__ = ['meter']

class Meter(Base):
    __tablename__ = "electricityMeter"

    id = Column(Text, primary_key=True)
    number = Column(Text)

    def __init_(self, message):
        Base.__init__(self)
        self.value = message

    @staticmethod
    def getAllMeters(session):
        return session.query(Meter);

