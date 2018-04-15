s='NXSTasasas'
aa='\n'.join(a for a in s.splitlines() if 'NXST' not in a )
if not aa:
    print'is None'
else :
    print  'not None'
