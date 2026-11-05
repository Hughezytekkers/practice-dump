textbook_price = input("What is the price of the textbook? ")
textbook_price = float(textbook_price)
shipping = (5)

def total_price(price):
    total = textbook_price + shipping
    return total

cost = print(f"The total cost will be £{total_price(textbook_price)}")
