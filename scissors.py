import random
# Allow the computer to randomly choose rock, paper, or scissors in each round
def Computer():
    choose = ['rock', 'paper', 'scissors']
    return random.choice(choose)

# Allow the user to now input their choice
def User():
    choice = input("Choose (rock, paper, scissors):  ")
    return choice

# compare it directly with the computer’s choice
def play_winner(Computer, you):
    if you == Computer:
        return 'tie'
    elif (you == 'rock' and Computer == 'scissors') or \
            (you == 'scissors' and Computer == 'paper') or \
            (you == 'paper' and Computer == 'rock'):
        return 'You win'
    else:
        return 'You loose'

# declare the winner of the round based on the rules of the game

def get_winner(rounds):
    userScore = 0
    computerScore = 0

    rounds = 5
    for _ in range(rounds):
        you = User()
        cpu = Computer()
        print(f"Computer chose: {cpu}")

        # assign a point to the winner of a round
        if play_winner(Computer, you) == 'tie':
            print(f"It's a tie, cpu:{computerScore} user: {userScore}")
        elif play_winner(Computer, you) == 'You win':
            userScore += 1
            print(f"You win, cpu:{computerScore} user: {userScore}")
        else:
            computerScore += 1
            print(f"The computer wins!, cpu:{computerScore} user: {userScore}")
#declare the winner immediately a user guess 2 points out of 3 in a 3-round game or 3 out of 5 points in a 5-round game '''

    if userScore > computerScore:
            print("You win!")
    elif computerScore > userScore:
            print("The computer wins!")
    else:
            print("The game is a tie!")


if __name__ == "__main__":
    rounds = int(input("Enter the number of rounds: "))
    get_winner(rounds)












