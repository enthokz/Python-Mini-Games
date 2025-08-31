# Greetings Message
'''
Create a function to show greeting message to the 
player and ask for player name that used in game.
'''

def greet():
    print(f'''{'-'*72}
|{"Welcome":^70}|
{'-'*72}\n
To start the game, please insert your player name below: ''')
    player_name=input('Player Name = ')
    print(f"\nAllohaa {player_name}! it's time to start the game...")
    return player_name


# Guide of the game
'''
Create a function to show instruction how play this game.
The answer will be in range 1-4 of integer. Therefore, we will create function
that accepts integer format only.
'''

def describe():
    print('''\nThe game is easy. Let's catch a Bahlil!
Bahlil is hiding in one of the cave below right now:
       _    _    _    _
      |1|  |2|  |3|  |4|
       ‾    ‾    ‾    ‾''')
    

# Question Funtion
'''
Create a function for question that used in game.
Function in this section is also have a jrole to validate an answer that player 
guees in game.
'''
'''
This function is set to accepts integer format answer only 
using exeption handling method.
Create a loop for incorrect format answer until 
the palyer answer the correct one.
'''

def question(msg,choice):
    while True:
        try:
            ans= int(input(msg))
            if ans in choice:
                return ans
            else:
                print(f'\nPlease check your answer. The answer only in range {choice}')
        except ValueError:
            print(f'\nPlease check your answer. The acceptable answer only in range {choice}')


# Set an answer
'''
Create a function for randomly select integer 
in range 1-4 for the answer of question function before.
'''

import random
key=random.randint(1,4)

# Create a gameplay
'''
Create a function for a gameplay of this game.
First, asking the player to guees where the cave Bahlil hidding for.
Second, make sure the player for answer that they are trying to guees.
Create a loop until the player is sure of the answer. 
'''

def game():
    guess=question('Which cave that Bahlil try to hide? ',[1,2,3,4])
    confirm=question('Are you sure? (1=Yes 2=No)',[1,2])
    while confirm:
        if confirm==1:
            return guess
        else:
            guess=question('\nWhich cave that Bahlil try to hide? ',[1,2,3,4])
            confirm=question(f'Are you sure bahlil hiding in cave {guess}? (1=Yes 2=No)',[1,2])


# Create an Answer
'''
Create a function to show a result from player answer.
In the end, ask player if they want to try it again.
'''

def result():
    if ply_guess==key:
        print(f'''
{'-'*72}
Congratulation {player}!! You have catched Bahlil !!
The cave number {ply_guess} as you answered, it was balil's hiding place.
{'-'*72}''')
    else:
        print(f'''
{'-'*72}
Unfortunately, Bahlil has not been caught yet.
You answered the cave number {ply_guess}. in fact, bahlil was hiding in the cave number {key}
{'-'*72}''')
    play_again=question('Play again? (1=Yes 2=No)',[1,2])
    return play_again


# Create how this game work
'''
Create gameplay, starting with greeting
player until result for players answered.
'''

player= greet()             #1 greeting
while True:                 # Loop for player want to try again
    describe()              #2 Guide
    ply_guess=game()        #3 Gameplay
    end=result()            #4 Result
    if end ==2:
        print(f'''\n{'-'*72}
{"Thank You for Playing!!":>49}
{"See Yaa!!":>42}
{'-'*72}''')
        break
    else:
        print(f'''\n{'-'*72}
{"NEW GAME":>40}
{'-'*72}''')