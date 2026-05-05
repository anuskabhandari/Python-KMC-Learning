import random
num = random.randint(10,20)
print("this is random number",num)
count = 0
guess_attempts = 5

print(f"you have {guess_attempts} remaining.")
while True:
    user_num = int(input("Enter the number:"))
    count = count+1
    
    guess_attempts = guess_attempts -1
    if user_num == num:
        print("Your guess has matched in count", count)
        
        again = input("Do you want to play again?y/n ").lower()
        if again == "y":
            num = random.randint(10,20)
            count = 0
        else:
            print("Thank you for playing")
            break
        
    else:
        print("Try Againn!!!")
        print(f"your remaining attempts are {guess_attempts}")
  
    if guess_attempts == 0:
        print(f"your attempts has been finished and your random number is {num}") 
        again = input("Do you want to play again?y/n ").lower()
        if again == "y":
            num = random.randint(10,20)
            count = 0
        else:
            print("Thank you for playing")
            break   

    

