import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from setting import *
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Declare mapping here

class User(Base):
    __tablename__ = 'users'

    uid = Column(Integer, nullable=False)
    name = Column(String(30), primary_key=True, index=True, unique=True)
    joindate = Column(Date, nullable=False)
    last_activate = Column(Date, nullable=False)

    def __repr__(self):
        return "<Users(uid='%s', name='%s', joindate='%s')>" % (
            self.uid, self.name, self.joindate)

engine = create_engine("mysql+mysqldb://" + MYSQL_USER + ":" + MYSQL_PASSWD + "@" +
                       MYSQL_HOST + "/" + MYSQL_DBNAME +
                       "?charset=utf8&use_unicode=0&unix_socket=/var/run/mysqld/mysqld.sock")
Base.metadata.create_all(engine)

# Session is a custom class
Session = sessionmaker(bind=engine)
session = Session()
