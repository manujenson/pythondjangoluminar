
from re import *

pattern="ab"

matcher=finditer(pattern,"ababababbababa")

cnt=0
for match in matcher:
    print(match.start())
    print(match.group())
    cnt+=1
print(cnt)