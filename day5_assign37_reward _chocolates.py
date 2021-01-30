#A teacher is conducting a camp for a group of five children. Based on their performance and behavior during the camp, the teacher rewards them with chocolates.

#Write a Python function to

#Find the total number of chocolates received by all the children put together.
#Assume that each child is identified by an id and it is stored in a tuple and the number of chocolates given to each child is stored in a list.
#The teacher also rewards a child with few extra chocolates for his/her best conduct during the camp.
#If the number of extra chocolates is less than 1, an error message "Extra chocolates is less than 1", should be displayed.
#If the given child Id is invalid, an error message "Child id is invalid" should be displayed. Otherwise, the extra chocolates provided for the child must be added to his/her existing number of chocolates and display the list containing the total number of chocolates received by each child.


child_id=(101, 201, 301, 401, 501)
chocolates_received=[10, 5, 3, 2, 4]

def calculate_total_chocolates():
    return sum(chocolates_received)

def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates>0:
        if child_id_rewarded in child_id:
            child_id_index=child_id.index(child_id_rewarded)
            chocolates_received[child_id_index]+=extra_chocolates
            print(chocolates_received)
        else:
            print("Child id is invalid")
    else:
        print("Extra chocolates is less than 1")    

print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(201,2)
© 2021 GitHub, Inc.
