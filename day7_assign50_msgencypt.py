'''Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence.

Rules are as follows:
a. Spaces are to be retained as is
b. Each word should be encoded separately

If a word has only vowels then retain the word as is
If a word has a consonant (at least 1) then retain only those consonants'''

def sms_encoding(data):
    words=data.split()
    final=''
    for word in words:
        if len(word)>1:
            temp=''
            for char in word:
                if char!='a' and char!='e' and char!='i' and char != 'o' and char!='u' and char!='A' and char!='E' and char!='I' and char!='O' and char!='U':
                    temp=temp+char
            final=final+temp+' '
        else:
            final+=word+' '
    return final.strip()
    
data="I love Python"
print(sms_encoding(data))
