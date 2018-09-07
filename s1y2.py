import random

letters = 'abcdefghijklmnopqrstuvwxyz'
letter = letters[random.randint(0, 25)]
while True:
    a = input('Enter letter: ')
    if a not in letters:
        print ('nope')
        continue
    if a == letter:
        print ('u won')
        break
    if a < letter:
        print('later')
    else:
        print ('earlier')


        
        
        
        
 
