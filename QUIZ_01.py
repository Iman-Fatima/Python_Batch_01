# QUIZ_01
# Problem Statements
# Q - 01
# Write a program that will take three integers as user defined inputs and prints the maximum number out of them.
# Solution:-


# number_1 = (input("Enter the 1st Number: "))
# number_2 = (input("Enter the 2nd Number: "))
# number_3 = (input("Enter the 3rd Number: "))

# if (number_1 >= number_2) and (number_1 >= number_3):
#    maximum = number_1
# elif (number_2 >= number_1) and (number_2 >= number_3):
#    maximum = number_2
# else:
#    maximum = number_3

# print("The Maximum Number Is", maximum)


# <--------------- OUTPUT --------------->  

# Enter the 1st Number: 55
# Enter the 2nd Number: 78
# Enter the 3rd Number: 95
# The Maximum Number Is 95



# Q - 02
# Write a program to calculate Area of Circle by taking radius as input.
# Solution:-


# print(f"In order to calculate Area of Circle")
# radius = int(input("Enter the Radius of the Circle: "))
# area_of_the_circle = 3.14*(radius**2)
# print(f"The Area Of The Circle Is {area_of_the_circle}.")


# <--------------- OUTPUT --------------->  

# In order to calculate Area of Circle
# Enter the Radius of the Circle: 2
# The Area Of The Circle Is 12.56.


# Q - 03
# Write a program to calculate percentage of total marks obtained in final term for a student.
# Solution:-


# total_marks = int(input("Enter the Total Marks: "))
# obtained_marks = int(input("Enter the Obtained Marks:"))
# percentage = (obtained_marks / total_marks)*100
# print(f" Congratulation, You scored {percentage} % in the FINAL TERM.") 

# <--------------- OUTPUT --------------->  

# Enter the Total Marks: 1100
# Enter the Obtained Marks:1021
#  Congratulation, You scored 92.81818181818183 % in the FINAL TERM.


# Q - 04
# Write a program to print whether the user defined number is a prime number or not with proper message.
# Solution:-


# number_1 = int(input("Enter a number: "))
# if number_1 > 1:

#     for i in range (2,number_1):
#         if (number_1 % i) == 0:
#             print(f"The given number is not a prime number.")
#             break
#     else:
#         print(f"The given number is a prime number.")

# <--------------- OUTPUT --------------->  

# Enter a number: 4
# The given number is not a prime number.

# Q - 05
# Write a Python program to check whether an alphabet is a vowel or consonant.
# Solution:-


# alphabet = (input("Enter an ALPHABET : "))
# if alphabet=="A" or alphabet== "E" or alphabet=="I" or alphabet=="O" or alphabet=="U" or alphabet=="a" or alphabet=="e" or alphabet=="i" or alphabet=="o" or alphabet=="u": 
#     print(f"The given alphabet {alphabet} is  a VOWEL. ")
# else:
#         print(f"The given alphabet {alphabet} is  a CONSONANT. ")

# <--------------- OUTPUT --------------->  

# Enter an ALPHABET : R
# The given alphabet R is  a CONSONANT. 

# .............................................................................................
# Q - 06
# Write a Python program to sum up two user defined integers. However, if the sum is:
#     Below Zero - Display "Bigger number was negative"
#     Equal to ZERO - Display "Both numbers were equally distant on number line on opposite sides"
#     Greater than ZERO - Display "Bigger number was positive"
# Solution:-


number_1 = int(input("Enter the first number : "))
number_2 = int(input("Enter the second number : "))
result = number_1 + number_2
print(f"The {result} is the sum of the given numbers. ")
if result ==0:
    print(f" As the result is equal to zero so, both numbers were equally distant on number line on opposite sides")
elif result < 0 :
    print(f"As the result is below zero so, the bigger number was negative")
elif result > 0 :
    print(f"As the result is greater than zero so, the bigger number was positive")


# <--------------- OUTPUT --------------->  

# Enter the first number : -2
# Enter the second number : 1
# The -1 is the sum of the given numbers. 
# As the result is below zero so, the bigger number was negative

# Enter the first number : 5
# Enter the second number : 6
# The 11 is the sum of the given numbers. 
# As the result is greater than zero so, the bigger number was positive

# Enter the first number : 7
# Enter the second number : -7
# The 0 is the sum of the given numbers. 
#  As the result is equal to zero so, both numbers were equally distant on number line on opposite sides

# .....................................................................................

# Q - 07
# Write a Python program to check whether two user defined integers are additive inverse of each other.


# integer_1 = int(input("Enter the first Integer: "))
# integer_2 = int(input("Enter the second Integer: "))
# if integer_1 + integer_2 ==0:
#     print("The user defined Integers are the ADDITIVE INVERSE of each other.")
# else:
#     print("The user defined Integers are not the ADDITIVE INVERSE of each other.")


# <--------------- OUTPUT --------------->  

# Enter the first Integer: 8
# Enter the second Integer: 8
# The user defined Integers are not the ADDITIVE INVERSE of each other.

# ......................................................................................................

# Q - 08
# Write a Python program to check whether two user defined integers are multiplicative inverse of each other.
# Solution:-



# integer_1 = int(input("Enter the first Integer: "))
# integer_2 = float(input("Enter the second Integer: "))
# if integer_1 * integer_2 ==1:
#     print("The user defined Integers are the MULTIPLICATIVE INVERSE of each other.")
# else:
#     print("The user defined Integers are not the MULTIPLICATIVE INVERSE of each other.")


# <--------------- OUTPUT --------------->  

# Enter the first Integer: 7
# Enter the second Integer: 0.14
# The user defined Integers are not the MULTIPLICATIVE INVERSE of each other.


# ......................................................................................................

# Q - 09
# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
#     All triangles have three sides
#     An equilateral triangle is a triangle in which all three sides are equal
#     A scalene triangle is a triangle that has three unequal sides
#     An isosceles triangle is a triangle with (at least) two equal sides
# Solution:-

# print("In order to check the TRIANGLE")
# print("Enter the Lengths of the sides of the Triangle")
# side_1= (input("Enter the length of side 1 = "))
# side_2= (input("Enter the length of side 2 = "))
# side_3= (input("Enter the length of side 3 = "))

# if side_1==side_2==side_3:
#     print("According to the lengths the given triangle is EQUILATERAL TRIANGLE")
# elif side_1==side_2 or side_2==side_3 or side_3==side_1:
#         print("According to the lengths the given triangle is ISOSCELES TRIANGLE")
# else:
#         print("According to the lengths the given triangle is SCALENE TRIANGLE")


# <--------------- OUTPUT --------------->  


# In order to check the TRIANGLE
# Enter the Lengths of the sides of the Triangle
# Enter the length of side 1 = 5
# Enter the length of side 2 = 8
# Enter the length of side 3 = 7
# According to the lengths the given triangle is SCALENE TRIANGLE

# In order to check the TRIANGLE
# Enter the Lengths of the sides of the Triangle
# Enter the length of side 1 = 6
# Enter the length of side 2 = 6
# Enter the length of side 3 = 7
# According to the lengths the given triangle is ISOSCELES TRIANGLE

# In order to check the TRIANGLE
# Enter the Lengths of the sides of the Triangle
# Enter the length of side 1 = 5
# Enter the length of side 2 = 5
# Enter the length of side 3 = 5
# According to the lengths the given triangle is EQUILATERAL TRIANGLE

# ..............................................................................................

# Q - 10
# Write a Python program to print user defined multiplication table and also reverse the table.
# Solution:-


# user_define = int(input("Enter any Number : "))
# for i in range(1,11):
#     print(f"{user_define} * {i} = {user_define * i}")
#     # For reverse order
# print("Now the REVERSE_TABLE is as follows:-")
# for i in range(10,0,-1):
#     print(f"{user_define} * {i} = {user_define * i}")

# <--------------- OUTPUT --------------->  

#     Enter any Number : 5
# 5 * 1 = 5 
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50
# Now the REVERSE_TABLE is as follows:-
# 5 * 10 = 50
# 5 * 9 = 45
# 5 * 8 = 40
# 5 * 7 = 35
# 5 * 6 = 30
# 5 * 5 = 25
# 5 * 4 = 20
# 5 * 3 = 15
# 5 * 2 = 10
# 5 * 1 = 5

# ...................................................................................................
