# dict = {
#     "name" : "shraddha",
#     "cgpa" : 9.6,
#     "marks" : [98,97,95]
# }

# dict["name"],dict["cgpa"],dict["marks"]
# dict['key'] = "value"
# dict["marks"] = "value"
# humlog tuple change nhi kar sakt hai but dictionary and list ko change kar sakte hai

info = {
    "key" : "value",
    "namee" : "missingskill",
    "learning": "coding", 
    "subjects" :["python", "C","Java"],
    "age" :35,
    "is_adult": True,
    12.99 : 94.4
}

# print(info["namee"])
# print(info["topics"])
# print(info["subjects"]) 
# print(info("age"))
# print(info("is_adult"))

info["namee"] = "Manisha"  # overwrite 
info["surname"] = "seth"
print(info)


null_dict =  {}  # null dictionary 
null_dict["name"] = "missingskill"
print(null_dict)

# Nested dictionaries

student = {
    "name" : "shraddha",
    "score":{
        "chem" : 98,
        "phy" : 97,
        "math" :95
    }
}
print(list(student.values()))# return all values
# print(dict(student.keys()))
print(student.items()) # key value pair and print in tuple form
print(student.keys()) # it shows only key value
# print(student["name2"])  # if i show error in if i given name2 name square bracket notation it will show error
# if i will run this code it will not work after code
print(student.get("name2")) # it will not show error it will show none method it will shows not error(student.update("city":"delhi"))
new_dict = {"city": "delhi","age":16}
# student.update({"city":"delhi"})
student.update(new_dict)
print(student)
# dictionaries ke andar duplicate keys allowed nhi hoti











































