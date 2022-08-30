


'''calculation of the percentage  amount on user specify percentage of 
using function in python..'''

def percentage(amount,percent):
    percentage_amount= (amount * percent)/100
    return percentage_amount

amount=int(input("enter the amount in Rs : "))
percent=int(input("enter the percentage : "))

print(percentage(amount,percent))



#calculate the sum of two numbers using function:
def sum(a,b):
    return a+b

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number: "))

add = sum(num1,num2)
print(add)



'''write a python function to find the Max of three numbers'''
def max(a,b,c):
    if a > b  and a > c : 
        return a 

    elif b > a  and b > c:
            return b

    elif a == b == c :
        print("Numbers are Equal ")

    else :
        return c

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number : "))

print(max(num1,num2,num3))



'''2. Write a Python function to sum all the numbers in a list'''
def sum_of_list(list):
    total =0
    for i in list :
        total +=i
    return total

print(sum_of_list(([1,2,3,4])))



'''Write a Python function to multiply all the numbers in a list'''
def multiples_of_num(number):
    total =1
    for i in number:
        total *=i 
    return total 

print(multiples_of_num((8,2,3,-1,7)))




'''. Write a Python program to reverse a string.'''

def reverse(string1):
    string = ''
    count = len(string1)
    while count > 0 :
        string += string1[count-1]
        count = count -1
    return string

print(reverse('1234abcd'))





'''Write a Python function to check whether a number falls in a given range'''

def check_range(n):
    if n in range(3,9):
        print( " inside the range ")

    else :
        print("The number is outside the given range.")

check_range(5)



'''Write a Python function that takes a number as a parameter and check the number is prime or not'''

def prime_num(n):
    if n ==1:
        return False
    elif n==2 :
        return True
    else:
        for i in range (2,n):
            if n%i ==0:
                return False
        return True

print(prime_num(9))


'''check  the even numbers or not even '''

def even_numbers(num):
    if num %2 ==0 :
        return True
    return False
print(even_numbers(7))



# def even_list(num):
#     nums=[]
#     for i in num:
#         if i % 2 ==0:
#             nums.append(i)
#     return nums

# print(even_list([1,2,3,4,5,6]))




'''finding the square of the every elements in list between 1 to 20'''

def square_list():
    list =[]
    for i in range(1,21) :
        list.append(i**2)
    return list


print(square_list())

