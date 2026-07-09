import random

print("========== ROCK PAPER SCISSORS ==========")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice: ").lower()

    if user_choice == "1":
        user_choice = "rock"
    elif user_choice == "2":
        user_choice = "paper"
    elif user_choice == "3":
        user_choice = "scissors"

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Congratulations! You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore")
    print("You:", user_score)
    print("Computer:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("\nThank you for playing!")
        break