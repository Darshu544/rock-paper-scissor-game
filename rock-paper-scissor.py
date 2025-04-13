import random

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nRock-Paper-Scissors Game")
        print("-----------------------")
        print(f"Score: You {user_score} - Computer {computer_score}")
        print("\nChoose: (1) Rock, (2) Paper, or (3) Scissors")
        
        # User input
        while True:
            try:
                user_choice = int(input("Enter your choice (1-3): "))
                if user_choice in [1, 2, 3]:
                    break
                else:
                    print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Map numbers to choices
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        user_choice_name = choices[user_choice]
        
        # Computer selection
        computer_choice = random.randint(1, 3)
        computer_choice_name = choices[computer_choice]
        
        print(f"\nYou chose: {user_choice_name}")
        print(f"Computer chose: {computer_choice_name}")
        
        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        # Play again?
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nFinal Score:")
            print(f"You: {user_score} - Computer: {computer_score}")
            print("Thanks for playing!")
            break

# Start the game
play_game()