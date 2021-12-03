#Coin Flip Betting Game 2

import random

playing = True
starting_balance = 100

#Prints welcome message and instructions
print("""Welcome to 50/50!  The game where you can bet on a coinflip!
              You have $100 to start.  Each winning wager is double the bet
              amount!  Good luck and have fun playing!""")

while playing == True:
    number = random.randint(1,2)
     #no nested loop necessary for guess. unexpected input handled in else statement.
    guess = input("Heads or Tails: ")
   
    #nested loop placed to eliminate unexpected bet input error.
    try:
        bet = int(input("Bet : $"))
    except ValueError:
        print("You must place a bet to play please try again.")
        continue
    else:
        #bet was successfully parsed exiting loop
        pass
    ledger_balance = (starting_balance - bet)

#Heads thrown and guessed
    if number == 1 and (guess == "Heads" or guess == "heads" or guess == "H" or guess == "h" or guess == "HEADS" or guess == "I AM A CODING GOD!"):
        print("You flipped a Head and guessed a Head. Winner!")
        running_total = ledger_balance + (bet *2)
        print("Current Ballance :$",running_total)
        throw = input("Do you wish to continue? Yes or No: ")
        
    #Tails thrown and guessed    
    elif number == 2 and (guess == "Tails" or guess == "tails" or guess == "T" or guess == "t" or guess == "TAILS" or guess == "I AM A CODING GOD!"):
        print("You flipped a Tail and guessed a Tail. Winner!")
        running_total = ledger_balance + (bet *2)
        print("Current Ballance :$",running_total)
        throw = input("Do you wish to continue? Yes or No: ")

    #Heads thrown Tails guessed
    elif number == 1 and (guess == "Tails" or guess == "tails" or guess == "T" or guess == "t" or guess == "TAILS"):
        print("You flipped a Head and guessed a Tail. Unlucky")
        running_total = ledger_balance
        print("Current Ballance :$",running_total)
        throw = input("Do you wish to continue? Yes or No: ")
        
    #Tails thrown Heads is guessed
    elif number == 2 and (guess == "Heads" or guess == "heads" or guess == "H" or guess == "h" or guess == "HEADS"):
        print("You flipped a Tail and guessed a Head. Unlucky ")
        running_total = ledger_balance
        print("Current Ballance :$",running_total)
        throw = input("Do you wish to continue? Yes or No: ")
        
    else:
        print("You have entered an incorrect value.")
        throw = input("Do you wish to try again? Yes or No: ")
   
    #if bet <= 1:
     #   print("You must place a bet! Would you like to try again?")
     #   throw = input("Yes or No: ")
        
    #elif bet > running_total:
     #   print("You do not have enough money")
     #   throw = input("Do you wish to try again? Yes or No: ")
    
    if (throw == "yes" or throw == "Yes" or throw == "Y" or throw == "y"):
        playing = True
        starting_balance = running_total
    elif (throw == "no" or throw == "No" or throw == "N" or throw == "n") and running_total >= starting_balance:
        playing = False
        print("You turned $100 into $",running_total, "Great job! See you next time!")
    elif (throw == "no" or throw == "No" or throw == "N" or throw == "n") and running_total < starting_balance:
        playing = False
        print("You turned $100 into $",running_total, "You suck!")