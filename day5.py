# #Average of height of student
# student_height=int(input("Enter number of student in the class"))
# student=[]
# sum=0
# for i in range(0,student_height):
#     input1=input("Enter the height of student" )
#     student.append(input1)
# for i in range(0,student_height):
#     student[i]=int(student[i])
# for i in range(0,student_height):
#     sum=sum+student[i]
# av=sum/student_height
# avh=round(av)
# print(avh)
# ##

# ##Highest number
# # student_score=int(input("Enter number of student in the class"))
# # student=[]
# # sum=0
# # for i in range(0,student_score):
# #     input1=input("Enter the score of student" )
# #     student.append(input1)
# # for i in range(0,student_score):
# #     student[i]=int(student[i])
# # h=student[0]
# # for i in range (1,student_score):
# #     if h<student[i]:
# #         h=student[i]
# # print(h)
# # print(max(student))


# #addind all the Even number
# # sum1=0
# # for i in range(1,101):
# #     if i%2==0:
# #         sum1+=i
# # print(sum1)
# # print(1%2)
# # print(2%2)

# #FizzBuzz
# for i in range(1,101):
#     if i%3==0:
#         if i%15==0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif i%5==0:
#         if i%15==0:
#             print("FizzBuzz")
#         else:
#             print("Buzz")
#     else:
#         print(i)
    
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
# list1=[letters,numbers,symbols]
# print(list1)
print("Welcome to PyPassword Denerator!")
n1=int(input("How many letters you want"))
n2=int(input("How many numbers you want"))
n3=int(input("How many symbols you want"))
password1=[]
for char in range(1,n1+1):
    password1.append(random.choice(letters))
for char in range(1,n2+1):
    password1.append(random.choice(numbers))
for char in range(1,n3+1):
    password1.append(random.choice(symbols))
print(password1)
random.shuffle(password1)
password=''
for char in password1:
    password+=char
print(password)

