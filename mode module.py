import statistics


#here we attempt to make a mode module

math_grades = [85, 90, 92, 78, 90, 88, 99, 99]
history_grades = [85, 92, 70, 95, 80,85 ]




def mode(grades):
    modes = []       
    appearances = 0
    
    for grade in grades:
        counter = 0
        for i in grades:
           if i == grade:
               counter += 1
               
        if counter > appearances:
            appearances = counter 
            modes.clear()
            modes = [grade]
            
        elif counter == appearances and grade not in modes:

                modes.append(grade)

        
    return modes



print(f"the mode for math grades is {mode(math_grades)}")
print(f"the mode for histort grades is {mode(history_grades)}")
