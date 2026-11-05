original_price = 100.00
sale_active = True
age = 80
sale_discount = 0.20
senior_discount = 0.10

def price_calc(itemPrice):
    if sale_active == True and age > 65:
        itemPrice - itemPrice * 0.30
        print(f"You are eligable for both discounts which gives you a total of 30% off! ")
    elif sale_active:
        itemPrice - itemPrice * sale_discount
        print(f"You are eligable for a sale discount of 20%! ")
    elif age > 65:
        itemPrice - itemPrice * senior_discount
        print(f"You are eligable for a senior discount of 10%! ")
    else:
        itemPrice
        (f"sadly you are not eligable for any discounts :( ")
    return 

 
print(f"total discounted price: {price_calc(original_price)}")

