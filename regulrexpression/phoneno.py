f = open("phonenumbers","r")


phoneno=[]
for lines in f:
    line=lines.rstrip("\n")
    from re import *
    rule="(91)?\d{10}"

    matcher=fullmatch(rule,line)
    if matcher==None:
        print("invalid ")
    else:
        print("valid =>",line)
        phoneno.append(line)
        print(phoneno)
