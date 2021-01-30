# anagaram example Reductions,discounter	
def check_anagram(data1,data2):
    l1=[]
    l2=[]
    for i in data1.lower():
        l1.append(i)
    for i in data2.lower():
        l2.append(i)
    c=0
    if len(data1)==len(data2):
        for i in range(0,len(data1)):
            if l1[i] in l2 and l1[i]!=l2[i]:
                c=c+1 
    else:
        return False
    if len(data1)==c:
        return True
    else:
        return False

print(check_anagram("tea","eat"))
