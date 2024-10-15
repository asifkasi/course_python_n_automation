# #Q:1 10 list of 10 natural numbers
# list=[1,2,3,4,5,6,7,8,9,10]
# print(list)
# # Q:2
# list2=["pakistan","india","afghanistan","china","iran"]
# print(list2)
# # Q:3
# list3=[10,20,30,40,50]
# print(list3[2])
# Q:4
# list=[1,2,3,4,5]
# print("before the update",list)

# a=list.index(2)
# list[a]=10
# print("after the update",list)
# Q5:
# list=[1,2,3,4,5]
# print("before the append value",list)
# list.append(10)
# print("after the update of append",list)
# Q6:
# list=[1,2,3,4,5]
# print("before the insert",list)
# a=list.index(1)
# list.insert(a,0)
# print("after the insert",list)
# Q7:
# list=[1,2,3]
# list2=[4,5,6]
# list.extend(list2)
# print(list)
# Q8:
# list=[1,2,3,4,5]
# # a=list.index(3)
# list.remove(3)
# print(list)

# # Q9:
# list=[1,2,3,4,5,6,7,8,9]
# print("before the pop",list)
# list.pop()
# print("after the pop",list)

# list=[1,2,3,4,5]
# a=list[0:3]
# print(a)

# list=[1,2,3,4,5]
# print(type(list))
# print(len(list))
# print(list)
# list=[1,2,4,5,6,7,8,4,34,43,43,45,43,342,325,3,26462]
# a=list[1::2]
# print(a)
# list=[1,2,3,4,5]
# print(len(list))
# Q:10 Clear all elements from the list [1, 2, 3, 4, 5].

# list=[1,2,3,4,5]
# list.clear()
# print(list)
# Find the length of the list [1, 2, 3, 4, 5]

# list=[1,2,3,4,5]
# print(len(list))

# #  Find the maximum value in the list [10, 20, 30, 40, 50].
# list=[10,20,30,40,50]
# max_num=max(list)
# print(max_num)

# 20. Sort the list [3, 1, 4, 2, 5] in ascending order.
# list=[3,1,4,2,5]
# list.sort()
# print(list)

# list=[1,2,3,4,5,]
# listeven=[]
# if list[0] %2==0:
#     listeven.append(list[0])
# if list[1]%2==0:
#     listeven.append(list[1])
# if list[2]%2==0:
#     listeven.append(list[2])
# if list[3]%2==0:
#     listeven.append(list[3])
# if list[4]%2==0:
#     listeven.append(list[4])
# print(listeven)

# Create a new list containing the lengths of each string in the list ['apple', 'banana', 'cherry'].

# list=["apple","banana","cheery"]
# var=[len(list[0]),len(list[1]),len(list[2])]
# print(var)
# . Create a new list containing the lengths of each string in the list ['apple', 'banana', 'cherry'].
# list=["apple","banana","cherry"]
# var=len(list[0])
# var2=len(list[1])
# var3=len(list[2])
# newlist=[var,var2,var3]
# print(newlist)

# list=[1,2,3,4,5]
# listnew=[]
# if list[0]%2==0:
#     listnew.append(list[0])
# if list[1]%2==0:
#     listnew.append(list[1])
# if list[2]%2==0:
#     listnew.append(list[2])
# if list[3]%2==0:
#     listnew.append(list[3])
# if list[4]%2==0:
#     listnew.append(list[4])
# print(listnew)
# 29. Create a list of the first letters of each word in the list ['apple', 'banana', 'cherry'] using a list comprehension.


# list=["banana","cherry","apple"]
# var=list[0]
# var2=list[1]
# var3=list[2]
# newlist=[var[0],var2[0],var3[0]]
# print(newlist)


# list=[1,2,3,4,5,7,5,43,5]
# print(list.count(5))


sum=0
var=int(input("enter the number:"))
for i in range(1,var+1,1):
    print("the square of upto",i,"terms are",i**2,end=",")
    sum=sum+i
print("final value",sum)
