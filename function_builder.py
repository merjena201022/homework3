import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    # We use a while loop to keep asking until the input is valid
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Try again!")

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    
    # Logic for player winning
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def play_round():
    player = get_player_choice()
    computer = get_computer_choice()
    print(f"Computer chose: {computer}")
    
    result = determine_winner(player, computer)
    
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win this round!")
    else:
        print("The computer wins this round!")
    
    return result

def play_game():
    player_score = 0
    computer_score = 0
    
    # Use a while loop to manage multiple rounds
    while True:
        result = play_round()
        
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
            
        print(f"Score -> You: {player_score} | Computer: {computer_score}")
        
        again = input("\nPlay another round? (yes/exit): ").lower()
        if again == 'exit':
            print("Final Score reached. Thanks for playing!")
            break

# Start the game
play_game()