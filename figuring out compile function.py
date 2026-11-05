space_remover = """
def strip_spaces(s):
    s = s.replace(" ", "")
    return s

def length_check_of_plate(r):
    length = len(r)
    if length != 7:            
        return False, "false - incorrect length"   
    return True, "correct lenght"
"""

compiled_function = compile(space_remover, filename="space_be_gone", mode="exec")

# 1. Namespace MUST be a dictionary
namespace = {}

# 2. Execute the compiled code into the dictionary
exec(compiled_function, namespace)

# 3. Use the exact function name defined in the string ("strip_spaces")
calc = namespace["strip_spaces"], namespace["length_check_of_plate"]


# Test it together
plate_input = "AB12 3CD"
cleaned_plate = calc(plate_input)


print(f"Cleaned: {cleaned_plate}")  # Output: AB123CD
