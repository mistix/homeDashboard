# -*- coding: utf-8 -*-
from datetime import datetime, date
from sqlalchemy import Column, cast, Date, func
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
    def isReadingExistsInCurrentDay(session, meterId):
        now = date.today()
        return session.query(func.count(ElectricityInsert.id)).filter(ElectricityInsert.meterId == meterId).filter(func.date(ElectricityInsert.readingDate) == now).scalar() > 0

    @staticmethod
    def addReadingValue(session, readingValue, meterId):
        now = datetime.now()
        dateAsText = now.strftime('%Y-%m-%d %H:%M:%S')

        isExists = ElectricityInsert.isReadingExistsInCurrentDay(session, meterId)
        if isExists:
            return

        newReading = ElectricityInsert(value=str(readingValue),  readingDate=dateAsText, meterId=str(meterId))
        session.add(newReading)
        session.commit()
