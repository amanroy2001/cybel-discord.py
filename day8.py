# import math
# def paintcan(height,weight,cover):
#     can=(height*weight)/cover
#     can=math.ceil(can)
#     print(can)
# paintcan(height=1,cover=5,weight=19)

#prime number
import math
def prime(n):
    if n==1:
        print("Its a prime number")
    elif n==2:
        print("Its a prime number")
    elif n==3:
        print("Its a prime number")
    else:
        for i in range(2,n-1):
            if n%i==0:
                is_prime=False       
    if is_prime:
        print("prime")
    else:
        print("not prime")

prime(16)