#Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

def find_common_characters(msg1,msg2):
    res=''
    for char in msg1:
        if char in msg2 and char!=' ' and char not in res:
                res=res+char
    if res=='':
        return -1
    else:
        
        return res
#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
