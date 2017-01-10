#WAP to find, a given number is prime or not

num = int(input("enter number"))

if num>1:
    #check for factors
    for i in range(2,num):
        if(num / i) == 0:
            print(num," is not prime number")
            break

else:
    print(num," is not a prime number")