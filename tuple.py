tup = (2,1,3,1)
print(tup[0])
print(tup[1])
print(type(tup))

tup = ("hello",) # if we do not write comma  it will show string so put comma  inside the tuple
print(type(tup))

tup = (1,2,3,4)
print(tup[1:3])
print(tup.index(2))
print(tup.count(2)) # kine baar aata hai 2 

 # Wap to ask their user to enter names of their favourite Movies  & store them in a list
movies = []
mov1 = input("enter 1 st movie")  
mov2 = input("enter 2 nd movie")  
mov3 = input("enter 3 rd movie") 

movies .append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# Wap to check if a list contains a palindrome of elements . (Hint : use copy() method)
# [1,2,3,2,1]  [1,"abc","abc",1]

list1 = [1,2,3]
# list1 = ["m","a","a","m","p"] # not palindrome
list2 = [1,2,3]

copy_list1 = list1.copy()

copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")  


# Wap to count the number of students with th "A"   grade in the folloeing tuple   
["C","D","A", "A", "B", "A"] 

grade = ("C", "D" , "A" , "A", "B" , "A")
print(grade.count("A"))


# store the values in a list & short them from "A "to  "D"
# Assending order create this tuple
grade = ("C", "D" , "A" , "A", "B" , "A")
grade.sort()
grade.sort()

hello = "hello"










