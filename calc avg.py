#student_scores = [100,99,45,68,46,56,76,34,76,58,72,65,87,34,67,23,97,43,98,23,67,98,65,43,65,43,65,86,43,67]
#
#def average(l):
#    total = 0
#    for i in l:
#        total += i
#        
#    return total/ len(l)
#
#print(f"average score is: {average(student_scores):.2f}")

valid_password = False



def upper(s):
    for char in s:
        if char == char.upper:
            return True

def hasnum(s):
    for char in s:
        if char.isdigit():
            return True
        
def checkspaces(s):
    for char in s:
        if char == "":
            return True
        
while not valid_password:
    enter_password = input("what is your password: ")
    
if len(enter_password) < 6 or len(enter_password) > 64:
    print("Invalid length, either below 6 or above 64")
elif not upper(enter_password):
    print("needs uppercase")
elif not hasnum:
    print("cant be blank")
elif not checkspaces:
    print("cant have spaces")