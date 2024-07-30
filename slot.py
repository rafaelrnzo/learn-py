import random

# List of possible slot symbols
list_slots = ["7", "fantastic", "jackpot", "amazing"]

# Initial user coins
user_coins = 1000

def play_slot_machine(coins):
    first_col = random.choice(list_slots)
    second_col = random.choice(list_slots)
    third_col = random.choice(list_slots)
    
    print(f'{first_col} | {second_col} | {third_col}')
    
    if first_col == "7" and second_col == "7" and third_col == "7":
        print("Jackpot! You win 10000 coins!")
        coins += 10000
    elif first_col == second_col == third_col:
        print("Triple match! You win 1000 coins!")
        coins += 1000
    elif first_col == second_col or second_col == third_col or first_col == third_col:
        print("Double match! You win 100 coins!")
        coins += 100
    else:
        print("No match! Better luck next time.")
    
    return coins

# Main game loop
print(f"Welcome! You start with {user_coins} coins.")

while True:
    user_input = input("Do you want to play? (y/n): ").lower()
    
    if user_input == 'y':
        try:
            coins_inserted = int(input("Insert your coins: "))
            if coins_inserted <= 0:
                print("Please insert a positive number of coins.")
                continue
            user_coins += coins_inserted
            
            # Check if user has enough coins to play
            if user_coins < 100:
                print("You don't have enough coins to play. Each play costs 100 coins.")
                continue
            
            # Deduct cost of one play
            user_coins -= 100
            
            # Play the slot machine
            user_coins = play_slot_machine(user_coins)
            print(f'Your remaining coins: {user_coins}')
            
            # Check if user is bankrupt
            if user_coins <= 0:
                print("Bankrupt! You have no more coins.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number of coins.")
    elif user_input == 'n':
        break
    else:
        print("Invalid choice. Please enter 'y' to play or 'n' to quit.")
        
print("Thanks for playing!")
