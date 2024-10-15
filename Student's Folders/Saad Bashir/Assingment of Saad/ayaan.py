# name=input("what is your name?")
# print("length of your name",len(name))
# name2=input("what is your father's name length")
# print("length of your father's name is",len(name2))
# age=int(input("what is your age?"))
# print(age)
# if(age>=18):
#     print("can drive")
# elif(age<18):
#     print("can't drive")
# age=16
# if(age>=18):
#     print("can vote")
# elif(age<18):
#     print("cant vote")
# light=input("what is the colour?")
# print("the color is",light)
# if(light=="green"):
#     print("you should go")
# elif(light=="red"):
#     print("stop")
# elif(light=="yellow"):
#     print("look")
# var_1="asif kasi"
# if "as" in var_1:
#     print("true")
# else:
#     print("false")
# var_1="asif kasi"
# print(var_1.capitalize())
# str="asif kasi"
# print(str[2:4])
# student=["saad",92,23,"karachi"]
# print(student[0])
# student[0]="muhammad saad"
# print(student)
# print(student[3])
# student[3]="islamabad"
# print(student)
# var_1="muhammad saad"
# print(len(var_1))
# print(var_1)
# print(var_1[2:5])
# print(var_1.endswith("ad"))
# print(var_1.capitalize())
# print(var_1.replace("a","o"))
# print(var_1.find("a"))
# print(var_1.count("a"))
# num=int(input("what is your number?"))
# if(num % 2 == 0):
#     print("even")
# else:
#     print("ODD")
# a=int(input("enter your first number!"))
# b=int(input("enter your second number!"))
# c=int(input("enter your third number!"))
# if(a>=b and a>=c):
#     print("first number is largest",a)
# elif(b>c):
#     print("second number is largest",b)
# else:
#     print("third number is largest",c)
# list=["apple","banana"]
# list.append("mango")
# list.sort(reverse=True)
# print(list)
# tup=(1,2,3,4,5)
# tup[0]=5
# print(tup)
var = input("Input a number: ")
for i in range(len(var) - 1, -1, -1):
    print(var[i], end="")
