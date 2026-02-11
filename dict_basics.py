dict1={'apple': 5, 'banana': 2, 'cherry': 7}
#dictionary printing
print(dict1)
#i want key from value
x=7

for key,value in dict1.items():#for loop itereation required ".items()"
    if value==x:
        print(key)
#i want value from key
y='banana'
for key,value in dict1.items():
    if key==y:
        print(value)

print("=======")

#all keys, all values, all kev value pairs
for key,value in dict1.items():
    print(key,value)
    print(key)
    print(value)
print("\n")

print(dict1['apple'])#individual values accessed by index like list
print("========")
print(dict1.get('banana'))#using get method

print("========")
dict4={2:3,4:1,6:7}
dict5={key:values for key,values in dict4.items()}
print("==========")
print(dict5)

#dictionary constructor asssingment operator"=" is required if i put ":" will errored out "invalid syntax"
dict2=dict(v1="apple",v2="orange")
print(dict2)


# adding dictionary items
dict1["grapes"]=5
print(dict1)
#update dictinary with new
dict1['apple']=10
print(dict1) 

d = {1: 'Geeks', 2: 'For', 'age':22}
for k in d:
    print (k)     
for k in d.items():
    print (k) 
for k in d.values():
    print(k)
    