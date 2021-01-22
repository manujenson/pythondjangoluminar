#read,write,append

#stp 1 :create a reference
#den open from it

f=open("demo","r")

for lines in f:
    print(lines)

#in to a word list
f=open("demo","r")

word=[]
for lines in f:
    word.append(lines.rstrip("\n").split(" "))
print(word)
mywords=[]
for lst in word:
    for wrd in lst:
        mywords.append(wrd)
print(mywords)
