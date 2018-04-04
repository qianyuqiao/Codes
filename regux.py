import re
f='[**]  asa   asa  [end]'
pat=re.compile(r'\](\s+)(\w+\s+\w+)(\s+)\[')
print pat.findall(f)
