# Q2:
# var_1="asif kasi"
# if "as" in var_1:
#     print("true")
# else:
#     print("false")
# Q3
# str="hello world"
# var = str[:-1]
# print(var)
# str="hello.world"
# indexworld=str.find("world")
# indexdot=str.find(".")

# str="hello"
# print(str.capitalize())

# str="asif kasi"

# var = str.find("a")
# var2 = str.find("i")

# str = str[var2]+str[var+1:]+str[var]

# print(str)

# str="asif kasi"
# print(str.replace("a","i"))

# var="asif kasi"
# var1=var[0]
# var2=var[-1]
# output=var2+var[1:-1]+var1
# print(output)

# num=int(input("enter your number"))
# if num>=1 and num <=10:
#     print("number is in range")
# else:
#     print("number is out of range")

# num=int(input("enter any number"))
# if num<=10:
#     if num>=1:
#         print("number is okay")
#     else:
#         print("number is not okay")
# else:
#     print("not okay")

# num=int(input("enter your number "))
# if num %2==0:
#     print("the number is even")
# else:
#     print("the is odd")
# num=int(input("enter your number"))
# if num %7==0:
#     print("the number is divisible")
# else:
#     print("not divisible")
# num=int(input("enter your number "))
# if num==0:
#     print("the number is neutral")
# elif num%2==0:
#      print("number is even")
      
# else:
#     print("the is odd")
# num=int(input("enter your number"))
# if num==0:
#     print("number is divisble")
# elif num%5==0 or num%7==0:
#     print("the number is divisible")
# else:
#     print("not divisvle")
num=int(input("enter your number"))
if num==0:
    print("num is neutral")
elif num%5==0 and num %7==0:
    print("num is divisible by both")
elif num%5==0:
    print("num is divisible by 5")
elif num%7==0:
    print("num is divisble by 7")

else:
    print("num is not divisible")