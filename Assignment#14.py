# Problem Statement 1:
#     Create python programs to print the given patterns with *
#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * *



for i in range(5):
    for j in range(-6, -i):
        print(" ", end="")
    for k in range(i+1):
        print("* ", end="")
    print()


# <--------------- OUTPUT --------------->  

#       * 
#      * * 
#     * * *
#    * * * *
#   * * * * *
