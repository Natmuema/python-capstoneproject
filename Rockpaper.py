import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game(rounds):
    user_points = 0
    computer_points = 0
    
    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            user_points += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_points += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        
        print(f"Score: You {user_points} - {computer_points} Computer")
        
        if (rounds == 3 and (user_points == 2 or computer_points == 2)) or \
           (rounds == 5 and (user_points == 3 or computer_points == 3)):
            break
    
    if user_points > computer_points:
        print("Congratulations! You win the game!")
    elif computer_points > user_points:
        print("Sorry, you lost the game. The computer wins!")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    rounds = int(input("Enter the number of rounds (3 or 5): "))
    while rounds not in [3, 5]:
        print("Invalid number of rounds. Please choose 3 or 5.")
        rounds = int(input("Enter the number of rounds (3 or 5): "))
    
    play_game(rounds)
