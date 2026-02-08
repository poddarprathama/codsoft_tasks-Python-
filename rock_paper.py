# rock-paper-scissors game
import random

user = input("Choose anyone from Rock,Paper and Scissors: ")
computer = random.choice(["Rock","Paper","Scissors"])
print("My choice: ",user)
print("Computer chose: ",computer)
print()
if user == "Rock" and computer == "Scissors":
    print("You won")
elif user == "Paper" and computer == "Rock":
    print("You won")
elif user == "Scissors" and computer == "Paper":
    print("You won")
elif user == computer:
    print("It's tie")
else:
    print("You lose")
again = input("Want to play again? (y/n): ")
print()
if again != "y":
    print("Game over. Thanks for playing")

