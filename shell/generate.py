import sys
from time import sleep

def generate():
    
    for i in range(10):
        sys.stdout.write('hello!This is sys.stdout NO.{}\n'.format(i))
        sys.stdout.flush()
        sleep(1)

    for i in range(10):
        sys.stderr.write('hello!This is sys.stderr NO.{}\n'.format(i))
        sys.stderr.flush()
        sleep(1)

if __name__ == '__main__':
    generate()
