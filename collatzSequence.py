import sys

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return number * 3 + 1

print('Input an integer.')
i = input()

try:
    while i != 1:
        i = collatz(int(i))
        print(i)
except ValueError:
    print('Something went wrong')
    sys.exit()
