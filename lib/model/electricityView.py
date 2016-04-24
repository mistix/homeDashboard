# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date
from sqlalchemy import Column
from sqlalchemy.types import Text

from lib.model import Base

__all__ = ['ElectricityView']

class ElectricityView(Base):
    __tablename__ = "powerUsageView"

    readingDate = Column(Text, primary_key=True)
    meterNumber = Column(Text)
    readingValue = Column(Text)
    powerUsage = Column(Text)

    def __init_(self, message):
        Base.__init__(self)
        self.value = message

    @staticmethod
    def get_this_month(session):
        now = date.today()
        firstDayOfMonth = date(now.year, now.month, 1)
        return session.query(ElectricityView).filter(ElectricityView.readingDate >= firstDayOfMonth).order_by(ElectricityView.readingDate)

    @staticmethod
    def get_last_month(session):
        now = date.today()
        firstDayOfPrevMonth = date(now.year, now.month-1, 1)
        lastDayOfPrevMonth = date(now.year, now.month, 1) - datetime.timedelta(days = 1)

        return session.query(ElectricityView).filter(Electricity.readingDate >= firstDayOfPrevMonth).filter(Electricity.readingDate <= lastDayOfPrevMonth).order_by(Electricity.readingDate)

    @staticmethod
    def get_month(session, year, month):
        firstDayOfPrevMonth = date(year, month-1, 1)
        lastDayOfPrevMonth = date(year, month, 1) - datetime.timedelta(days = 1)

        return session.query(Electricity).filter(Electricity.readingDate >= firstDayOfPrevMonth).filter(Electricity.readingDate <= lastDayOfPrevMonth).order_by(Electricity.readingDate)
