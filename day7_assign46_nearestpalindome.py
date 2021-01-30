#PF-Assgn-46
#find nearest paindrome of a numbe

def is_palindrome(num):
    tem=str(num)
    if tem==tem[::-1]:
        return True

def nearest_palindrome(number):
    while True:
        if is_palindrome(number):
            return number
        else:
            number+=1 

number=123
print(nearest_palindrome(number))
