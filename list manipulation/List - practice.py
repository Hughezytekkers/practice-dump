


#define and declare lists
namesList = ['Ava', 'Bob', 'Charles', 'Dave','Emily']
gradesList = [45,34,15,44,34]
over18 = [True,True,False,True,True]

#create one from a string

#manipulate lists

#add an item within a list

#find an item within a list

#remove an item in a list

#step through a list - easy python style - quick & dirty
#for name in namesList:
    #print(name) #print always by default prints a new line character - "\n"
    #print(name, end=', ') #print will now do it all on the same line
    
#step through using index
for i in range(len(namesList)-1):
    print(namesList[i], end=', ',)
#after and outside for loop
print(namesList[-1]) #now prints the final element of the list

newName = input('Please enter a new name to add to the list! ') #adds it to the end
namesList.append(newName)
print(namesList)

#Adds it to anywhere
namesList.insert(0,newName)