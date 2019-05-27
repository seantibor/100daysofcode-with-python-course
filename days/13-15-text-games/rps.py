import bullet as b
import random

class Roll:
    
    def __init__(self, name: str, wins: list=[], loses: list=[]):
        self.name = name
        self.wins = wins
        self.loses = loses

    def check_win(self, opposing_roll) -> bool:
        if opposing_roll.name == self.name:
            return None
        return opposing_roll.name in self.wins

class Player:

    def __init__(self, name: str):
        self.name = name
        self.roll = None
        self.score = 0
    

def setup_rolls():
    rolls = {
        'Rock': Roll('Rock', wins=['Scissors'], loses=['Paper']),
        'Paper': Roll('Paper', wins=['Rock'], loses=['Scissors']),
        'Scissors': Roll('Scissors', wins=['Paper'], loses=['Rock']),
    }
    return rolls

def main():
   print_header()
   game_loop() 
   end_game()

def game_loop():
    rolls = setup_rolls()

    cli = b.Input('What is your name? ')
    p1 = Player(cli.launch())
    p2 = Player('computer')

    print(f'Welcome to Rock Paper Scissors, {p1.name}')

    while True:
        cli = b.Bullet(prompt='Choose your roll: ', choices=list(rolls.keys()))
        p2.roll = random.choice(list(rolls.values()))
        p1_choice = cli.launch()
        print(p1_choice)
        p1.roll = rolls[p1_choice]
        print()
        print(f"You chose {p1.roll.name} and the computer chose {p2.roll.name}")
        # compare rolls
        
        if p1.roll.check_win(p2.roll):
            print("You Win!")
            p1.score += 1
        elif p1.roll.check_win(p2.roll) is None:
            print("Tie!")
        else:
            print("You Lose!")
            p2.score += 1
        # print scores
        print_scores(p1, p2)
        cli = b.YesNo(prompt="Play again? ")
        if not cli.launch():
            # end the game
            print_scores(p1, p2)
            return
        

def print_header():
    print('------------------------------')
    print('       Welcome to RPS         ')
    print('------------------------------')
    print()

def print_scores(p1, p2):
    print('----------------------')
    print(f"P1 {p1.name}: {p1.score}")
    print(f"P2 {p2.name}: {p2.score}")
    print('----------------------')

def end_game():
    print('Thanks for playing!')
    
if __name__ == '__main__':
    main()