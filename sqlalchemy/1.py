import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm  import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext import declarative
from sqlalchemy import func,or_,not_
from sqlalchemy import orm
import sqlalchemy.exc
import sys

SQL_CONNECTION = 'mysql+mysqldb://root:767918@localhost/init?charset=utf8'
class MetaBase(object):
    
    @declarative.declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()+'s'

    def update(self,kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

Session=None
BASE = declarative_base(cls=MetaBase)


class Class(BASE):
    class_id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    teacher = Column(String(10))


class User(BASE):
    Id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer, nullable=True)
    class_id = Column(Integer, ForeignKey('classs.class_id', ondelete='CASCADE'))
    class_ = orm.relationship(Class, backref=orm.backref('users'))


def main():
    test = Test()
    resp = test.create('Class', class_id=2, name='class2')
    if resp:
        print resp

class Test(object):

    def __init__(self):
        self._db_connection = SQL_CONNECTION
        self.session = self._get_session()
        # self._unregister_models()
        self._register_models()

    def _get_session(self, autocommit=True, expire_on_commit=False):
        self._engine = sqlalchemy.create_engine(self._db_connection)
        self._maker = sqlalchemy.orm.sessionmaker(bind=self._engine,
                                            autocommit=autocommit,
                                            expire_on_commit=expire_on_commit)
        return self._maker()


    def _register_models(self, base=BASE):

        try:
            base.metadata.create_all(self._engine)
        except sqlalchemy.exc.OperationalError as e:
            return False
        return True


    def _unregister_models(self, base=BASE):

        try:
            base.metadata.drop_all(self._engine)
        except sqlalchemy.exc.OperationalError as e:
            return False
        return True


    def fields(self, data, fields=None):

        if fields:
            return dict((key, item) for key, item in data.items() if key in fields)
        return data


    def create(self, model, **params):

        session = self.session
        if isinstance(model, basestring):
            model = getattr(sys.modules['__main__'], model)

        with session.begin(subtransactions=True):
            for key, value in params.items():
                try:
                    getattr(model, key)
                except AttributeError as e:
                    raise e

            model_orm = model(**params)
            try:
                session.add(model_orm)
            except sqlalchemy.exc.OperationalError as e:
                raise e
        return { model_orm.__tablename__: params}


    def delete(self):
        pass


    def update(self):
        pass


    def show(self, model, id, fields=None):
        session = self.session
        with session.begin(subtransactions=True):
            query = self.session.query(model)
            result = query.filter(model.id == id).one()
        return result


    def list(self, model, filters=None, fields=None):
        pass


if __name__ == '__main__':
    main()