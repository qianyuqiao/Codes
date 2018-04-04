import sys
import os
import cPickle as pickle
import six
from mymy import *
import itertools
from wsgiref.simple_server import make_server
import webob.dec
import json
import datetime
_simple_types=(six.string_types +six.integer_types+( type(None) , bool , float))
import inspect
import datetime
import copy


def get_type(object):
    return type(object)

def application(environ,start_response):
    start_response('200 ok',[('Content-type','text/html')])
    return '<h3>helloworld</h3>'

def run_server():
    print 'serving http on port 8000 ....'

    httpd=make_server('0.0.0.0',8000,application)
    httpd.serve_forever()

class Counter(object):
    def __init__(self):
        self.__counter=0
    def add(self):
        self.__counter+=1
    @property
    def value(self):
        return self.__counter
def countetest():
    counter=Counter()
    counter.add()
    counter.add()
    print counter.value

def new(s,b='b'):
    if not isinstance(s,str):
        print 's must be a string'
    else:
        print 's=',s,' b=',b

def new1():
    dir=r'd:\1\1.txt'
    dir=dir.replace('\\','/')
    print dir

def new2():
    path='/etc/'
    for f in os.listdir(path):
        print f

def repeat_in_list():
    mylist=list()
    mylist.append('a')
    if 'a' not in mylist:
        mylist.append('a')
    for i in mylist:
        print i
def file_a():
    f=open('/1.txt','a')
    f.write('a')
    f.close()

def serialization():
    d=dict(name='Bob',age=20,score=88)
    f=open('/dump.txt','wb')
    pickle.dump(d,f)
    f.close()

def deserialization():
    f=open('/dump.txt','rb')
    d=pickle.load(f)
    f.close()
    print d

def dict_type():
    d=dict()
    d[u'a']=1
    d[u'b']=2
    for name,value in d.items():
        if isinstance(name,six.string_types):
            print 'the type is ',type(name), 'and the name is ', name, ' and the value is ',value

def tuple_test():
        return ('qianyuqiao','21')

name,age= tuple_test()

def count():
    i=0
    for item  in itertools.count(100):
        if i>10:
            break
        print item
        i+=1
class Connection(object):
    _connection=None
    def __init__(self):
        self.base_num=0
        class_base_num=0
    def add(self,b):
        self.base_num+=b
    def sub(self,b):
        self.base_num-=b
    


class A(object):
    def __init__(self):
        self.lower='a'
        self.upper='A'

def change_A(obj):
    if isinstance(obj,A):
        obj.lower='b'
        obj.upper='B'
    else:
        print 'obj is not a instance of A'

def change_string(s):
    if isinstance(s,str) and s.index(s)>-1  :
        s=s.replace('a','')
    else:
        print 'Error in change_string'
def main():
    s='abcd'
    print 'before pass into change_s, s= ',s
    change_string(s)
    print 'after pass into change_s, s=', s

def dicttest():
    d={'a':{'a':1}}
    d.get('a')
    d['a']=2
    print d


class B(object):
    def __init__(self):
        print 'before,dir: '+str(dir(self))
        self.name='qianyuqiao'
        print 'after,dir: '+str(dir(self))

class Singleton(type):
        
    def __init__(cls,name,bases,attrs):
        print 'you have created a class!'
        super(Singleton,cls).__init__(name,bases,attrs)
        cls._instance=None

    def __call__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance=super(Singleton,cls).__call__(*args,**kwargs)
            print 'you have created an instance!'
            return cls._instance

class MyClass(object):
    __metaclass__ = Singleton


aa=None

def a():
    global aa
    aa=2
    aa+=2
def do():
    a()
    global aa
    aa+=1
    print aa

class Middleware(object):
    
    @classmethod
    def factory(cls,global_conf,**local):
        return cls

    def __init__(self , application):
        self.app=aplication

    def process_request(req):
        
        return None

    def process_response(response):
        
        return response
    
    @webob.dec.wsgify
    def __call__(self,req):
        response=self.process_request(req)
        if response:
            return response
        response=req.get_response(self.application)
        return self.process_response(response)

def copy_t():

    a= {'a':1,'b':2,'c':3}
    aa=a
    del aa['a']
    print 'aa',aa
    print 'a',a

class Cycle(object):
    def __init__(self):
        self.obj=None
    
    @property
    def bind(self):
        return self.obj

    @bind.setter
    def bind(self,obj):
        self.obj=obj

class Left(object):
    def __init__(self):
        self.obj=None
    
    @property
    def bind(self):
        return self.obj

    @bind.setter
    def bind(self,obj):
        self.obj=obj
def main():
    #to prove that all elements , including the subelement ,are transformed
    python2json={}
    listdata=[1,2,3]
    dictdata={'a':1,'b':2}
    python2json['listdata']=listdata
    python2json['dictdata']=dictdata
    json_result=json.dumps(python2json)
    print json_result

def now():
    print datetime.datetime.now()

def count(start_val=0,step=1):
    num=start_val
    while True:
        yield num
        num+=step

class Container(object):
    
    def __init__(self,start=0,end=0):
        self.start=start
        self.end=end

    def __iter__(self):
        print 'iterator created!'
        return self

    def next(self):
        print 'get next number'
        if self.start<self.end:
            i=self.start
            self.start+=1
            return i
        else:
            raise StopIteration()

#this is a generatorfunction . which means , inspect.isgeneratorfunction(gen) is True
#and a generator can be stopped
def gen():
    i=0
    print 'generator created!'
    while True:
        yield (i,i*i)
        i+=1
        if i>20:
            break

def time2str(time):
    TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
    if isinstance(time ,datetime.datetime):
        timestr= time.strftime(TIME_FORMAT)
        print type(timestr)
        return timestr

    else:
        raise TypeError()

class Q(object):
    class_var=1
    def __init__(self):
        self._name='qianyuqiao'
        self._age=22

    @property
    def age(self):
        return self._age
    
    def fun(self):
        pass
    
#key dict
def key_dict():
    a=Q()
    b=Q()
    _dict={a:'1',b:'2'}
    print _dict

def aaa():
    print 'aaa'
    time.sleep(1)
    bbb()
    

def bbb():
    print 'bbb'
    time.sleep(1)
    aaa()
    

def update_dict(obj,dict,attributes):

    for attr in attributes:
        if getattr(obj,attr,None):
            dict[attr]=getattr(obj,attr)

COMMANDS=['net-list']
def find_command(argv):
    search_argv=argv[:]
    name=''
    while search_argv:
        if search_argv[0].startswith('--'):
            raise ValueError('Invalid command!')
        val=search_argv.pop(0)
        name = '%s %s'%(name,val) if name else val
        return  name

def _merge_args(parsed_args,_extra_values):
    #shallow copy
    _extra_tmp = _extra_values.copy()
    for key,value in _extra_tmp.iteritems():
        
        print key
        
        if getattr(parsed_args,key,None):
            
            print 'found!'
            arg_value=getattr(parsed_args,key)
            
            if value and isinstance(arg_value,list) and isinstance(value , list):
                if type(arg_value[0])  == type(value[0]):
                    print 'yes'
                    arg_value.extend(value)
                    _extra_values.pop(key)

class C(object):

    a='abc'
    
    def __get__(self,instance,owner):
        
        print '__get__ is called!',instance,owner
        return self

class C2(object):
    d= C()

def parse_args_to_dict(value_specs):
    specs={}
    index=-1
    config_index=[]
    for item in value_specs:
        index+=1
        if item.startswith('--'):
            item=item.replace('--','')
            config_index.append(index)

    for i in config_index:
        specs[value_specs[i]]=value_specs[i+1]
    return specs

def test3():
    l=['--config-file','/etc/neutron/neutron.conf','--tenant_id','helloworld']
    for i in l:
        if i.startswith('--'):
            i=i.replace('--','')
    return l

class B(object):
    
    def __init__(self,name):
        self.name  =name

    def sayHello(self):
        return 'hello world!'
    
    def position(self):
        return self.__class__.__name__ 

def show_dict(cls):
    
    for value in cls.__dict__.values():
        print value

class ObjectDict(dict):
    
    def __init__(self,*args,**kwargs):
        super(ObjectDict,self).__init__(*args,**kwargs)

    def __getattr__(self,name):
        value=self[name]
        if isinstance(value,dict):
            value=ObjectDict(value)
        return value


class  Mydatetime(object):
    
    def __init__(self):
        self.name='nihao'

    @classmethod
    def now(cls):
        return  cls()
    
    def __repr__(self):
        return self.name


