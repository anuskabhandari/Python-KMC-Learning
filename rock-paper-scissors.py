import random

choices = [ "rock", "paper", "scissor"]

while True:
    user = input("Enter rock , paper , ors scissors (or 'quit' to stop):").lower()

    if user not in choices:
        print("Invalid choice try again")
        continue

    computer = random.choice(choices)
    print("Computer chose",computer)

    if user==computer:
        print("Its a tie!")

    elif :
        (user == "rock" and computer =="scissors") or \
        (user == "rock" and computer =="scissors") or \
        (user == "rock" and computer =="scissors")