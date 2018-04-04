def hook(params):
    f=open('hook.txt','a+')
    f.writelines(str(params)+'\n')
    f.close()
