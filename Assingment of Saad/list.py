# list=["saad",101,26,"bashir ahmed"]
# print("before",list)
# list.append(5.9)
# print("after the update ",list)

# imran ki name age class address add karo roll number or usky subjects
# list=["imran",12,7,"keamari"]
# print("before the update ",list)
# list.extend([102,"computer","maths","physics"])
# print("after the update",list)

#  umar ki name age class add address , roll number or uski cricket or subjects
# list_umar=["muhammad umar", 17,11,"keamari"]

# print("before the update",list_umar)

# list_umar.extend([103,"crickter","maths","english","urdu"])

# print("after the update",list_umar)

# print(list_umar[1:4])
#  
# this time the list will be modified by me
# list=["saad",24,5.7,"keamari"]

# print("before the update",list)

# a=list.index("keamari")

# list[a]="islamabad"

# print(list)

# this time it will be modified for imran as well
# var_list=["imran",13,4.4,6]

# print("before the update",var_list)

# a=var_list.index(4.4)

# b=var_list.index(6)

# var_list[a]=4.6

# var_list[b]=7

# print(var_list)

# this time it is created for abu g

# list_bashir=["bashir ahmed",50,"gov servant",58000]
# print("before the update",list_bashir)
# a =list_bashir.index(50)
# b =list_bashir.index("gov servant")
# c =list_bashir.index(58000)
# list_bashir[a]=int(input("what is your age now"))
# list_bashir[b]=input("enter your occupation")
# list_bashir[c]=int(input("enter the your bank balance"))
# print(list_bashir)

# this time it is inserting the values with finding its index first
# list=["saad","imran","umar","haris","noman"]
# print("before the update",list)
# a=list.index("saad")
# list.insert(a,"bashir ahmed")
# print(list)
# list_A=["a","b","c"]
# list_B=[1,2,3]
# var=(list_A+list_B)
# print(var)

# list=["apple","banana","cherry","date","pineapple"]
# list.remove("cherry")
# print(list)
# list=["car","truck","bike","revo","vigo"]

# print("before the update ",list)

# a=list.index("bike")

# list[a]="scooter"
# print("after the update",list)

# list=[1,4,5,6,7,3,6,2,5,6,74,3,3434,6,743,5,33,53,34,6765,]
# list.sort()
# print(list)

# insert program
# list=["car","truck","bus","bike","bicycle"]
# a=list.index("bus")
# list.insert(a,"imran")
# print(list)

# list=["saad",24,5.6,"massan"]
# a=list.index("saad")
# list[a]="imran"
# print(list)

# list=[3,4,5,6,2,2,6,7,8,3,34,56,733,6,56,78,33,36,6,732,25,]

# print("before the update",list)

# list.sort()

# max_num=max(list)
# print("this is the maximum number",max_num)
# min_num=min(list)
# print("this is the minimum number",min_num)
# print(list)
# 10 list of 10 natural numbers

# list=[1,2,3,4,5,6,7,8,9,10]

# print(list)
# list2=["pakistan","india","afghanistan","china","iran"]
# print(list2)
# list3=[10,20,30,40,50]
# print(list3[2])

# var=int(input("enter the number"))
# for i in range(1,var*2,2):
    
var=input("enter the num:")
for i in range(len(var)-1,-1,-1):
    print(var[i],end="")
    