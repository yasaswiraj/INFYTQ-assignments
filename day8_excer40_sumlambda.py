'''Write a python lambda expression for calculating sum of two numbers and find out whether the sum is divisible by 10 or not.

'''
num1=10
num2=10

div = lambda num1,num2:num1+num2#Write the lambda expression here

if(div(num1,num2)%10)==0:
    print("Divisible by 10")
else:
    print("Not Divisible by 10")
