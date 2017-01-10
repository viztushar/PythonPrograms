
#Write a Function to swap values of a pair of integers.

def swap(num1,num2):
    tem = num1
    num1 = num2
    num2 = tem
    print("num1 is ", num1, " num2 is ", num2)
    return

num1 = input("enter number one = ")
num2 = input("enter number two = ")
swap(num1,num2)
