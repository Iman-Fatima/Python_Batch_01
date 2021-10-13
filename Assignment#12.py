# Problem Statement #01:
#    1- Create a program to print any user defined multiplication table
#    2- Print the same above table in reverse order

user_define = int(input("Enter any Number : "))
for i in range(1,11):
    print(f"{user_define} * {i} = {user_define * i}")

# <--------------- OUTPUT --------------->  

# Enter a number : 15
# 15 * 1 = 15
# 15 * 2 = 30
# 15 * 3 = 45
# 15 * 4 = 60
# 15 * 5 = 75
# 15 * 6 = 90
# 15 * 7 = 105
# 15 * 8 = 120
# 15 * 9 = 135
# 15 * 10 = 150

# .......................................................................................................


# Problrem Statement #02:
#   Print the same above table in reverse order


user_define = int(input("Enter any Number : "))
for i in range(10,0,-1):
    print(f"{user_define} * {i} = {user_define * i}")

# <--------------- OUTPUT --------------->  
 
# Enter any Number : 15
# 15 * 10 = 150
# 15 * 9 = 135
# 15 * 8 = 120
# 15 * 7 = 105
# 15 * 6 = 90
# 15 * 5 = 75
# 15 * 4 = 60
# 15 * 3 = 45
# 15 * 2 = 30
# 15 * 1 = 15
