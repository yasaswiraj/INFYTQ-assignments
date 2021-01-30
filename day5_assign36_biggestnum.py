#Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers.
def create_largest_number(number_list):
    num=''
    number_list.sort(reverse=True)
    for no in number_list:
        num=num+str(no)
    return int(num)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
