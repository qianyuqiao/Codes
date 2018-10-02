def inner(num):
    if num == 1:
        raise ValueError("value error")

def haha(num):
    if num == 1:
        raise Exception("num is 1")

def main(num):
    try:
        inner(num)
    except Exception as e:
        raise e

def outer(num):
    try:
        main(num)
    except Exception as e:
        raise Exception('outer')

outer(1)
