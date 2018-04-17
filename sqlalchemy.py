from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext import declarative
from sqlalchemy import func,or_,not_

class UserBase(object):
    
    @declarative.declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()+'s'

    def update(self,kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

Session=None
Base = declarative_base(cls=UserBase)

def main():
    
    #Base is an orm implementor
    db='mysql+mysqldb://root:767918@localhost/init?charset=utf8'
    #engine is a connection managment
    engine=create_engine(db)

    Session=sessionmaker(bind=engine)
    session=Session()
    select_all(session)


def test(session):
    print 'before modifying:'
    objs = _query(session,User).all()

    for obj in objs:
        print 'Id: ',obj.Id,' name: ',obj.name,' age: ',obj.age

    modify_age(session)
    

def init_db(engine):
    
    Base.metadata.create_all(engine)

def select_all(session):
    objs = _query(session,User).all()
    for obj in objs:
        print 'Id: ',obj.Id,' name: ',obj.name,' age: ',obj.age


def  drop_db(engine):

    Base.metadata.drop_all(engine)


class User(Base):

    Id=Column(Integer,primary_key=True)
    name=Column(String(30))
    age = Column(Integer,nullable=True)


def use(session):
    
    session.add(User(Id='1',name='a',age=12))
    session.add(User(Id='2',name='b',age=13))
    session.commit()


def modify_age(session):

    agent= _get_by_name(session)    
    res={'age':22}

    agent.update(res)
    session.commit()

def _query(session,class_,attr=None,condition=None):
            
    query= session.query(class_)
    if attr:
        try:
            if condition:
                query = query.filter(getattr(class_,attr) == condition)
            else:
                raise

        except Exception :
            raise 

    return query


def _get_by_name(session):
    
    try:
        agent_db = _query(session,User,'name','a').one()
        return agent_db
    
    except Exception:
        raise


if __name__ == '__main__':
    main()
