import random

choices = ["rock", "paper", "scissors"]
bot_score = 0
player_score = 0
tie_score = 0
total_games = 0

print("Welcome to Rock-Paper-Scissors Game!")

while True:
    user_input = input("Choose rock, paper, or scissors: ").lower()

    if user_input not in choices:
        print("Invalid choice. Please choose either rock, paper, or scissors.")
        continue

    bot_choice = random.choice(choices)
    print(f"Bot chose: {bot_choice}")

    if user_input == bot_choice:
        print("It's a tie!")
        tie_score += 1
    elif (user_input == "rock" and bot_choice == "scissors") or \
         (user_input == "scissors" and bot_choice == "paper") or \
         (user_input == "paper" and bot_choice == "rock"):
        print("You win!")
        player_score += 1
    else:
        print("Bot wins!")
        bot_score += 1

    total_games += 1

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("\nGame Summary:")
print(f"Total games played: {total_games}")
print(f"Player wins: {player_score}")
print(f"Bot wins: {bot_score}")
print(f"Ties: {tie_score}")
print("Thanks for playing!")
