import random

def play():
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    computer = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")

    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Run the game
print(play())
