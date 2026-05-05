import random

user_score = 0
computer_score=0

while True:
    num = random.randint(10,20)
    print("Guess number between 10 to 20")

    user_attempts =5
    user_count =0

    while user_attempts>0:
        user_num = int(input("Enter your guess:"))
        user_count +=1
        user_attempts -=1

        if user_num ==num:
            print("User guess has matched in count", user_count)
            break

        else:
            print("Try again ! Remaining: ", user_attempts)

    if user_num == num:
        user_score += 5
    else:
        computer_score +=5    

# ---- computer----#
    computer_attempts =5
    computer_count =0

    while user_attempts>0:
        computer_num = int(input("Enter computer guess:"))
        computer_count +=1
        computer_attempts -=1

        if computer_num ==num:
            print("Computer guess has matched in count", computer_count)
            break

        else:
            print("Try again ! Remaining: ", user_attempts)

    if computer_num == num:
        computer_score += 5
    else:
        user_score +=5    

