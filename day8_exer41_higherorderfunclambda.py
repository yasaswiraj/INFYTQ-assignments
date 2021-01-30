'''Write a higher order function, sum_all() to calculate the sum of elements in a list.
sum_all() – It accepts a list and calculates the sum of the elements in the list based on the conditions being checked in the lambda expressions passed to it.
Only those values satisfying the condition should be included in the sum.

Write the following lambda expressions.

greater: To check whether a given number is greater than 10.
divide: To check whether a given number is divisible by 10 and not greater than 100.
range_of_values: To check whether a given number is between 25 and 50 (Both inclusive).'''
def sum_all(function, data):
    sum=0
    for d in data:
        if(function(d)):
            sum=sum+d
    return sum
            


list_of_nos=[100,200,300,500,1040]

greater =lambda x:x>10 

divide = lambda x:x%10==0 and x<=100

range_of_values =lambda x:x>=25 and x<=50


#Use the below given print statements to display the output
# Also, do not modify them for verification to work
print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))
