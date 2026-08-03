import random

while True:
    input("Press Enter to roll the dice...")

    dice = random.randint(1, 6)
    print("You rolled:", dice)

    play_again = input("Roll again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
