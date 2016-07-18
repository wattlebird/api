from sqlalchemy import Column, Integer, String, Float
from db import Base


# Declare mapping here

class User(Base):
    __tablename__ = 'user'

    index = Column(Integer, primary_key=True)
    id = Column(String, unique=True)
    nickname = Column(String)
    active = Column(Integer)
    score = Column(Float)

    def __repr__(self):
        return '<User id={0}, nickname={1}, index={2}'.format(self.id, self.nickname, self.index)


class Rank(Base):
    __tablename__ = 'rank'

    index = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    rate = Column(Float)
    rank = Column(Integer)
    title = Column(String)
    bangumi_rank = Column(Integer)

    def __repr__(self):
        return '<Rank id={0}, title={1}, rank={2}'.format(self.id, self.title, self.rank)

