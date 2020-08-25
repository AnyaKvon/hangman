import random
from string import ascii_lowercase
# Write your code here
sentence = ['python', 'java', 'kotlin', 'javascript']

print('H A N G M A N')
while True:
    answ = input('Type "play" to play the game, "exit" to quit: ')
    if answ == 'play':
        comp = list(random.choice(sentence))
        ans = list(len(comp) * '-')
        sp = []
        n = 8
        while n != 0:
            print('')
            print(''.join(ans))
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print('You should input a single letter')
            elif letter not in ascii_lowercase:
                print('It is not an ASCII lowercase letter')
            elif letter in sp:
                print("You already typed this letter")
            elif letter in set(comp):
                sp.append(letter)
                for i in range(comp.count(letter)):
                    ans[comp.index(letter)] = letter
                    comp[comp.index(letter)] = '-'
            
            elif '-' not in ans:
                n = -1
                break
            elif letter not in comp:
                sp.append(letter)
                n -= 1
                print('No such letter in the word')
        if n == 0:
            print("You are hanged!")
        else:
            print(''.join(ans))
            print(""" You guessed the word!
                    You survived!""")
    else:
        break
