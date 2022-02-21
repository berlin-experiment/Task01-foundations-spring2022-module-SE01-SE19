# for the bot to guess a random number.
import random

# the bot "guesses" a number.
botGuess = random.randint(1, 101)
playerGuess = 0

gameState = True
firstGame = True

print("So I will guess a number between 1 and 100, you do the same. The one with the highest number wins!")

while gameState == True:
    if firstGame == True:
        # player must accept or decline with 'y' or 'n', capslock does not matter.
        reply = input("Do you wanna play the game? y/n? ").lower()
    firstGame = False

    # if the player accepts,
    if reply == "y":
        # the player picks a number and tells the bot.
        playerGuess = int(input("What is your number? "))
        if playerGuess > 100:
            print("That's not how the game works.")
            reply = input("Want to try again? y/n ")
        # the bot compares their number to the players.
        # if the bot's number is lower, it will tell the player they win.
        elif botGuess < playerGuess:
            print(f"Mine was {botGuess}, so I guess you win...")
            reply = input("Want to play again? y/n ")
            # if the bot's number is the same as the player's, the bot will say it is a draw/tie.
        elif botGuess == playerGuess:
            print("It is a draw!")
            reply = input("Want to try again? y/n ")
        # if the bot's number higher, the bot will celebrate with a mocking laugh, tell the player.
        else:
            print(f"Mine was {botGuess}. HAHA I WIN! You lose this one.")
            reply = input("Want to play again? y/n ")
    # if the player declines, the bot is sad and lashes out.
    elif reply == "n":
        print("You're lame...")
        gameState = False
        # break
    # if the player typed something other than "y" or "n", the bot is confused.
    else:
        print("I don't understand...")
        gameState = False
