f = open("1.txt", "w")
for i in xrange(1000):
    f.write("Hosts:" + "#"*10)
    f.write("\n")

f.close()
