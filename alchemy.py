from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func,or_,not_


Base=declarative_base()

db='mysql+mysqldb://root:767918@localhost/init?charset=utf8'
engine=create_engine(db,echo=True)
Session=sessionmaker(bind=engine)
session=Session()

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(CHAR(30))


#init_db()
def use():
    user=User(name='a')
    session.add(user)

    user=User(name='b')
    session.add(user)

    session.commit()

    query=session.query(User)
    print 'statement: ',query

    for user in query:
        print 'user_name:',user.name


