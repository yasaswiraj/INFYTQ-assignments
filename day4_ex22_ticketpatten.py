#Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
#The ticket number should be generated as airline:src:dest:number
#where

#Consider AI as the value for airline
#src and dest should be the first three characters of the source and destination cities.
#number should be auto-generated starting from 101
#The program should return the list of ticket numbers of last five passengers.


def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    total_ticket_list=[]
    #Write your logic here
    #Write your logic here
    for t in range(1,no_of_passengers+1):
        ticket=''
        ticket=airline[0:2]+':'+source[0:3]+':'+destination[:3]+':'+str(100+t)
        total_ticket_list.append(ticket)

    if len(total_ticket_list)>5:
        ticket_number_list=total_ticket_list[-5:]
    else:
        ticket_number_list=total_ticket_list
    
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",3))
