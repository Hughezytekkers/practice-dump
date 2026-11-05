VALID_PIN = '1234'
ATTEMPTS = 3
PIN_GUESS = int(input("the pin is: "))

while PIN_GUESS != VALID_PIN:
    ATTEMPTS -= 1
    PIN_GUESS = int(input(f'invalid pin , enter correct pin, you {ATTEMPTS} attempts left: '))
    print(ATTEMPTS)

if PIN_GUESS == VALID_PIN:
    print("correct PIN entered")