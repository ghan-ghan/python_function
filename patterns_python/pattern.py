





'''#Displaying the different pattern using the while loop in python ....

    # 1.Output is given as :
    # 1
    # 12
    # 123
    # 1234
    # 12345  '''

num=int(input("Enter how many times you want to print:: "))
for i in range(num):
    for j in range (1,i+2):
        print(j, end="")
    print()


    '''# # 2.For the output given as below ,what may be the code:

    # 1
    # 22
    # 333
    # 4444
    # 55555 '''

for i in range (6):
    for j in range (i):
        print(i, end="")
    print()



    '''' # 3.write down the program to print the output as :
    # 55555
    # 4444
    # 333
    # 22
    # 1'''

for i in range (5):
    for j in range(5-i):
        print( 5-i, end ="")
    print()





    '''# for the given output what is the program:
    # 1
    # 23
    # 456
    # 78910'''

num=1
for i in range(5):
    for j in range (i):
        print(num, end="")
        num+=1
    print()
    


# output as :

    # *
    # **
    # ***
    # ****
    # # *****

num=int(input("Enter the number : "))
for i in range(num):
    for j in range(i+1):
        print("*",end="")
    print()

# 2.output is :

   # ****
   # ***
   # **
   # *

for i in range(num):
    for j in range(i,num):
        print("*",end="")
    print()


