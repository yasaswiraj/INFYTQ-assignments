#A teacher is in the process of generating few reports based on the marks scored by the students of her class in a project based assessment.
#Assume that the marks of her 10 students are available in a tuple. The marks are out of 25.


#Write a python program to implement the following functions:

#find_more_than_average(): Find and return the percentage of students who have scored more than the average mark of the class.
#generate_frequency(): Find how many students have scored the same marks. For example, how many have scored 0, how many have scored 1, how many have scored 3….how many have scored 25. The result should be populated in a list and returned.
#sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values should be populated in a list and returned.



list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    class_average=sum(list_of_marks)/10
    count_of_studs_scored_above_avg=sum(map(lambda x:x>class_average,list_of_marks))
    
    return (count_of_studs_scored_above_avg/10)*100
    
def sort_marks():
    return sorted(list_of_marks)

def generate_frequency():
    mark_frequency_list=[0]*26
    for mark in list_of_marks:
        mark_frequency_list[mark]+=1
    return mark_frequency_list
        
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
