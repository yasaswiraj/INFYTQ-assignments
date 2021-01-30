#Write a python program to solve a classic ancient Chinese puzzle.

#We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?


def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if legs%2!=0 or heads==0 or heads>legs:
        print(error_msg)
    else:
        rabbit_count=int((legs-(2*heads))/2)
        chicken_count=int(heads-rabbit_count)
        print(chicken_count,rabbit_count)
#Provide different values for heads and legs and test your program
solve(35,94)
