t = {"a": 4, "c": 3, "b": 2}

print(sorted(t))
print(sorted(t.items()))#key value tuple sort  ascending  placed it in list
print(t)
#i want to see sort in dictionary not as tuple dictionary
dict1={key:values for key,values in sorted(t.items())}
dict2={key:values for key,values in sorted(t.items(),reverse=True)}
print(dict1,"\n",dict2)
#above key are sorted, but not sorted by values
#sorted by values
dict3={key:values for key,values in sorted(t.items(), key=lambda item :item[1], reverse=True)}
dict8={key:values for key,values in sorted(t.items(), key=lambda item :item[0], reverse=True)}
print(dict3)
print(dict8)
dict4={2:3,4:1,6:7}
dict5={key:values for key,values in dict4.items()}
print("==========")
print(dict5)