from re import *
regno=input("enter reg no")
rule="kl\d{2}[a-z]{2}\d*"

matcher=fullmatch(rule,regno)
if matcher==None:
    print("invalid variable name")
else:
    print("valid variables")
