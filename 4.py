class Connection(object):
    pool= None
    def __init__(self):
        pass


class Pool(object):
    def __init__(self):
        pass

def get_connection_pool(connection_cls):
    if not connection_cls.pool:
        connection_cls.pool=Pool()
    return connection_cls.pool

def main():
    a=get_connection_pool(Connection)
    b=get_connection_pool(Connection)
    if a is b:
        print 'yes'
    else:
        print 'no'

if __name__ == '__main__':
    main()
