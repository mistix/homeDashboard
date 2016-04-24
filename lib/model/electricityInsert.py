# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date
from sqlalchemy import Column
from sqlalchemy.types import Number, Text

from lib.model import Base

__all__ = ['electricityInsert']

class ElectricityInsert(Base):
    __tablename__ = "powerConsumption"

    id = Column(Text, primary_key=True)
    value = Column(Number),
    readingDate = Column(Text),
    meterId = Column(Number)

    def __init_(self, message):
        Base.__init__(self)
        self.value = message

    @staticmethod
    def get_this_month(session, readingValue, meterId):
        now = date.today()

        newReading = session.query(Electricity).insert(id='NULL', value=readingValue,  readingDate=now, meterId = meterId)
        sessiona.add(newReading)
        session.commit()

