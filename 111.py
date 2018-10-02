class ClientCache(object):
    
    def __init__(self, factory):
        
        self.factory = factory
        self._handler = None 

    def __get__(self, instance, owner):
        if self._handler is None:
            self._handler = self.factory(instance)

        return self._handler 

class Client(object):
    
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

def make_client(instance):
    return Client(instance.name)

class ClientManager(object):
    
    neutron = ClientCache(make_client)

    def __init__(self, name):
        self.name = name

client_manager = ClientManager('qian')

def get_client():
    return client_manager.neutron

print get_client().get_name()
