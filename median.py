math_grades = [85, 977, 66, 77, 33, 44, 92, 78,]
history_grades = [85, 92, 70, 95, 80, 85]

def find_median(grades):
    if not grades:
        return None

    sorted_grades = sorted(grades)
    numbers = len(sorted_grades)
    mid = numbers // 2

    if numbers % 2 != 0:
        return sorted_grades[mid]

    return (sorted_grades[mid - 1] + sorted_grades[mid]) / 2




print("Math median:", find_median(math_grades))
print("History median:", find_median(history_grades))

