import random

numbersList = [3,6,1,2,7,6,2,9,10]

def Randomize(randomize):
    randomed = []
    randomize = random.randint(randomize)
    for val in randomize:
        randomed.append(val)
    return randomed
 
 
 
print(f"the numbers randomized are: {Randomize(numbersList)}")