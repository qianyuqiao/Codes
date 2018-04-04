import neutron.extensions 
from oslo_config import cfg
import sys

CONF=cfg.CONF
CONF(sys.argv[1:])

def _get_private():
    print 'this is s private method'

def get_public():
    print 'this is a publiv method'

if __name__== '__main__':
    
    
    paths= ':'. join(neutron.extensions.__path__)
    try:
        if cfg.CONF.api_extensions_path:
            paths=':'.join([cfg.CONF.api_extensions_path,paths])
    except Exception:
        pass

    print paths
