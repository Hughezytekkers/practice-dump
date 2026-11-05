#use of compile function

#x = compile('print(55), print(88), print(55+15)', 'compile1.py', 'exec')
#exec(x)


#f = open("randomize.py", "r")
#print(f.read())

#num = round(5.948582859, 5)
#print(num)

# 1. Define your function as a string
code_str = """
def calculate_tax(price, rate=0.10):
    return price + (price * rate)
"""

# 2. Compile the string in 'exec' mode
compiled_code = compile(code_str, filename="<tax_calculator>", mode="exec")

# 3. Create a dictionary to act as the namespace
namespace = {}

# 4. Execute the compiled bytecode inside that namespace
exec(compiled_code, namespace)

# 5. Extract and call the function from the dictionary
tax_fn = namespace["calculate_tax"]
result = tax_fn(100, 0.15)

print(result)  # Output: 115.0