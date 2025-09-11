age = 24
if(age >= 18):
    print("can vote")
else:    
    print("cannot vote")


light = "green"
if(light== 'red'):
    print("stop")
elif(light == 'green'):
    print("go")  
elif(light == 'yellow'):
    print("look") 

else:
    print("light is broken")      

    print("end of the code")   

    num = 5
    if(num >2):
        print("greater than 2")
    elif(num>3):
        print("greater than 3")   
    


    # If statements in python
is_hot = False
is_cold = True
if is_hot:
  print("It is a hot day" )
elif is_cold:
  print("It is a cold day")
  print("Wear Warm clothes")
else:
 print("It is lovely day")
 print("enjoy able day")


 # Problem 
#  Price of a house is $ 1M
# If buyer has a good credit 
# they need to put down 10% 
# Otherwise 
# they need to put down 20%
#  print the down payment

Price = 1000000
has_good_credit = True

if has_good_credit:
  down_payment: 0.1 * Price
else:
  down_payment :  0.2 * Price
# print(f"Down Payment: ${down_payment}")


marks = input("enter students Marks :")

# Convert the input string to an integer
marks = int(marks) 

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student ->", grade)


# WAP to check if a number entered by the user is odd or even

num = input("enter number :")

num = int(num)

rem = num %2
if(num %2 == 0):
   print("EVEN")
else: 
   print("ODD")   


   # Wap to find the greatest of 3 number entered by the User 

   a = int(input("enter first number:"))
   b = int(input("enter second number"))
   c = int(input('enter third number'))
   if(a>=b and a>=c):
      print("first number is largest",a)
   elif(b>=c):
      print("second number is largest",b)
   else:
      print("third is largest",c)



   # Wap to check if a number is a multiple of 7 or not 

   x = input("enter number")
   x = int(x)

   if(x% 7 == 0):
      print("multiple of 7")
   else:
      print("not a multiple of 7")   












    

