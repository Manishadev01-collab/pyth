# Function and recursion

# Block statements that peform  a specific task:
# def func_name(param1, param2..):
    # some work 
    # return 
    # func_name (arg1,arg2 ...) # function call 

# def sum(a,b):
#         s = a +b
#         return s 
# print(sum(2,3))

# a = 5
# b = 10
# sum = a +b 
# print(sum)



# a = 2
# b = 10
# sum = a +b 
# print(sum)
#  retdent code is bohot kharab programmer ki nishani hoti hai



# def cal_sum(a,b):
#   sum = a +b     # parameters are input
# print(cal_sum)



# def cal_difference (a,b):
#       difference = a -b 
#       print(difference)


# def cal_sum (a,b):
#     sum = a + b 
#     print(cal_sum)  
#     print (sum)  
#     return sum 
# cal_sum(5,10) # argument value supply in python function 
# cal_sum(2,10) # number of line decresase because of function and also rebundacy decrease in code 
# cal_sum(3,10)
# function defination
def cal_sum(a,b): # parameters
      return a + b
sum = cal_sum(1,2)
sum = cal_sum(178,222) # function call ; arguments
print(sum)
print(sum)

def print_hello():
      print("hello")
print_hello() 
print_hello()      
print_hello()      
print_hello() 
print_hello()   


def print_hello():
      print("hello")
output = print_hello()
print(output) # None value  because this function returns noting in that particuar function 



# average of 3 numbers 
def calc_avg(a,b,c):
      sum = a + b + c
      avg = sum/3
      print(avg)
      return avg

calc_avg(1,2,3)
calc_avg (98,97,95)



# Built in function 

# print()
# len()
# type()
# range()


# User defined functions  # ham likte hai 3 built in function 

# print("missingskill", end= " " )# sep = "" do not giving spaces

# print("manishaseth") # end = "\n"

# print("manisha seth")  


# default parameters

# def cal_product(a = 1,b = 2):
#       print(a + b)
#       print(a * b)
#       return a +b

# cal_product(1)


# WAF TO PRINT THE LENGTH OF A LIST (LIST IS THJE PARAMETERS)

# WAF TO PRINT THE E;EMENTS OF A LIST IN A SINGLE LINE. (LIST IS THE PARAMETER)

# WAF TO FIND THE FACTORAIL OF N (N IS THE PARMAETER)

# WAF TO CONVERT USD TO INR

# cities = ["delhi", "gurgaon", "noida", "pune", "chennai","mumbai"]
# heroes = ["thor", "ironman", "captain america", "shaktiman"]
# print(len(cities))

# def print_len(list):
#       print(len(list))


# print_len(heroes)     
# print(heroes[0], end = "\n") 
# print(heroes[1], end = " \n")



def print_list(list):
      for item in list :
            print(item, end=" ")


n= 5
fact = 1
for i in range(1, n+1):
      fact *=i
    #   print(fact())

def cal_fact(n):
      fact = 1
      for i in range(1, n+1):
            fact *= i


print(fact)

cal_fact(6)




# WAF to convert USD to INR 
#  1 dollar = ruppes 83


def converter(usd_val):
      inr_val = usd_val *83
      print(usd_val,"USD =", inr_val,"INR")


converter(100)      # dollar conveter 

# number input lega ek function andar likna hai and 
# if woh number odd hai toh string mein odd print karegaa  
# and agar woh even hai toh string even print karegaa



# Recursion

# when a function calls itself repeatedly
 # loops ka khatarnak version hai
# def show(n):
#       if(n==0) :
#             return
#       print(n)
#       show(n-1)


# def show(n):
    # Base case: The recursion stops when n is 0.
#     if n == -1:
#         return
    
    # Recursive step: Call the function with the next smaller number.
#     show(n - 1)
    
    # Print the current number.
    # This print statement is executed on the "return trip"
    # of the recursive calls, printing from 1 to 5.
#     print(n)

# Initial call to the function with n = 5
# show(5)

# n!=n×(n−1)×(n−2)×⋯×1


def factorial(n):
    # Base Case: Stop the recursion when n is 0.
    if n == 0:
        return 1 # Base case
    # Recursive Step: Call the function with n-1.
    else:
        return n * factorial(n - 1)

# Example usage
# print(f"The factorial of 4 is: {factorial(4)}")
# Output: The factorial of 4 is: 24




# For example, 4!=4×3×2×1=24.

# This can be defined recursively as:

# Base Case: 0!=1

# Recursive Step: n!=n×(n−1)!

# Python Code
# Here's how to implement the factorial function using recursion in Python:

# Python

# def factorial(n):
#     # Base Case: Stop the recursion when n is 0.
#     if n == 0:
#         return 1
#     # Recursive Step: Call the function with n-1.
#     else:
#         return n * factorial(n - 1)

# # Example usage
# print(f"The factorial of 4 is: {factorial(4)}")
# # Output: The factorial of 4 is: 24
# How the Code Works for factorial(4):
# factorial(4) is called. Since 4
# 
# =0, it returns 4 * factorial(3).

# factorial(3) is called. It returns 3 * factorial(2).

# factorial(2) is called. It returns 2 * factorial(1).

# factorial(1) is called. It returns 1 * factorial(0).

# factorial(0) is called. This is the base case, so it returns 1


# call stack ka mtlb hai ek call ke upar dusra call 



# if i comment out base part in recursion then it will work in
#  infinite in loops but it will crash the code 
# so be careful after  commenting the base part in code
# program band ho jayegaa 


# n! = (n-1)!*n

# 5! = 4! *5
# 1*2*3*4*5

def fact(n):
       if(n == 1 or n == 0):
             return 1
       return fact(n-1) * n

print(fact(6))



# write a  recursive function to calculate the sum of first n natural numbers 

# def calc_sum(n):
#       if(n==0):
#             return
#       print(n)
#       return calc_sum(n-1) + n

# sum = print(calc_sum(5))
# print(sum)





#       def calc_sum(n):
#     if n == 0:
#        return 0
#     return n + calc_sum(n - 1)

# print(calc_sum(10))




# Write a recursive function to print all elements in a list .
# Hint: use a list & index as parameters

# def print_list(list,idx):
#       if(idx == len(list)):
#             return
#       print_list(list,idx+1)


# fruits = [ "mango", "litchi", "apple", "banana"]
# print_list(fruits)



def print_list(lst, idx):
    if idx == len(lst):
        return
    print_list(lst, idx + 1)
    print(lst[idx])

fruits = ["mango", "litchi", "apple", "banana"]
print_list(fruits, 0)











































































































