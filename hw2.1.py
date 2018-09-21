import random
hangman = ["""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
"""

         ]
print('Здравствуйте! Вам настолько нечем заняться,что вы решили поиграть в это жалкое подобие виселицы?На здоровье!Выберите одну из 3 тем:лингвистические термины (1), математические термины (2) и литературные термины (3). Введите 1, 2 или 3. ')
a = input()
if a == '1':
   with open ('lingterms.txt', encoding = 'utf-8') as f:
      text = f.read()
      lingterms = text.split('\n')
      word = random.choice(lingterms)
elif a == '2':
   with open ('mathterms.txt', encoding = 'utf-8') as f:
      text = f.read()
      mathterms = text.split('\n')
      word = random.choice(mathterms)
elif a == '3':
   with open ('litterms.txt', encoding = 'utf-8') as f:
      text = f.read()
      litterms = text.split('\n')
      word = random.choice(litterms)
word_list = list(word)
guesses = []
dashes = len(word) * '_'	
dashlist = list(dashes) 
newdashlist = list(dashes)
print('Угадайте слово.')
print (' '.join(dashlist))
for d in range(10):
    guess = input('Введите 1 букву: ')
    if guess not in 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя':
        print ('Что вам непонятно в слове "букву"?')
    elif len(guess) > 1:
        print ('Вы считать не умеете? Одну букву!!!')
    elif guess == '':
        print ('Ну и дальше что?')
    else:
        if guess not in word:
            print ('Одна ошибка и вы ошиблись.')
            print(' '.join(dashlist))
            
##            for l in hangman:
##                print(l)
        else:
            for i in range(len(word)):
                if guess == word[i]:
                    dashlist[i] = word_list[i]
            print(' '.join(dashlist))
        if guess in guesses:
            print('Вы это уже загадывали.')
            print(' '.join(dashlist))
    if d == 3 or d == 2:
        print("Осталось", d , "попытки")
    elif d == 1:
        print("Осталась", d , "попытка")
    else:
        print("Осталось", d , "попыток")
    if dashlist == word_list:
        print('Вы выиграли!(зачем вы только что потратили на это время...)')
        break
else:
    print('К сожалению, вы не справились даже с этой простейшей игрой. Займитесь лучше чем-нибудь полезным!')
    
    
            

                    
            

        
  
        
 
        
