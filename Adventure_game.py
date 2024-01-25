start_game = input("Would you like to play the adventure game? yes/no:\n").lower().strip()

if start_game == "yes":
    character_name = input("What is your name adventurer?: ").lower().strip()
    answer = input("You approach a forest, do you follow the visible path by the trees, or take the path with fog."
                   " enter (path/fog): ").lower()
    if answer == "path":
        print("{} walks down the path with the trees, you feel like you are being watched".format(character_name))
        answer = input("You notice you are being watched by someone in a bush."
                       "do you attack the person in the bush or call out to them. enter (attack/call): ").lower()
        if answer == "attack":
            print("You attack the man charging into him and he falls back onto a tree trunk and dies")
            answer = input("You see he has a map in his hand showing the safe route out of the forest."
                           "do you take the safe route or stay to bury his body. enter (safe/bury): ").lower()
            if answer == "safe":
                print("You take the safe route out avoiding all the monsters in the woods "
                      f"you reach the town and feel safe again, well done {character_name} you win!")
            else:
                print("You attempt to bury his body, but a pack of wolves smell the blood,"
                      "the howling gets closer as a pack of wolves attack you, Game Over!")
        elif answer == "call":
            print("You call out to the man revealing his location, he instantly fires an arrow at you "
                  f"game over {character_name}, try again next time!.")
        else:
            print("Please enter a valid option next time! Game Over!.")
    elif answer == "fog":
        answer = input("You walk down the path unable to see the further you go, you hear howling in the distance,"
                       "do you defend yourself or attempt to run. enter (defend/run): ").lower()
        if answer == "run":
            print("You run in a different direction until you can see again, you see a man walking to a bush")
            answer = input("you see a pack of wolves charging towards do you hide or shout the man?"
                           "enter (hide/shout): ").lower()
            if answer == "hide":
                print("The wolves maul the man to death and take his body and leave, he drops a map "
                      f"on the floor, you take it showing you the way out! You win {character_name} well done!.")
            else:
                print("You shout over to the man to warn him but the wolves spot you too!, "
                      "they charge and kill you both game over!")
        elif answer == "defend":
            print("The wolves circle you in the fog and maul you to death! Game Over!.")

        else:
            print("Please enter a valid option next time! Game Over!.")
    else:
        print(f"Game over {character_name}, you did not pick a path")
else:
    print("Please enter yes next time to play!")
