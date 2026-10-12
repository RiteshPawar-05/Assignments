list_1 = [12,22,33,44,45,22,33,45,77,88]
print("original list", list_1)
print("slicing operation in list :",list_1[0:5])
print()
print("indexing in list :")
print(list_1[0])
print(list_1[1])
print(list_1[2])
print(list_1[3])
dict_1  = {"umesh":78,
           "ranjit":89,
           "sagar":82,
           "yogesh":63,
           "kartik":66}
print("original dictonary :",dict_1)

dict_1["suhel"] = 66
print("dictonary after add operation :",dict_1)
print()
dict_1["yogesh"] = 94
print("dictonary after updating: ",dict_1)
print()
del dict_1["umesh"]
print("dictonary after delete operation",dict_1)
print()
print("sets operation ")
set_1 = {'22','22','56','66'}
set_2 = {'45','66','66','22'}
print("union of sets :",set_1 | set_2)
print("intersection of sets :", set_1 & set_2)

