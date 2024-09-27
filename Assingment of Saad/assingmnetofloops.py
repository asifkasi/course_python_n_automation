# Q1. Print numbers from 1 to 10 using a for loop
# for i in range(1,11):
#     print(i)

    # Q2 Print even numbers from 1 to 20 using a for loop.
# for i in range(2,21,2):
#     print(i)
# Q3.print odd numbers from 1 to 20 using a loop.
# for i in range(1,20,2):
#     print(i)

# 7. Print the multiplication table of 5 using a for loop
# null=0
# for i in range(5,51,5):
#     null=null+1
#     print("5 x",null,"=",i)
# for i in range(1,11,1):
#     print("5x",i,"=",i*5)
# a=int(input("enter your number:"))
# for i in range(1,a+1,1):
#      if a % i == 0:
#       print(i)
#  Q:write a python program that reads five numbers and sums all odd values between them.
# a=int(input("enter your number:"))
# sum=10
# for i in range(1,a+1,1):
#     b=int(input("number of loops"))
#     if b % 2 !=0:
#         sum=sum+b
# print("final ",sum)
# sum=0
# for i in range(0,5,1):
#     a=int(input("enter no:"))
#     if a % 2!=0:
#         sum=sum+a
# print("stored the added value",sum)

# a=int(input("enter your num:"))
# for i in range(1,100,1):
#     if i % a == 3:
#        print(i)


# a=int(input("enter the number"))
# factorial=1
# for i in range(a0,-1):
#     factorial=factorial*i
# print("final result",factorial)
    
# Q1: print numbers from 1 to 10 using for loop

# for i in range(1,11,1):
#     print(i,end="")

# print even numbers from 1 to 20 using a for loop:
# for i in range(2,21,2):
#     print(i,end=",")

# # Print odd numbers from 1 to 20 using a loop.
# for i in range(1,21,2):
#     print(i,end=",")

# # 7. Print the multiplication table of 5 using a for loop.
# null=0
# for i in range(1,11,1):
    
#     print("2 x",i,"=",i*5)
# null=0
# for i in range(5,51,5):
#     null=null+1
#     print("5x",null,"=",i)

# 11. Print each character of a string using a loop.

# a="saad bashir"
# b=len(a)
# for i in range(b):
#     print(a[i])

# str="string"
# for i in range(len(str)):
#     print(str[i],end=",")

# 13. Count the number of vowels in a string using a for loop.
# var='asif kasi'
# var2="aeiou"
# sum=0
# for i in range(len(var)):
#     if var in var2:
#         sum=sum+var
#         print("vowels",sum)

# var = 'asif kasi'
# vowels = "aeiou"
# vowel_count = 0

# for char in var:
#     if char in vowels:
#         vowel_count += 1

# print("Number of vowels:", vowel_count)

# a="asif kasi"
# for i in range(0,-len(a)-1,-1):
#     print(a[i])
# a = "asif kasi"
# for i in range(-1, -len(a)-1, -1):
#     print(a[i])

# Question 1: Reverse a String Using a For Loop
# str="python"
# for i in range(-1,-len(str)-1,-1):
#     print(str[i],end=",")

# 21. Print each element of a list using a for loop.
# s= ['A','s','i','f',' ','K','a','s','i']
# len=len(s)
# for i in range(0,len,1):
#     print(s[i])

# 24. Sum all integer elements of a list using a  loop.
# s= [1,3,5,2,4,0]
# sum=0
# a=len(s)
# for i in range(0,a,1):
#     sum=sum+i
# print("final output",sum)


# 25. Find the maximum element in a list using a for loop.
# Output: 5
# Varstr= [1,3,5,2,4,0]
# star=len(Varstr)
# for i in range(0,star,1):
#  if max in Varstr:
#     print(Varstr[i])


# 0.0.1 Write a Python program to print a number, its square and cube, starting with 1 and printing n lines. Accept the number of lines (n, integer) from the user.
# a=int(input("enter your number:"))
# for i in range(1,a+1,1):
#     print(i,i**2,i**3)
# 0.0.3 Write a Python program that finds all the divisors of an integer.
# Test Data:
# Input an integer: 45
# Expected Output:
# All the divisor of 45 are:
# 1
# 3
# 5
# 9
# 15
# 45
# a=int(input("enter your number:"))
# for i in range(1,a+1,1):
#     if a %i==0:
#         print("the number",i)
# sum=0
# for i in range(1,6,1):
#     i=int(input("enter the number:"))
#     if i%2!=0:
#         sum=sum+i
# print("the final output",sum)

# 0.5 Write a Python program to find and print the square of all the even values from 1 to a specified value.
# Test Data :
# List of square of each one of the even values from 1 to a 4 :
# Expected Output:
# 2^2 = 4
# 4^2 = 16
# a=int(input("enter your number:"))
# for i in range(1,a+1,1):
#     if i %  2==0:
#         print("the square ans",i**2)

# 0.6 Write a Python program to print all numbers between 1 and 100 which are divided by a specified number and the remainder will be 3.
# Test Data :
# Input an integer: 25
# Expected Output:
# 3
# 28
# 53
# 78
# a=int(input("what is the number:"))

# for i in range(1,101,1):
#     if i %a ==3:print("the final result",i)
# 2. Write a program to find the sum of the digits of a given number.

# a=(input("what is the number:"))
# sum=0
# for i in range(0,len(a),1):
#     sum=sum+int(a[i])
# print("the final result",sum)

# 5. Write a program to display the cube of the number up to an integer.
# Input the number of terms : 5
# Sample Output:
# Number is : 1 and the cube of 1 is: 1
# Number is : 2 and the cube of 2 is: 8
# Number is : 3 and the cube of 3 is: 27
# Number is : 4 and the cube of 4 is: 64
# Number is : 5 and the cube of 5 is: 125

# a= input ("enter a number")
# for i in range(1,int(a)+1,1):
#     print(i,i**3)

# 6. Write a program that display the sum of n odd natural numbers.

# var = int(input("entre a number"))
# sum=0
# for i in range (1,var*2,2):
#     print(i,end="!")
#     sum= sum+i
# print("sum of odds",sum) 



# 2. Write a program to display n terms of natural numbers and their sum.
# Test input : 7
# Expected Output :
# The first 7 natural number is :
# 1 2 3 4 5 6 7
# The Sum of Natural Number upto 7 terms : 28

# var=int(input("enter your number"))
# sum=0
# for i in range(1,var+1,1):
#     print(i,end=",")
#     sum=sum+i
# print("final output",sum)

# 5. Write a program to display the multiplication table for a given integer.

# var=int(input("enter the number"))
# for i in range(1,var+1,1):
#     print("5x",i,"=",i*5)

# .0.1 Write a Python program to print a number, its square and cube, starting with 1 and printing n lines. Accept the number of lines (n, integer) from the user.
# Test Data :
# Input number of lines: 5
# Expected Output:
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125


# var=int(input("enter the number:"))
# for i in range(1,var+1,1):
#     print("value",i,"square",i**2,"cube",i**3)


# 9. Write a program to display the sum of n terms of even natural numbers.
# Test Data :
# Input number of terms : 5
# Expected Output :
# The even numbers are :2 4 6 8 10
# The Sum of even Natural Number upto 5 terms : 30
# sum=0
# input=int(input("enter the number"))
# for i in range(2,(input*2)+1,2):
#     print(i)
#     sum=sum+i
# print("final value",sum)


# 12. Write a program that displays the n terms of square natural numbers and their sum.
# 1 4 9 16 ... n Terms
# Test Data :5
# Expected Output :
# The square natural upto 5 terms are :1 4 9 16 25
# The Sum of Square Natural Number upto 5 terms = 55

# sum=0
# var=int(input("enter the number:"))
# for i in range(1,var+1,1):
#     print("the square of upto",var,"terms are",i**2,end="|")
#     sum=sum+i
# print("final value",sum)


# 17. Write a program to display the number in reverse order.
# Test Data :
# Input a number: 12345
# Expected Output :
# The number in reverse order is : 54321

# var=input("enter the num:")
# for i in range(len(var)-1,-1,-1):
#     print(var[i],end="")

# 19. Write a program to find the number and sum of all integers between 100 and 200 which are divisible by 9.
# Expected Output :
# Numbers between 100 and 200, divisible by 9 :
# 108 117 126 135 144 153 162 171 180 189 198
# The sum : 1683

# sum=0
# for i in range(100,201):
#     if i % 9==0:
#      print(i,end=",")
#     sum=sum+i
# print("final",sum)


# for i in range(1,10,1):
#     print("loop ended")     
# a=input("enter the num :")
# for i in range(1,len(a),1):
#     for j in range(1,i,1):
#         print("*",end=" ")
#     print()

import csv
with open("sample2.csv",mode="r")as f:
    reader=csv.reader(f)
    for row in f:
        print(row)