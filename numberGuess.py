import random
number = random.randint(1, 20)
print('Please guess the random number between 1 and 20')

while True:
    try:
        guess = int(input())
        if guess > number:
            print('Your guess is higher than the number.')
            continue
        elif guess < number:
            print('Your guess is lower than the number.')
            continue
        else:
            print('Correct!')
            break
    except ValueError:
        print('Input an integer!')

