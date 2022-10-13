# #Q-1- Even and Odd
# n=int(input("Eneter a number you want to check? "))
# if n%2==0:
#     print("Even")
# else:
#     print("odd")

# w=float(input("Plesse input your Weight"))
# l=float(input("Please input your Lenght"))
# bmi=w/(l*l)
# #print(bmi)
# if bmi<=18.5 :
#     print("Underweight")
# elif bmi>18.5 and bmi<=25.0:
#     print("Normal Weight")
# elif bmi>25.0 and bmi<=30.0:
#     print("Overweight")
# elif bmi>30.0 and bmi<=35.0:
#     print("Obese")
# else:
#     print("Clinically obose")

#q3-Leap year
# year=int(input("Enter the year you want to check"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap")
#         else:
#             print("not leap")
#     else:
#         print("Leap")
# else:
#     print("Not Leap")

# Q-4
# Pizza dilevery
# print("Welcome to Pizza Shop")
# size=input("What is the size of Pizza. S,M,L")
# add_pepperoni= input("Do you want pepperoni. Y,N")
# extra_cheese= input("Do you want extra cheese. Y,N")

# if size=='S':
#     bill=15
#     if add_pepperoni=='Y':
#         bill+=2
#         if extra_cheese=='Y':
#             bill+=1
# elif size=='M':
#     bill=20
#     if add_pepperoni=='Y':
#         bill+=3
#         if extra_cheese=='Y':
#             bill+=1
# elif size=='L':
#     bill=25
#     if add_pepperoni=='Y':
#         bill+=3
#         if extra_cheese=='Y':
#             bill+=1
# print(bill)
    

# Q-5
# LOve Calculator
print("Welcome to Love Calculator")
name1= input("What your name? ")
name2=input("What your lovers name? ")
c=0
d=0
for items in name1:
    if items=='t':
        c+=1
    if items=='r':
        c+=1
    if items=='u':
        c+=1
    if items=='e':
        c+=1
for item in name2:
    if item=='l':
        d+=1
    if item=='o':
        d+=1
    if item=='v':
        d+=1
    if item=='e':
        d+=1
    
love=(10*c)+d
print(love)