print('This program can determine your birthyear.')
print()
while True:
    try:
        print('What is your age?')
        age = int(input())
        break
    except ValueError:
        print('Input your age as an integer.')
        print()
while True:
    try:
        print('What year is it?')
        year = int(input())
        break
    except ValueError:
        print('Input the year as an integer.')
        print()


def yes():
    birthyear = str(year - age)
    print('Your birthyear is ' + birthyear +'.')

def no():
    birthyear = str(year - age - 1)
    print('Your birthyear is ' + birthyear +'.')

while True:
    print('Have you had your birthday this year? (Y/N)')
    yesNo = input()
    print()
    if yesNo == 'Y' or yesNo == 'N':
        break
    else:
        print('Enter \'Y\' or \'N\'')
        continue


if yesNo == 'Y':
    yes()
elif yesNo == 'N':
    no()
