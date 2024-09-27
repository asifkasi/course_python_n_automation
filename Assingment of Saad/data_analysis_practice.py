# a=eval(input("enter the number:"))
# print(a)
# print(bin(1981))
# a=int(input("enter the number"))
# if a %2!=0:
#     print("NUM IS odd",a)
# else:
#     print("even")


# while True:
#     a=int(input("enter the number here :"))
#     b=int(input("enter the 2nd number here :"))
#     print(a+b,a-b,a*b,a%b)

#     repeat=input("do you want to stop the program:")
#     if repeat == "yes":
#         break

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end='')
#     print()

# for i in range(1,11):
#     if i == 4:
#         break
#     else:
#         print(i)
#     print()
# sum=0
# for i in range(0,51,2):
#     sum=sum+i
# print(sum)
# # sum=0
# for i in range(1,51):
#     if i %2==0:
#         sum=sum+i
# print(sum)

# for i in range(1,21):
#     print(i,i**2)

# super market billing system
# while True:
#     print("welcome to A-Z super market:")
#     name=input("enter the name of customer:")
#     total=0
#     while True:
#         print("enter the amount and quantity:")
#         amount=float(input("enter the amount:"))
#         quantity=float(input("enter the quantity:"))
#         total+= amount*quantity
#         repeat=input("do you want to add more items?(yes/no)")
#         if repeat == "no" or repeat == "No":
#             break
#     print("-"*50)
#     print("Name",name)
#     print("Amount to be paid",total)
#     print("-"*50)
#     repeat1=input("do you want to deal the other customer:")
#     if repeat1 == "no" or repeat1 == "No":
#         print("Shop Is Closed:")
#         break
#     # print("Shop Is Closed:")


# some practice questions of strings
# write a program to caluclte the length of a this string
# A="why fit in, when you are born to stand out:"
# print(len(A))

# Write a program to check how many times alphabet o is occuring
# A="why fit in, when you are born to stand out:"
# print("the number of times O is occuring",A.count("o"))


# # convert the whole string into upper and lower case:
# a="why fit in, when you are born to stand out:"
# print(a.lower())
# print(a.upper())
# print(a.title())
# print(a.find("why"))


# printing patterns

# for i in range(1,6,1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print() 

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(6,0,-1):
    for k in range(1,i-1):
        print("*",end=" ")
    print()




# for i in range(1,6,1):
#     for j in range(1,i+1):
#         print(i*j,end=" ")
#     print()


# def main():
#     x=int(input("what is your x value?"))
#     print("x squared is ",square(x))
#     def square (x):
#      return x*x
#     main(3)

# def main():
#     x = int(input("What is your x value? "))
#     print("x squared is", square(x))

# def square(x):
#     return x * x

# main()
