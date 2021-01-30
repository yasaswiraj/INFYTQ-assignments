def sum_of_numbers(list_of_num,filter_func=None):
    num_sum=0
    if filter_func!=None:
        num_sum=sum(filter_func(list_of_num))
    else:
        num_sum=sum(list_of_num)
    return num_sum
            
def even(data):
    even_no=[]
    for num in data:
        if num%2==0:
            even_no.append(num)
    return even_no
def odd(data):
    odd_no=[]
    for num in data:
        if num%2!=0:
            odd_no.append(num)
    return odd_no
sample_data = range(1,11)

print(sum_of_numbers(sample_data,odd))
print(sum_of_numbers(sample_data,even))
print(sum_of_numbers(sample_data,None))
