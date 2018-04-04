import struct
f=open('/home/qianyuqiao/codes/text.txt','w+')
a=12
bytes_a=struct.pack('i',a)

f.writelines(bytes_a)
f.close()
