import os
import imp
def load_all_extensions_from_path(path):
    for f in sorted(os.listdir(path)):
        mod_name,file_ext=os.path.splitext(os.path.split(path)[-1])
        ext_path=os.path.join(path,f)
        if file_name.lower== '.py' and not mod_name.startswith('_'):
            mod=imp.load_source(mod_name,file_ext)
            ext_name=mod_name[0].upper()+mod_name[1:]
            new_ext_class=getattr(mod,ext_name,None)
            if not new_ext_class:
                raise NotImplemented
        new_ext=new_ext_class
        

    
