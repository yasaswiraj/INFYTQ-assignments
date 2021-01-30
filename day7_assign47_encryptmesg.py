'''Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.
Also write the pytest test cases to test the program.

Sample Input	                 Expected Output
the sun rises in the east	eht snu sesir ni eht stea'''

def encrypt_sentence(sentence):
    #start writing your code here
    fin=""
    lis=sentence.split()
    for i in range(0,len(lis)):
        temp=""
        if i%2==0:
            temp=lis[i]
            fin=fin+temp[::-1]+' '
        else:
            temp=lis[i]
            tem=""
            vow=""
            conso=""
            for i in temp:
                if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
                    vow=vow+i
                else:
                    conso=conso+i
            tem=conso+vow
        
            fin=fin+tem+' '
    fin=fin.strip()
    return fin

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
