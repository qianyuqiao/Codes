import re
HEX_ELEM =  '[0-9a-fA-F]'
UUID_PATTERN = '-'.join([HEX_ELEM + '{8}',HEX_ELEM + '{4}'])
print UUID_PATTERN
s = '12345678-asfg'
match = re.match(UUID_PATTERN, s)
if match:
    print match.group(1)
else:
    print 'No matched'
