f = open("vehicleregno","r")
for lines in f:
    line=lines.rstrip("\n")
    from re import *
    rule="[a-zA-Z]{2}\d{2}[a-zA-Z]{2}\d{1,4}"

    matcher=fullmatch(rule,line)
    if matcher==None:
        print("invalid ")
    else:
        print("valid =>",line)
