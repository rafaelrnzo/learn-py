import tkinter as tk
from tkinter import messagebox
import random

# Function to create a deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'suit': suit, 'value': value} for suit in suits for value in values]
    random.shuffle(deck)
    return deck

# Function to calculate the value of a hand
def hand_value(hand):
    value = 0
    num_aces = 0
    
    for card in hand:
        if card['value'] in ['J', 'Q', 'K']:
            value += 10
        elif card['value'] == 'A':
            num_aces += 1
            value += 11
        else:
            value += int(card['value'])
    
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    
    return value

# Update the UI with the current hand
def update_hand_display(hand, owner):
    hand_text = f"{owner}'s hand: "
    for card in hand:
        hand_text += f"{card['value']} of {card['suit']}; "
    hand_text += f"(Value: {hand_value(hand)})"
    if owner == "Player":
        player_hand_label.config(text=hand_text)
    else:
        dealer_hand_label.config(text=hand_text)

# Function to handle player's turn
def player_hit():
    global player_hand
    player_hand.append(deck.pop())
    update_hand_display(player_hand, "Player")
    if hand_value(player_hand) > 21:
        messagebox.showinfo("Game Over", "Bust! You lose.")
        disable_buttons()
    elif hand_value(player_hand) == 21:
        messagebox.showinfo("Blackjack", "Blackjack! You win!")
        disable_buttons()

def player_stand():
    global dealer_hand
    update_hand_display(dealer_hand, "Dealer")
    while hand_value(dealer_hand) < 21:
        dealer_hand.append(deck.pop())
        update_hand_display(dealer_hand, "Dealer")
    
    dealer_value = hand_value(dealer_hand)
    player_value = hand_value(player_hand)

    if dealer_value > 21:
        messagebox.showinfo("Game Over", "Dealer busts! You win!")
    elif dealer_value > player_value:
        messagebox.showinfo("Game Over", "Dealer wins!")
    elif dealer_value < player_value:
        messagebox.showinfo("Game Over", "You win!")
    else:
        messagebox.showinfo("Game Over", "It's a tie!")
    disable_buttons()

def disable_buttons():
    hit_button.config(state=tk.DISABLED)
    stand_button.config(state=tk.DISABLED)

def new_game():
    global deck, player_hand, dealer_hand
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    update_hand_display(player_hand, "Player")
    update_hand_display(dealer_hand, "Dealer")
    
    hit_button.config(state=tk.NORMAL)
    stand_button.config(state=tk.NORMAL)

# Initialize main window
root = tk.Tk()
root.title("Blackjack")

# Initialize deck and hands
deck = create_deck()
player_hand = []
dealer_hand = []

# UI Elements
title_label = tk.Label(root, text="Welcome to Blackjack!", font=("Arial", 16))
title_label.pack(pady=10)

player_hand_label = tk.Label(root, text="", font=("Arial", 14))
player_hand_label.pack(pady=5)

dealer_hand_label = tk.Label(root, text="", font=("Arial", 14))
dealer_hand_label.pack(pady=5)

hit_button = tk.Button(root, text="Hit", command=player_hit)
hit_button.pack(side=tk.LEFT, padx=20, pady=20)

stand_button = tk.Button(root, text="Stand", command=player_stand)
stand_button.pack(side=tk.RIGHT, padx=20, pady=20)

new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.pack(pady=20)

# Start new game on launch
new_game()

# Run the application
root.mainloop()
