#ite a python program which merges the content of two given lists and sorts the merged list.

#Write the following functions to achieve the above functionalities:

#def merge_lists(list1,list2): Returns the merged list. Use keyword arguments to pass the lists in method invocation
def merge_lists(list1,list2):
    new_merge_list=list1+list2
    return new_merge_list
    
def sort_list(merged_list):
    return sorted(merged_list)

#Provide different values for list1 and list2 and test your program
merged_list=merge_lists(list1=[1,2,3,4,1] ,list2=[2,3,4,5,4,6])
print(merged_list)
sorted_merged_list=sort_list(merged_list)
print(sorted_merged_list)
