from re import *
gmail= input("enter email")
rule = '[a-zA-Z.]*[/d]*@gmail.com'

matcher = fullmatch(rule, gmail)
if matcher == None:
    print("invalid mail id")
else:
    print("valid mail id")