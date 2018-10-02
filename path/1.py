import os
import os.path
path = '/home/qianyuqiao/codes'

if not os.path.exists(path):
    raise Exception('path does not exist')
else:
    for f in os.listdir(path):
        print os.path.split(path)
