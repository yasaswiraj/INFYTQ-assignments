#Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.

#Always num1 should be less than num2
#Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
#Sum of the digits of the number is a multiple of 3
#Number has only two digits
#Number is a multiple of 5
#Display the maximum element from the list
#In case of any invalid data or if the list is empty, display -1.

def is_sum_multiple_of_three(num):
    summ=0 
    while num!=0:
        summ=summ+num%10 
        num=num//10
    if summ%3==0:
        return True
    else:
        return False

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    list1=[]
    if num1<num2:
        for num in range(num1,num2+1):
            if num%5==0 and num>9 and num<100 and is_sum_multiple_of_three(num)==True:
                list1.append(num)
              
        if len(list1)>0:
            max_num=max(list1)  
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(14,2)
print(max_num)
