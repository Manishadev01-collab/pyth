# for loops & while loops 

# while True :
#     print("hello")  # loops goes on 


# count = 1
# while count <=5 :
#     print("hello")    
#     count += 1
#     print(count)


# count = 2 
# while count <=7 :
#     print("HELLO WORLD")
#     count += 1

# i =1 # iterator
# while i<=100:
#     print("apna college",i)   
#     i+=1 

# print numbers from 1 to 5

# i = 5
# while i <=5:
#     print(i)
#     i -=1

# print("loops ended")

# lets practice 
# print numbers from 1 to 100 

# i = 1
# while i<100:
#     print(i)
#     i+=1

#     i = 100
# while i>=1: # stopping condition
#     print(i)
#     i -=1


# print the multiplication table of a number to n 
# n = int(input("enter number:"))
# i = 1
# while i<=10:
#     print(n*i)
#     i+=1

# print the elements of the following list using a loop 
# nums = [1,4,9,16,25,36,49,64,81,100]

# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3]) #  print nums 
# idx = 0
# while idx <len(nums):
#     print(idx)
#     idx +=1

# heroes = ["ironman", "thor", "superman", "batman"]
# idx = 0
# while i <len(nums):
#     print(heroes[1])
#     idx +=1



    





# Search for a number x in this tuple using loop
# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 36
# i = 0   # intialization
# while i <len(nums):
#     if(nums[i] == x):
#         print("Found at idx ", i)
#         break
#     else:
#         print("finding")
#     i +=1
#     print("end of loop")





#  nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 36
# i = 0

# while i < len(nums):
#     if nums[i] == x:
#         print("Found at idx", i)
#         break
#     i += 1

# print("Search completed.")

    # break and continue

# break : used to terminate the loop when encountered 
#continue :terminates execution between the 

# i = 1
# while i <=5:
#     print(i)
#     if(i==3):
#         break
#         i+=1
#         print("end of the loop")


 # continue do not break iteration
# i = 0
# while i<=10:
#     if(i%2 ==0):
#         i +=1
#         continue # skip
#     print(i)


# i = 0
# while i <= 10:
#     if i % 2 != 0:  # Check for odd numbers
#         print(i)
#     i += 1


# i = 0
# while i <= 10:
#     if i % 2 == 0:  # Check for even numbers
#         print(i)
#     i += 1


# for loops are used for sequential traversal . for traversing list , string tupkes etc.
# for loops el in list 


# veggies = ["potato", "brinjal","ladyfinger","cucumber"]

# # list = [1,2,3,4,5]
# for val in veggies:
#     print(val)

# tup = (1,2,3,4,2,8,9)

# for num in tup:
#     print(num)


# str = "missingskill"

# for char in str:
#     print(char)    # individual character
# else:
#  print("END")


 # Lets practice 
# using for 
# print elements of the following list using a loop for 
#  nums = [1,4,9,16,25,36,49,64,81,100]
#  for el in nums:
#      print(el)

# Search for a number x in this tuple using loop   #linear search single line search termonology of programming
# nums = (1,4,9,16,25,36,49,64,81,100,49)
# x = 49
# idx = 0
# for el in nums:
#    if(el == x) :
#        print("number found at idx:",)
#        idx +=

# nums = (1,4,9,16,25,36,49,64,81,100,49)
# x = 49
# idx = 0
# for el in nums:
#    if(el == x) :
#        print("number found at idx:",)
#        idx +=1

       # This is the most reliable way to get the correct index
# for idx, el in enumerate(nums):
#     if el == x:
#         print("number found at idx:", idx)


# range is a n important function return a sequence of numbers , starting from  0 
# by default  and increment  by 1 (by default) and stops befor e a specified mannner

# range(start?,stop,step?)
# seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])

# for i in seq:
#     print(i)

# for i in range(10): # stop condition
#     print(i)   

# for i in range(2,10): # range(start, stop)
#     print(i)  

# for i in range(2,10,2): # range(start, stop)
#   print(i) 


#   for i in range(2,100,2):
#     print(i)

    
#   for i in range(2,101,2):
#     print(i)
# for i in range(1,101,2):
#     print(i)


# Lets Practice 
# using for and range()

# Print numbers from 1 to 100
# for i in range(1,101):
#     print(i)

# print numbers from 100 to 1 step size decreasing order
# for i in range(100, 0 , -1):
#     print(i)

# print the multiplication table of a number of n

# n = int (input('enter number :'))
# for i in range (1 ,11):
#     print(n *i)


    #  Pass statement is anull statement that does nothing . It is used as a placeholder for future code 


# for el in range(10):
#        pass 
# if i>5:
#         pass
#         print('some useful work')



# Wap to find the sum of first n numbers (using while)
n = 5
for i in range(n+1):
   print(i)

for i in range(1,n+1):
 print(i)


n = 5
sum = 0 
for i in range(1,n+1):
   sum +=i
   print("total sum =", sum) 

 # using while loop 

n = 7 
sum = 0 
i = 1
while i<= n:
  sum +=i
  i += 1
  print("total sum =", sum )

# Wap to find the factorail of first n numbers (using for)
#1 *2*3*4*5



# n = 3
# fact = 0 
# i = 1
# while i<= n:
#   fact *=i
#   i += 1
#   print("factorail =", fact ) Wrong code 



n = 4
fact = 1  # Initialize 'fact' to 1, not 0
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)


































    
















































