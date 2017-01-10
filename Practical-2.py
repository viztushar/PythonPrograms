#WAP to read two numbers from the keyboard and display the larger one on the screen.

num1 = input("enter the number one")
num2 = input("enter the number two")

if(num1>num2):
    largest = num1
    print("number is ", largest)
else:
    largest = num2
    print("number is ",largest)
