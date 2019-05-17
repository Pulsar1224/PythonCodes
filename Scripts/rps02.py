import random

class Rps():
    """ Rock, Paper, Scissors """

    def game(self):
        print(f'\nRock = r or R, Paper = p or P, Scissors = s or S')
        userChoice = input("Enter your choice -->  ")
        userChoice = userChoice.upper()
        
        computerChoice = random.choice(['R','P','S'])
        print(f'Computer\'s choice : {computerChoice} ')

        print(f'==============================')
        print(f'{userChoice} v/s {computerChoice}')
        print(f'==============================')

        if userChoice == computerChoice:
            print(f'Its a tie')
            exit

        if userChoice == "R":
            if computerChoice == "P":
                print(f'Winner : Paper'.center(25, ' '))
            elif computerChoice == "S":
                print(f'Winner : Rock'.center(25, ' '))

        if userChoice == "P":
            if computerChoice == "R":
                print(f'Winner : Paper'.center(25, ' '))
            elif computerChoice == "S":
                print(f'Winner : Scissors'.center(25, ' '))

        if userChoice == "S":
            if computerChoice == "P":
                print(f'Winner : Scissors'.center(25, ' '))
            elif computerChoice == "R":
                print(f'Winner: Rock'.center(25, ' '))
                
        

    def playAgain(self, choice):
        self.game()



user1 = Rps()
user1.game()

play = int(input("Type 1 to play again and cntrl + c to quit "))
while(play !=0):
    user1.playAgain(play)
        
        
