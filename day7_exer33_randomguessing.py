import random

def guess_number(number_in_mind):
   a=random.randrange(1,10)
   print(a)
   
   if a>number_in_mind:
       print("number is high")
   elif a==number_in_mind:
     print("You have got it right!!!")
   else:
     print("Number is low")


            

#use the print statements given below wherever applicable
#print ('Number is low')
#print ('Number is high')
#print ('You have got it right!!!')

#Provide different values for number_in_mind and test your program
guess_number(4)
