#Pyton program to find the factorial of number provided by user using the function


#WAP to find N! Using function.

def factorial(int):
    fac = 1
    if int < 0:
        print("factorial does not exist for negative numbers")
    elif int == 0:
        print("the factorial of 0 is 1")
    else:
        for i in range(1,int + 1):
            fac = fac * i
        print(fac)
    return

num = int(input("enter number"))
factorial(num)