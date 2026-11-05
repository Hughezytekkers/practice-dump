from datetime import datetime
Current_year = datetime.now().year
Current_year = int(Current_year)

def whenBorn(ageofperson):
    birth_year = int(Current_year) - int(age)
    return birth_year

age = input("How old did you turn this year/are turning this year? ")
birth_year = str(whenBorn(age))
born = print("You were born in the year " + (birth_year))


