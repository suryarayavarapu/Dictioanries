# using exceptions
l1={1:"hi",2:"hello",3:"world"}
try:
    print(l1[4])
except KeyError:
    print("not found")

#print(l1[5])# key error not listed in dictionary l1

from collections import defaultdict
l1= defaultdict(lambda: 'key not found')
print(l1[6])

l1={1:"hi",2:"hello",3:"world"}
l2=[0,1]
for i in l2:
    if i in l1:
        print(i,l1[i])
    else:
        print(i,"not found")