# sets are immutable  MEANS IT will not changed after assign a value
# boolean -    true false  float 2.9 str -m "abc" tuple  - (123)
# these values are set on set 
# list and dictionaries are not on set 

# collection = {1,2,3,4,5, "hello ", "world", "world"}
# print(collection)
# print(type(collection))# sets are unordered
# print(len(collection)) # duplicate elements ko kaise create kaise karta hai 
collection = set() # empty set : syntax
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("hello")
collection.add((1,2,3)) # unhashable value jo change hoti hai value 
collection.clear() # empties the set
collection = {"hello","apnacollecge","world","coding","python"}
print(collection.pop()) # random value is removed
print(len(collection))

print(len(collection))





# collection.remove()


# print(type(collection))

 # SET METHODS
 # SETS ARE MUTABLE AND ELEMENTS ARE NOT MUTABLE
 #.ADD TUPLE KO PASS KAR SAKTE HAI BUT LIST AUR DICTIONARY KO PASS NHI KAR SAKTE HAI

set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2)) # {1,2,3,4} combines both set values & return new
print(set1)
print(set2)
print(set1.intersection(set2)) # common values


# Lets Practice

 # store the folowing word meanings in python dictionary:

 # table : "a piece of furniture " , "List of facts & figures"
 # cat : " a small animal"

 # you are a given a list of subjects for students . Assume one classroom is required for 1
 # subject . How many classrooms are needed by all students.
# "python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++","C"  5 classrooms


dictionary = {
    "cat" : " a small animal",

    "table" : [" a piece of furniture ", "list of facts & figures"]
}
print(dictionary)

 # subjects subjects = {
subjects = {
  "python", "java","c++", "python", "javascript", "java",
  "python", "java","c++","C"
 }
print(len(subjects))


# Wap to enter marks of 3 subjects from the user and store them ina dictionary . 
# Start with an empty dictionary & add one by one . Use the subject name as key & marks as avalue
# marks = {}
# x = int(input("enter phy"))
# marks.update({"phy":x})

# x = int(input("enter math"))
# marks.update({"math":x})

# x = int(input("enter chem"))
# marks.update({"chem":x})

# print(marks)

# figure out a way to store 9 & 9.0 as seprate values in the set .
# (you can take help of built in data types)

# Wap to enter marks of 3 subjects from the user and store them in a dictionary . 
# Start with an empty dictionary & add one by one . Use subject name as key & marks as value.

values = {9, 9.25,8 , 8.0}
values = {9, "9.0"}
print(values)


# Figure out a way to store 9 & 9.0 as separate values int he set .
# (you can take help of built in data type)

# 9 --> int
# 9.0 --> float 
#[("float", 9.0) value]
#[("int", 9) value]

values = {
   ( "float", 9.0),
   ("int", 9)
}
print(values)













































