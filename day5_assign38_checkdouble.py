#Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

#The number and its double should have exactly the same number of digits.
#Both the numbers should have the same digits ,but in different order.
#Otherwise it should return False.

#Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.
def check_double(number):
    double_of_number=2*number
    str_num=str(number)
    str_dbl_num=str(double_of_number)
    if len(str_num)==len(str_dbl_num):
        for i in range(0,len(str_num)):
            if str_num[i] in str_dbl_num:
                continue
            else:
                return False 
    else:
        return False
        
    return True
#Provide different values for number and test your program
print(check_double(9))
