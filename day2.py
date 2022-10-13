# #String
# print("Hello"[4])
# #print(100/15)
# print("133"+"1312")

# #Integer
# print(123+2112)

# #Float
# num_char=str(input("What is your name?"))
# print(type(num_char))
# print("Your Name has "+num_char+" wfwefef")

#Q1-Sum of 2 digit number
# a=(input("Type a two digit number --"))
# sum=(int(a[0])+int(a[1]))
# print(sum)

#Q2-BMI Calculatow=
# w=float(input("Plesse input your Weight"))
# l=float(input("Please input your Lenght"))
# bmi=w/(l*l)
# print(bmi)
# print(round(7/2,2))

# #F-string
# score=0
# height=1.8
# iswiinner=True
# print(f"hii i am {score} my height is {height} {iswiinner} ")

# #Q-3 Life in weeks
# age=int(input("What is your current age-?"))
# year=90-age
# months=(90*12)-(age*12)
# weeks=(90*12*52)-(age*12*52)
# days=year*365

# print(f"You have {days}days left, {weeks}weeks, {months}months and {year}year")

# Q-4
# Tip Calculator
print("Welcome to tip calculator")
bill=float(input("What is the total bill? "))
tip=int(input("How much persent would you like to give tip ?"))
n=int(input("In How many person we had to split the bill"))
pay=(bill/n)+(((tip/100)*bill)/n)
rounded=round(pay,2)
print(f"Each person will pAY {rounded}")

