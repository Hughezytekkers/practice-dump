numbersList = [3,6,1,2,7,6,2,9,10]

sorted = sorted(numbersList)

total = sum(sorted)


def findEven(even):
    result = []
    for val in even:
        if val % 2 == 0:
            result.append(val)
    return result

def square(squaredNum):
    result = []
    for val in squaredNum:
        val = val*val
        result.append(val)
    return result

def backwards(LB):
    reversed_list = []
    for i in range(len(LB)-1, -1, -1):
        reversed_list.append(LB[i])
    return reversed_list

def findFactors(fact):
     result = []
     factor = int(input(f"what is the factor?: "))
     for val in fact:
         if val % factor == 0:
            result.append(val)
     return result



print(f"the sum of the numbers are: {total}")
print(f"the even numbers are: {findEven(numbersList)}")
print(f"the squared numbers are: {square(numbersList)}")
print(f"the numbers backwards  are: {backwards(numbersList)}")
print(f"the factor (that you chose) of the numbers are: {findFactors(numbersList)}")