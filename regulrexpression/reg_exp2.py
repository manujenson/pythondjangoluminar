from re import *

#predefined chara set

#pattern="[ab]"
#pattern="[a-z]"
#pattern="[A-Z]"
pattern="[0-9]"
pattern="[^0-9]"#except 0-9
pattern="[a-zA-Z0-9]"#all words
pattern="[ab]"

#another pre defined
pattern="\s"#chk for spaces
pattern="\d"#chk for digit
pattern="\D"#except digit

pattern="\w"#chk for all words
pattern="\W"#except words
matcher=finditer(pattern,"abc _72k@c")


for match in matcher:
    print(match.start(),"=>",match.group())