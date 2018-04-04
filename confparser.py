import ConfigParser,os

config=ConfigParser.ConfigParser()
config.readfp(open('t.conf'))
for section in config.sections():
    for name,value in config.items(str(section)):
        print name,'=',value
