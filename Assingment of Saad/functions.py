# # def cal_val(a,b):
# #     sum=a + b
# #     print(sum)
# #     return sum

# # cal_val(2,10)
# # cal_val(5,32)
# # cal_val(12,34)

# # def sub_val(a,b):
# #     subtract= a - b
# #     print(subtract)
# #     return subtract
# # sub_val(10,2)
# # sub_val(20,10)
# # sub_val(40,23)

# def mul_val(a,b):
#     mul=a * b
#     print(mul)
#     return mul
# mul_val(10,2)
# mul_val(29,2)
# mul_val(23,30)

# def div_val(a,b):
#     div=a/b
#     print(div)
#     return div
# div_val(10,2)
# div_val(20,10)
# div_val(40,4)

# def mod_val(a,b):
#     mod=a%b
#     print(mod)
#     return mod
# mod_val(20,2)
# mod_val(30,3)
# mod_val(40,5)
# mod_val(30,4)

# def avg(a,b,c):
#     avg=((a+b+c)/3)
#     print(avg)
#     return avg
# avg(10,20,30)
# avg(20,5,12)
# avg(10,20,12)

# cities=["karachi","islamabad","peshawar","quetta"]
# def cal_len(list):
#     print(len(list))
    
# cal_len(cities)

# students=["saad",'sana','sadaf','yousaf','hamza']
# def cal(list):
#     print((list))
# cal(students)
    


# studnets=["saad",'sana','sadaf','yousaf','hamza']
# def calc_std(list):
   
#     for item in list:
#         print(item,end=" ")
# calc_std(studnets)

# def converter(USD_val):
    
#     pkr=USD_val*280
#     print(USD_val,"USD=",pkr,"PKR")
# converter(100)
    
# def cal_fac(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# cal_fac(7)

# list_1=[1,2,4,5,6,7,43,2,1,23,45,67,843,2]
# def count(list):
#     print(len(list))

# count(list_1)

# list_1=[1,2,4,5,6,7,43,2,1,23,45,67,843,2]
# def loop(list):
#     for item in list:
#         print(item,end=" ")
# loop(list_1)

# def calc_fac(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
# calc_fac(87)

# def converter(dollar):
#     pkr=dollar*280
#     print(dollar,"usd = ",pkr,"pkr")
# converter(234)

# def calc(a,b):
#     mul=a*b
#     print(mul)

# def isgreater(a,b):
#     if a>b:
#         print("A is greater ",a)
#     else:
#         print("b is greater",b)
# d=12
# c=44
# calc(c,d)
# isgreater(c,d)

# def findsqr():
#     a=int(input("enter the number to be squared"))
#     print("your final output",square(a))
# def square(a):
#     return a*a
# findsqr()

# def greet():
#     a=input("what is your name?:")
#     print("hello!",a)
# greet()

# # Question: Write a function add_numbers that takes two parameters and returns their sum

# def add_numbers(a,b):
#     a=int(input("write your first num:"))
#     b=int(input("write your 2nd num:"))
#     x=a+b
#     print("final result after the sum",x)


# a=10
# b=20
# add_numbers(a,b)


# def calculateGmean(a,b):
#     # a=int(input("enter the number:"))
#     # b=int(input("enter the number:"))
#     mean=(a*b)/(a+b)
#     print(mean)
#     return mean

# def isgreater(a,b):
#     if a>b:
#         print("a is greater then b:")
#     else:
#         print("b is greater:")
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))

# calculateGmean(a,b)
# c=10
# d=20
# isgreater(c,d)

# functions with multiple strings
# def name(name,fname,mname="sumaiya"):
#     print(name,fname,mname)
# name("saad","bashir")


# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum= sum+i
#         print("average is ",sum/len(numbers))
# average(9,6,7,8)        


# def f1():
#     print("helllo world!")
# f1()
# def f2(name):
#     print(name)
# f2("saad")

# ADD TWO NUMBERS
# def add_numbers(n1,n2):
#     result=n1+n2
#     print("The Sum Is",result)
# number1=123
# number2=343
# add_numbers(number1,number2)

# def find_marks():

#     marks=[55,64,75,80,65]

#     marks_sum=sum(marks)

#     print(marks_sum)

#     marks_len=len(marks)

#     print(marks_len)

#     average=marks_sum/marks_len
#     print(average)

#     if average>80:
#         print("result is A",average)
#     else:
#         print("result is B")

# find_marks(23,55,66,77,88)


# def find_avg_marks(marks):
#     sum_of=sum(marks)
#     total=len(marks)
#     result=sum_of/total
#     return result
# marks=[23,66,77,88,99]
# final_output=find_avg_marks(marks)
# print("the final output",final_output)

# def find_average_marks(marks):
#     sum_of_marks=sum(marks)
#     total_subjects=len(marks)
#     average_marks=sum_of_marks/ total_subjects
#     return average_marks

# marks=[55,44,33,22,11]
# average_marks=find_average_marks(marks)
# print("your final output",average_marks)

# def find_avg_marks(marks):
#     sum_of=sum(marks)
#     total=len(marks)
#     result=sum_of/total
#     return result
# marks=[23,66,77,88,99]
# final_output=find_avg_marks(marks)
# print("the final output",final_output)

# def compare(final_output):
#     if final_output > 90:
#         print("A")
#     elif final_output<=90:
#         print("B")
# compare(final_output)


# can you create a program to add and multiply two numbers? for this , create two functions add-numbers() and multiply_numbers(). These functions should compute the results and return them to the functions call.and result should be printed form outside the function:
# def add_numbers(a,b):
#     sum=a+b
#     print("the final result",sum)
#     return


# def mul(a,b):
#     mul=a*b
#     print("multiplication is",mul)
#     return
# add_numbers(12,12)
# mul(23,3)


# def add_num(n1,n2):
#     sum=n1+n2
#     return sum
# result=add_num(23,23)
# print(result)


# def add_numbers(a,b):
#     sum=a+b
#     return sum
# def multiply_numbers(a,b):
#     multiply=a*b
#     return multiply
# result_of_sum=add_numbers(22,33)
# print("the final result is ",result_of_sum)

# result_of_mul=multiply_numbers(2,3)
# print("multiplication is ",result_of_mul)


# **Sum of List Elements**: Write a function `sum_list(lst)` that takes a list of numbers and returns the sum of all elements in the list.
# def sum_list(lst):
#     add=sum(lst)
#     return add

# my_list=[1,2,3,4,5]
# result=sum_list(my_list)
# print(result)


#                             *************************************/**
# 2. **Find Maximum Value**: Write a function `find_max(lst)` that takes a list of numbers and returns the maximum value.

# def find_max(lst):
#     find=max(lst)
#     return find

# my_list=[12,33,44,12,3,4,5,65]
# result=find_max(my_list)
# print(result)
#                           **************************************************
# 5. **Factorial Calculation**: Write a function `factorial(n)` that returns the factorial of a given number `n`.
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i 
#         print(fact)
#     print()
    
# fact(9)
#                8***********************************************************888

# 
# 6. **Reverse a String**: Write a function `reverse_string(s)` that takes a string `s` and returns it reversed.
# def reverse():
#     a="umar bashir"
#     a=a[::-1]
#     print(a)
# # a="bashir ahmed"
# # result=reverse(a)
# # print(result)
# reverse()
# 




#     **************************************************************************************

# . **Square of a Number**: Write a function `square(n)` that takes a number `n` and returns its square.

# def square(n):
#     a=("square of number:",n*n)
#     return a
# b=square(9)
# print(b)


# def abc():
#     x=int(input("enter the number"))
#     print(square(x))
# def square():
#     return

# def square(n):
#     return n*n
# def abc():
#     x=int(input("enter the num:"))
#     print(square(x))
    

# abc()


                #   **********************************************
# 4. **Convert to Uppercase**: Write a function `to_uppercase(s)` that converts a string `s` to uppercase.
# a="saad bashir"
# b=a.upper()
# print(b)


# def Upper_Case():
#     a=input("enter the numbe to be uppercased:")
#     b=a.upper()
#     return b
# print(Upper_Case())

#                   \**************************************\
# 5. **Check Even or Odd**: Write a function `is_even(n)` that returns `True` if `n` is even, and `False` otherwise.

# def is_even(n):
#     if n %2==0:
#         print("the number is even",n)
#     else:
#         print("the number is odd:")
#     print(n)
# is_even(9)


# /////////////////************************************************************************//////////
# def is_concat(s1,s2):
#     is_sum=s1+s2
#     return is_sum
# a=is_concat("saad","umar")
# print(a)

# //////////////*****************************////////////////

# 7. **Print a Message**: Write a function `print_message(msg)` that prints a given message `msg`.
# def print_message(msg):
#     print(msg,"saad")
#     return msg
# print_message("hello brother:")


#              ***********************************************************
# 8. **Convert Celsius to Fahrenheit**: Write a function `celsius_to_fahrenheit(c)` that converts a temperature from Celsius to Fahrenheit.

# def convereter(c):
#     f =(c * 9/5) + 32 

#     print(f)
# convereter(8)
# 9. **Find Length of String**: Write a function `string_length(s)` that returns the length of a given string `s`.
# def string_length(s):
#     a=len(s)
#     return a
# final_output=string_length("saad bashir ahmed")
# print(final_output)



# ***************************************************************************************************8
# 10. **Subtract Two Numbers**: Write a function `subtract_numbers(a, b)` that takes two numbers and returns the result of subtracting `b` from `a`.


# def subtract_numbers(a,b):

#     subt=a-b

#     return subt
# c=20

# d=90

# final_result=subtract_numbers(c,d)

# print(final_result)


# *************************************************************************************
# 1. **Sum of List Elements**: Write a function `sum_list(lst)` that takes a list of numbers and returns the sum of all elements in the list.
# def sum_list(lst):
#     a=sum(lst)
#     return a
# list1=[2,3,4,5,6,7,8]
# final=sum_list(list1)
# print(final)

# ******************************************************
# 2. **Find Maximum Value**: Write a function `find_max(lst)` that takes a list of numbers and returns the maximum value.
# def find_max(lst):
#     calc=max(lst)
#     return calc
# list1=[1,3,4,5,6,55]
# final=find_max(list1)
# print(final)



def count_vowels(s):

    vowels="aeiouAEIOU"

    count=0

    for char in s:

        if char in vowels:

            count=count+1

    return count

a=count_vowels("hello world!")
print(a)

