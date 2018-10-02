from datetime import datetime

def log_time(f):
    def func(*args, **kwargs):
        start = datetime.now()
        result = f(*args, **kwargs)
        end = datetime.now()
        print 'interval is %s' % str(end - start)
        return result

    return func

def do_post():
    print 'do post'

def do_get():
    print 'do get'

def do_put():
    print 'do_put'

def do_delete():
    print 'do_delete'


actions = ['POST', 'GET', 'PUT', 'DELETE']

def get_action_dict():
    action_dict = dict()
    for action in actions:
        action = action.lower()
        action_dict[action] = __module__

@log_time
def test_if(method):
    if method == 'POST':
        do_post()
    elif method == 'GET':
        do_get()
    elif method == 'PUT':
        do_put()
    elif method == 'DELETE':
        do_delete()
    
@log_time
def test_match():

