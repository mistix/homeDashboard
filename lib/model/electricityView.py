# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date
from sqlalchemy import Column
from sqlalchemy.types import Text
from sqlalchemy.sql import func

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
    def get_last_month(session):
        now = date.today()
        firstDayOfPrevMonth = date(now.year, now.month-1, 3)
        lastDayOfPrevMonth = date(now.year, now.month, 3)

        if now.day >= 3:
            firstDayOfPrevMonth = date(now.year, now.month, 3)
            lastDayOfPrevMonth = date(now.year, now.month+1, 3)

        return session.query(ElectricityView).filter(func.julianday(ElectricityView.readingDate) >= func.julianday(firstDayOfPrevMonth)).filter(func.julianday(ElectricityView.readingDate) <= func.julianday(lastDayOfPrevMonth)).order_by(ElectricityView.readingDate)

    @staticmethod
    def get_last_two_months(session):
        now = date.today()
        firstDayOfPrevMonth = date(now.year, now.month-2, 3)

        return session.query(ElectricityView).filter(func.julianday(ElectricityView.readingDate) >= func.julianday(firstDayOfPrevMonth)).order_by(ElectricityView.readingDate)

    @staticmethod
    def get_last_mesurement(session):
        return session.query(ElectricityView).order_by(func.julianday(ElectricityView.readingDate).desc()).first()

    @staticmethod
    def get_payment_values(session):
        return session.query(ElectricityView).filter(func.strftime('%d', ElectricityView.readingDate) == '03').order_by(ElectricityView.readingDate)

    @staticmethod
    def get_month(session, year, month):
        firstDayOfPrevMonth = date(year, month-1, 1)
        lastDayOfPrevMonth = date(year, month, 1) - datetime.timedelta(days = 1)

        return session.query(Electricity).filter(Electricity.readingDate >= firstDayOfPrevMonth).filter(Electricity.readingDate <= lastDayOfPrevMonth).order_by(Electricity.readingDate)
