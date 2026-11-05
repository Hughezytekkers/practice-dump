

#while PIN_GUESS != VALID_PIN:
#    ATTEMPTS += 1
#    PIN_GUESS = int(input(f'invalid pin , enter correct pin, you have done {ATTEMPTS} attempts out of three: '))
#    print(ATTEMPTS)
#    if ATTEMPTS == 3:
#        print("entered incorrect pin too many times")
#    elif PIN_GUESS == VALID_PIN:
#        print("correct PIN entered")


#def pin_checker(pin, attempts):
#    attempts = 0
#    pin = int(input("enter the pin: "))
#    valid = '1234' 
   
#    while attempts > 0 and pin != valid:
#        pin = int(input('enter your password: '))
#        attempts = attempts + 1
#        print("try again")

    
#    if pin == valid:
#        print("correct pin bro!")
#    else:
#        print("incorrect")   
        
#    return pin, attempts, valid
    
#print(f"do it {pin_checker(Apin, ATTEMPTS)}")

VALID_PIN = '1234'

def check_pin(attempts, pinlen):
    pin_valid = False
    pinlen = 4
    while attempts > 0 and not pin_valid:
        user_pin = int(input('please enter your pin: '))
        attempts -= 1
        
        if user_pin == VALID_PIN:
            pin_valid = True 
        
        else:
            print(f"try again, pin not valid, you have {attempts} attempts left")
    
    if attempts < 0 and not pin_valid:
       print("invalid pin entered too many times")
    else:
        print("accepted")
        
        
check_pin(3,4)