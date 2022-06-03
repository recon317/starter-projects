#some example lists to pass
spam = ['apples', 'bananas', 'tofu', 'cats']
siblings = ['Dug', 'Jeff', 'Bob', 'Sally', 'Peter']
emptyList = []


def commaCode(myList): #main function
    try:
        length = len(myList) - 1 #find the length - 1 in order to join any sized list
        return (', '.join(myList[0:length]) + ', and ' + myList[-1]) #return string by joining list separated by comma;
        #then adding ', and ' only before the last item in the list
    except IndexError: #except for IndexError in order to avoid problems with empty lists
        return 'IndexError: Please enter a list that contains items.'



output = commaCode(siblings)

print(output)
