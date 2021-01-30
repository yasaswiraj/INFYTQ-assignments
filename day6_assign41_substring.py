#A 10-substring of a number is a substring of its digits that sum up to 10.

#For example, the 10-substrings of the number 3523014 are:
#3523014, 3523014, 3523014, 3523014

#Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.
def find_sum(num):
    summ = 0
    for n in num:
        summ += int(n)
    return summ
    
def find_ten_substring(num_str):
    arr = []
    for i in range(2, len(num_str)):
        end_index = len(num_str)-i+1
        for j in range(0, end_index):
            if find_sum(num_str[j:j+i]) == 10:
                arr.append(num_str[j:j+i])    
    return arr
    
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
