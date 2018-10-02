import re
UUID_PATTERN = '[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}'
print UUID_PATTERN
s = '12345678-1234'
match = re.match(UUID_PATTERN, s)
if match:
    print match.group(0)
else:
    print 'No matched'
