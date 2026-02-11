# ihave value i need to update key
t = {"a": 1, "b": 2, "c": 3}
new_key='e'
for_value=2
for key,value in list(t.items()):
    if value ==for_value:
        del t[key]#key=new_key#its INDEX IS KEY SO WE CANT CHANGE
        t[new_key]=for_value
print(t)

del t["c"]
print(t)

#pop with item
print("===========")
key, value=t.popitem()
print(key ,value)

print("===========")
#pop with key
print(t.pop('a')) # for pop item we are providing index

t.clear()
print(t)
