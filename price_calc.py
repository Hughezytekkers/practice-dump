PRICE = 100
SALE = True
AGE = 80


discount_percent = 0

def discounts(price, active, oldness):
    
    d1 = 0.20
    d2 = 0.10
    
    if active and oldness > 65:
        discount_percent = d1 + d2
        print(price = price - discount_percent)
        
    elif active:
        discount_percent = d1
        print(price = price - discount_percent)
        
    elif oldness > 65:
        discount_percent = d2
        print(price = price - discount_percent)
        
    else:
        discount_percent = 0.0
    
    return discount_percent

print(f"here is the prices according to what you're eligable for: {discounts(PRICE,SALE,AGE)}")