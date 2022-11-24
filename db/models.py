from .database import Base
from sqlalchemy import Column, Integer


class DbEventInfo(Base):
    __tablename__ = 'event_info'
    event_id = Column(Integer, primary_key=True, index=True)
    num_terminals = Column(Integer, nullable=False)