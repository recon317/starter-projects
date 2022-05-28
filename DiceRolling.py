import random
import sys
print('This program is a six-sided dice rolling simulator.')

while True:
    x = str(random.randint(1, 6))
    print()
    print('Your number is ' + x +'.')
    print()
    print('Would you like to roll again? (Y/N)')
    again = input()
    if again == 'Y':
        continue
    elif again == 'N':
        break
    else:
        print('Enter Y or N.')
        sys.exit()
