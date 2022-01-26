values = [1, 2, "rahul", 4, 5]

#list is data type that allows multiple values and can be different data types

print(values[0]) # 1
print(values[3])
print(values[-1])
print(values[1:4])
values.insert(3, "shetty")
print(values)
print(values[0])
values.append("End")
print(values) # [1, 2, 'rahul', 'shetty', 4, 5, 'End']

values[2] = "Rahul" #updating
print(values)

del values[0] # deleting

print(values)

# Tuple - same as LIST data type but immutable
val = (1, 2, "rahul", 4.5)

print(val[1])
print(val)

# Dictionary
dic = {"a": 2, 4: "bcd", "c": "Hello world"}

print(dic[4])
print(dic["c"])

#
dict = {}

dict["firstname"] = "Rahul"
dict["lastname"] = "shetty"
dict["gender"] = "Male"

print(dict)
print(dict["lastname"])

