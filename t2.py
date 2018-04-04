from eventlet import pools
from eventlet import semaphore

class Connection(object):
    pool=None
    def __init__(self,name,server_params=None):
        self.name=name
        self.server_params=None

class MyPool(pools.Pool):
    def __init__(self,connection,name)
        self.connection=connection
        self.name=name
    def create(self):
        return self.connection(self.name)


_pool_create_sem=semaphore.Semaphore()
def get_connection_pool(name,connection_cls):
    if not connection_cls.pool:
        connection_cls.pool=Pool(connection_cls,name)
        return connection_cls.pool

class ConnectionContext():
    def __init__(self,name,connection_pool,pooled=True,server_params=None):
        self.connection=None
        self.name=name
        self.connection_pool=connecion_pool
        if pooled:
            self.connection=connection_pool.get()
        else:
            self.connecion=connection_pool.connecion_cls(name,server_params)
        self.pooled=pooled


def create_connection(name,new,connection_pool):
    return ConnectionContext(name,connection,pooled=not new)

def entry(name,new=True):
    return create_connection(name,new,get_connection_pool(name,Connection))
