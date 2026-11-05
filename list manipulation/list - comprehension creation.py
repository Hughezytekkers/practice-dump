#create a quick list of 500 random items with list comprehension

import random

age_list = [random.randint(1,100) for i in range(500)]


def calc_mean(ageFinder):
    total = 0
    for i in range (len(ageFinder)):
        total += ageFinder[i]
        
    return total/len(ageFinder)

print(f"the average age is {calc_mean(age_list)}")