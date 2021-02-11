#quantifirs
from re import *

pattern="a+"#any no of a including blank no
pattern="a*"#any no of a excluding other
pattern="a?"#single groups
pattern="a{2,4}"#limits

matcher=finditer(pattern,"aaaaabaabaabaa")


for match in matcher:
    print(match.start(),"=>",match.group())