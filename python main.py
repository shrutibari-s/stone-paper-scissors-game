import random

def play_game():
    # Define available game choices
    choices = ["stone", "paper", "scissors"]
    
    # Initialize game score trackers
    player_score = 0
    computer_score = 0
    
    print("=======================================")
    print("Welcome to Stone, Paper, Scissors!")
    print("=======================================")
    print("Rules: Stone beats Scissors | Scissors beat Paper | Paper beats Stone\n")

    while True:
        # Secure valid user input with fallback handling
        user_choice = input("Enter Choice (Stone, Paper, Scissors) or 'Quit': ").strip().lower()
        
        if user_choice == 'quit':
            break
            
        if user_choice not in choices:
            print("❌ Invalid entry! Please check your spelling and try again.\n")
            continue

        # Generate automated computer selection
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        # Evaluate match results and update win metrics
        if user_choice == computer_choice:
            print("👔 It's a tie game!")
        elif (user_choice == "stone" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "stone") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 Match point to you! You won this round.")
            player_score += 1
        else:
            print("🤖 Computer wins this round!")
            computer_score += 1

        # Render ongoing scoreboard display
        print(f"Current Score -> You: {player_score} | Computer: {computer_score}")
        print("-" * 40 + "\n")

    # Present final statistics session summary
    print("\n=======================================")
    print("             GAME OVER                 ")
    print("=======================================")
    print(f"Final Tallies -> You: {player_score} | Computer: {computer_score}")
    
    if player_score > computer_score:
        print("🏆 Congratulations! You are the ultimate champion!")
    elif player_score < computer_score:
        print("💻 The machine wins this time. Better luck next game!")
    else:
        print("🤝 Perfect stalemate! The overall match ended in a tie.")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
