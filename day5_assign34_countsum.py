#Write a python function, find_pairs_of_numbers() which accepts a list of positive integers with no repetitions and returns count of pairs of numbers in the list that adds up to n. The function should return 0, if no such pairs are found in the list.
def find_pairs_of_numbers(num_list,n):
    count_of_pairs=0
    for i in range(0,len(num_list)-1):
        for j in range(i+1,len(num_list)):
            if num_list[i]+num_list[j]==n:
                count_of_pairs+=1 
                break
    return count_of_pairs
num_list=[1, 2, 7, 4, 5, 6, 0, 3]
n=6
print(find_pairs_of_numbers(num_list,n))
