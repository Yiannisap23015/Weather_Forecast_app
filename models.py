import datetime
from sqlalchemy import String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    city: Mapped[str] = mapped_column(String(30), nullable = True)
    weather: Mapped[float] = mapped_column(Float)
    date_created: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now)

    def __init__(self, city, weather):
        self.city = city
        self.weather = weather

    


