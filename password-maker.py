from os import system
from sys import platform
from random import choice
from string import ascii_letters, punctuation, digits

def clear():
    if platform == 'linux' or 'posix':
        system('clear')
    else:
        try:
            system('cls')
        except:
            pass

def chars():
    charPass = ascii_letters + punctuation + digits
    return charPass

def passMaker():
    clear()

    try:
        passLen = int(input('Enter length of password: '))
        thisWord = input('\nDo you want to add more words in password (y, n(default))? ')

        if thisWord.lower() == 'y':
            thisWord = input('\nWhat words do you want to be in the password? ')
            selectWord = input('\nWould you like the position word (random, scatter, static)? ')
            
            if selectWord.lower() == 'random':
                password = ''.join(choice(chars() + thisWord) for i in range(0, passLen))

            elif selectWord.lower() == 'scatter':
                password = thisWord.join(choice(chars()) for j in range(0, passLen))
                if len(password) > passLen:
                    password = password[:passLen]

            elif selectWord.lower() == 'static':
                password = thisWord + ''.join(choice(chars()) for k in range(0, passLen))
                if len(password) > passLen:
                        password = password[:passLen]
            
            else:        
                pass

        else:
            password = ''.join(choice(chars()) for i in range(0, passLen))
        
        clear()
        return print('This is your password: ', password)
    
    except:
        pass

passMaker()

while True:
    redo = input('Would you like restart script (y, n(default))? ')
    
    if redo == 'y':
        passMaker()
        
    else:
        print('OK,\nBye Bye...')
        break
