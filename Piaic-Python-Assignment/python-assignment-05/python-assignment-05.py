import random  
def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0
    
    #Total Round
    rounds = 5
    for round_number in range(1, rounds + 1):
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"\nRound {round_number}")
        print(f"Your number is {int(player_number)}") 

        guess = str(input("Do you think your number is higher or lower than the computer's?: ")).strip().lower()
        
    
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print(f"You were right! The computer's number was {int(computer_number)}")  
            score += 1 
        else:
            print(f"Aww, that's incorrect. The computer's number was {int(computer_number)}")  
        
        print(f"Your score is now {int(score)}") 

    print("\nThanks for playing!")
    
high_low_game()
