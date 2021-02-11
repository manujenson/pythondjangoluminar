f = open("emailid","r")
for lines in f:
    line=lines.rstrip("\n")
    from re import *

    rule = '[a-zA-Z.]*[\d]*@+[a-z.]*'
    matcher = fullmatch(rule,line)
    if matcher == None:
         print("invalid mail id")
    else:
         print("valid =>",line)