import random
## n= random.randint(1,10)
# print(n)
# a=random.random()
# print(a)
# b=random.random()*5
# print(a)

# n= random.randint(1,2)
# if n==2:
#     print("Head")
# else:
#     print("False")
# print(n)

#list
#append add the name at lst
#extend to add list
#inset to add item in a fix location
#pop to remove
#split remore ,
# name=input("Write all the names of friends")
# names=name.split(",")
# print(names)
# l=len(names)
# print(l)
# n=random.randint(0,l-1)
# print(names[n])

#Question- Rock Paper scissor
print("What do you choose?")
n=int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors"))
event=["Rock","Paper","Scissor"]
computer=random.randint(0,2)
if computer==n:
    print("Draw")
    print("you had selected "+event[n]+" and same computer is "+event[computer])
elif computer==0 and n==1:
    print("Win")
    print("you had selected "+event[n]+" and computer is "+event[computer])
elif computer==1 and n==2:
    print("Win")
    print("you had selected "+event[n]+" and computer is "+event[computer])
elif computer==2 and n==1:
    print("Lose")
    print("you had selected "+event[n]+" and computer is "+event[computer])
elif computer==2 and n==0:
    print("Lose")
    print("you had selected "+event[n]+" and computer is "+event[computer])
elif n==0 and computer==1:
    print("Win")
    print("you had selected "+event[n]+" and computer is "+event[computer])




