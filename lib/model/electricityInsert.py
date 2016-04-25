# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.types import Text, Integer

from lib.model import Base

__all__ = ['electricityInsert']

class ElectricityInsert(Base):
    __tablename__ = "powerConsumption"

    id = Column(Integer, primary_key=True)
    value = Column(Text)
    readingDate = Column(Text)
    meterId = Column(Text)

    def __init_(self, message):
        Base.__init__(self)
        self.value = message

    @staticmethod
    def addReadingValue(session, readingValue, meterId):
        now = datetime.now()
        dateAsText = now.strftime('%Y-%m-%d %H:%M:%S')

        newReading = ElectricityInsert(value=str(readingValue),  readingDate=dateAsText, meterId=str(meterId))
        session.add(newReading)
        session.commit()

