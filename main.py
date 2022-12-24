from random import randint

choices = ['Rock', 'Paper', 'Scissors']

def playerChoose():
    player_choice = ''
    has_chosen = False

    while player_choice not in choices and player_choice != 'I Quit':
        if has_chosen:
            print('That was not a valid choice, please try again')
        player_choice = input('Type Rock, Paper, or Scissors to play, or type I Quit to quit >> ').title()
        has_chosen = True
    
    quit = player_choice == 'I Quit'
    return quit, player_choice

def opponentChoose():
    choice = choices[randint(0, 2)]
    print(f'Your opponent has chosen: {choice}')
    return choice

def fight(player_choice: str, opponent_choice: str):
    results = ['You Win', 'You Lose']
    result = 'Game Tied'

    if player_choice == choices[0]: # Player chooses Rock
        if opponent_choice == choices[2]:
            result = results[0] # Player wins
        elif opponent_choice == choices[1]:
            result = results[1] # Loses
    elif player_choice == choices[1]:
        if opponent_choice == choices[0]:
            result = results[0]
        elif opponent_choice == choices[2]:
            result = results[1]
    else:
        if opponent_choice == choices[1]:
            result = results[0]
        elif opponent_choice == choices[0]:
            result = results[1]
    
    print(result)


while True:
    quit, player_choice = playerChoose()

    if quit:
        print('Thank you for playing')
        break

    opponent_choice = opponentChoose()
    fight(player_choice, opponent_choice)
