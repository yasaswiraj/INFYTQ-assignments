'''Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers.
Assume that the words contain only uppercase letters and the maximum word length is 10.

Also write the pytest test cases to test the program.


Sample Input                                                                 	                Expected Output
{"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}	[2, 2, 1]'''

def find_correct(word_dict):
    correct_list=[0]*3
    for key,value in word_dict.items():
        if len(key) == len(value):
            difference=0
            for i in range(len(key)):
                if key[i]==value[i]:
                    continue
                else:
                    difference+=1
            if difference == 0:
                correct_list[0]+=1
            elif difference < 3:
                correct_list[1]+=1 
            else:
                correct_list[2]+=1
        else:
           correct_list[2]+=1 
    return correct_list

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
