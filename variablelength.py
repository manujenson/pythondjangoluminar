def add(*args):
    return sum(args)


tot=add(10,20,30,40,50)
print(tot)

#
def print_data(**kwars):
    print(kwars)

print_data(name="manu",worklocation="kakanad",home="tcr")