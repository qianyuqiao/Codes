f=open('/home/qianyuqiao/codes/text.txt','r')
for line in f.readlines():
    print line.decode('ascii')
f.close()
