#import os,sys,inspect
#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parentdir = os.path.dirname(currentdir)
#sys.path.append(parentdir)

from api import app
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Declare mapping here

class User(Base):
    __tablename__ = 'users'

    name = Column(String(50), primary_key=True, index=True, unique=True)
    nickname = Column(String(50))
    uid = Column(Integer, nullable=False)
    joindate = Column(Date, nullable=False)
    activedate = Column(Date, nullable=False)

    def __repr__(self):
        return "<Users(uid='%s', name='%s', joindate='%s')>" % (
            self.uid, self.name, self.joindate)

engine = create_engine("mysql+mysqldb://" + app.config['MYSQL_USER'] + ":" + app.config['MYSQL_PASSWD'] + "@" +
                       app.config['MYSQL_HOST'] + "/" + app.config['MYSQL_DBNAME'] +
                       "?charset=utf8&use_unicode=0&unix_socket="+app.config['MYSQL_SOCKET'])
Base.metadata.create_all(engine)

# Session is a custom class
Session = sessionmaker(bind=engine)
session = Session()
