import random

options = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissor!\n")
print("If you don't want to play, type 'exit' to quit the game.\n")

while True:
    user_input = input("Enter your choice (rock, paper or scissor): ").lower()
    
    if user_input == "exit":
        print("\nGame Over!")
        print(f"User score: {user_score}")
        print(f"Computer score: {computer_score}")
        
        if user_score > computer_score:
            print("User wins the game!")
        elif user_score < computer_score:
            print("Computer wins the game!")
        else:
            print("It's a tie!")
        break
    
    if user_input not in options:
        print("Please enter a valid option (rock, paper or scissor)\n")
        continue

    computer_input = random.choice(options)
    print(f"\nUser input is: {user_input}")
    print(f"Computer input is: {computer_input}")
    
    if computer_input == user_input:
        print("It's a tie!\n")
    elif (user_input == "rock" and computer_input == "scissor") or \
         (user_input == "scissor" and computer_input == "paper") or \
         (user_input == "paper" and computer_input == "rock"):
        print("User wins this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1