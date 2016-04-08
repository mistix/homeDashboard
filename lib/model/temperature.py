# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from sqlalchemy import Column
from sqlalchemy.types import DateTime, Numeric

from lib.model import Base

__all__ = ['Temperature']

class Temperature(Base):
    __tablename__ = 'sensorsReadingView'

    readingDate = Column(DateTime, primary_key=True)
    airTemperature = Column(Numeric)
    heaterTemperature = Column(Numeric)

    @staticmethod
    def get_last_24_hours(session):
        return session.query(Temperature).filter(Temperature.readingDate >= datetime.now() + timedelta(days=1)).order_by(Temperature.readingDate)

    @staticmethod
    def get_last_48_hours(session):
        return session.query(Temperature).filter(Temperature.readingDate >= datetime.now() + timedelta(days=2)).order_by(Temperature.readingDate)

    @staticmethod
    def get_last_week(session):
        return session.query(Temperature).filter(Temperature.readingDate >= datetime.now() + timedelta(days=7)).order_by(Temperature.readingDate)

    @staticmethod
    def get_reading_inrange(session, fromDateTime, toDateTime):
        return session.query(Temperature).filter(Temperature.readingDate >= fromDateTime and Temperature.readingDate <= toDateTime).order_by(Temperature.readingDate)

    @staticmethod
    def all_(session):
        return session.query(Temperature)
