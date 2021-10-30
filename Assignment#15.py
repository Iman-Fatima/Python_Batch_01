# Problem Statement

#     Suppose that you are a teacher and you want to find average obtained marks of a student. 
#     Create a Python program to perform the following tasks:
#         Ask user if he/she has entered marks against desired number of subjects and wants to 
#         calculate average so far or wants to enter marks for more subjects
#         Print Number of subjects against marks were added
#         Print Average of all obtained marks


flag = True
count = 1
t_m = 0
while flag:
    marks = int(input(f"Enter Marks for subject {count} : "))
    print(f"Your marks for subject {count} are : {marks} ")
    t_m +=  marks
    choice = input('Press N to exit or any other to continue :')
    if choice == 'N' or choice == 'n':
        flag = False
    count += 1
count -= 1
average= t_m/ count
print (f"Number of subjects are {count}")
print(f"The average of the given marks is: {average}")

# <--------------- OUTPUT --------------->  


# Enter Marks for subject 1 : 99
# Your marks for subject 1 are : 99         
# Press N to exit or any other to continue :
# Enter Marks for subject 2 : 88
# Your marks for subject 2 are : 88         
# Press N to exit or any other to continue :
# Enter Marks for subject 3 : 77
# Your marks for subject 3 are : 77 
# Press N to exit or any other to continue :
# Enter Marks for subject 4 : 78
# Your marks for subject 4 are : 78 
# Press N to exit or any other to continue :
# Enter Marks for subject 5 : 89
# Your marks for subject 5 are : 89 
# Press N to exit or any other to continue :
# Enter Marks for subject 6 : 98
# Your marks for subject 6 are : 98 
# Press N to exit or any other to continue :87
# Enter Marks for subject 7 : 97
# Your marks for subject 7 are : 97 
# Press N to exit or any other to continue :85
# Enter Marks for subject 8 : 95
# Your marks for subject 8 are : 95 
# Press N to exit or any other to continue :n
# Number of subjects are 8
# The average of the given marks is: 90.125