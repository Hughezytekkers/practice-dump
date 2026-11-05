math_grades = [85, 90, 92, 78, 90, 88, 99, 99]
history_grades = [85, 92, 70, 95, 80]


def mode(grades):
    modes = []
    appearances = 0

    for grade in grades:
        counter = 0
        for i in grades:
            if i == grade:
                counter += 1

        # Found a score that appears MORE times than the current record
        if counter > appearances:
            appearances = counter
            modes = [grade]

        # Found a score that TIES the current record
        elif counter == appearances:
            if grade not in modes:
                modes.append(grade)

    return modes


print(f"The mode is {mode(math_grades)}")