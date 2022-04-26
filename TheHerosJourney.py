"""
CPS109-11 Assignment 1
A program that is a Text-based adventure game
@author Viet Hoang
@date Oct 19th, 2021

Description:
Ever since the beginning of time, this problem has plagued all of humanity. Some describe it as a feeling worse than
suffering. This issue is known as "Boredom". During the Covid-19 pandemic of 2019, everyone was told to stay indoors
and was forced to isolate themselves from everyone else. As a result, it led to a surge in "Boredom" cases all around
the world. People left and right were feeling non-stop boredom.

This program is a text-based adventure game featuring fantasy RPG elements alongside with turn based combat and as
well as allowing the user to make some choices in how they want to progress with their adventure. This program
attempts to solve the problem of "Boredom" by trying to entertain the user (est playtime to be around 10-20 mins)

resources used: https://www.asciiart.eu/mythology/devils (Ascii art of the Demon Lord by eViL)
"""
import random
import time


def startGame():
    """
    Ask the use if they want to start the game.
    """
    inStart = ""
    inStart = str(input("Would you like to start the game? (1 = yes, 2 = no): ")).strip()

    # to account if the user doesn't type in 1 or 2
    while inStart != "1" and inStart != "2":
        inStart = str(input("A valid input was not entered. Would you like to start the game? (1 = yes, 2 = no): " +
                            "")).strip()

    if inStart == "1":
        return True

    else:
        return False


def wait3():
    time.sleep(1.3)


def intro(nameHero):
    """
    Plays out the intro of the game and introduces the user to the fantasy world.
    """
    # to imitating a loading screen
    print("loading intro", end="")
    time.sleep(1)
    dot = "..."
    for i in dot:
        print(i, end="")
        time.sleep(0.333)

    print()
    print()
    print()

    print("######################################")
    time.sleep(0.5)
    print("|                                    |")
    time.sleep(0.5)
    print("|         The Hero's Journey         |")
    time.sleep(0.5)
    print("|                                    |")
    time.sleep(0.5)
    print("######################################")

    print()
    print()
    time.sleep(1)
    print("Year: 1350")
    time.sleep(1.5)
    print("There lived a village in the outskirts of the Astodia Kingdom.")
    wait3()
    print("The village was considered to be mankind's last stand against the Demon Lord.")
    wait3()
    print("You see five years ago, the Demon Lord launched an all out attack upon the Astodia Kingdom.")
    wait3()
    print("However the Astodia Kingdom was unable to fend off against the Demon Lord's assault.")
    wait3()
    print("And with that, the Astodia Kingdom fell into the hands of the Demon Lord.")
    wait3()
    print("The village composes of the remaining survivors that were able to escape during the attack.")
    wait3()
    print(f"{nameHero} was one of the survivors that were able to escape but unfortunately, the same couldn't have been"
          f" said about their family.")
    wait3()
    print(f"{nameHero} vowed that once they reached level 18, they'd set off to the forest heading to the old ruins "
          f"of the Astodia Kingdom to find and kill the Demon Lord.")
    wait3()
    print(f"{nameHero} will start training today to become stronger.")
    wait3()
    print(f"So {nameHero} decided to exist their house.")


def demonLordIntro(nameHero):
    """
    plays the demon lord's intro
    """
    time.sleep(1)
    print(f"\n{nameHero} carefully enters castle of the ruin Kingdom.")
    wait3()
    print(f"So far, {nameHero} could see no sign of life at all. Perhaps the Demon lord had abandoned this place.")
    wait3()
    print(f"As soon as that thought crossed their mines, a loud explosion occurred at the end of the hallway.")
    wait3()
    print(f"As the smoke started to clear, {nameHero} could see a shadowy figure begin to emerge")
    wait3()
    print("                            ,-.")
    time.sleep(0.5)
    print("       ___,---.__          /'|`\          __,---,___")
    time.sleep(0.5)
    print("    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.")
    time.sleep(0.5)
    print("  ,'        |           ~'\     /`~           |        `.")
    time.sleep(0.5)
    print(" /      ___//              `. ,'          ,  , \___      \\")
    time.sleep(0.5)
    print("|    ,-'   `-.__   _         |        ,    __,-'   `-.    |")
    time.sleep(0.5)
    print("|   /          /\_  `   .    |    ,      _/'\          \   |")
    time.sleep(0.5)
    print("\  |           \ \`-.___ \   |   / ___,-'/  /           |  /")
    time.sleep(0.5)
    print(" \  \           | `._   `\\\  |  //'\033[36m0\033[0m  _,' |           /  /")
    time.sleep(0.5)
    print("  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'")
    time.sleep(0.5)
    print("     ``       /     \    ,='/ \`=.    /     \       ''")
    time.sleep(0.5)
    print("             |__   /|\_,--.,-.--,--._/|\   __|")
    time.sleep(0.5)
    print("             /  `./  \\\`\ |  |  | /,//' \,'  \\")
    time.sleep(0.5)
    print("            /   /     ||--+--|--+-/-|     \   \\")
    time.sleep(0.5)
    print("           |   |     /'\_\_\ | /_/_/`\     |   |")
    time.sleep(0.5)
    print("            \   \__, \_     `~'     _/ .__/   /")
    time.sleep(0.5)
    print("             `-._,-'   `-._______,-'   `-._,-'")
    print()
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    print("There stood the Demon Lord. The same one that launch the attack upon this Kingdom all those years ago.")
    wait3()
    print(f"Neither {nameHero} nor the Demon Lord exchanged any words. For they both knew that only one of them was "
          f"leaving here alive.")
    wait3()


def outro(heroName, totalKills):
    """
    plays the outro
    """
    print("And with that, the Demon Lord was dead.")
    wait3()
    print("                            ,-.")
    print("       ___,---.__          /'|`\          __,---,___")
    print("    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.")
    print("  ,'        |           ~'\     /`~           |        `.")
    print(" /      ___//              `. ,'          ,  , \___      \\")
    print("|    ,-'   `-.__   _         |        ,    __,-'   `-.    |")
    print("|   /          /\_  `   .    |    ,      _/'\          \   |")
    print("\  |           \ \`-.___ \   |   / ___,-'/  /           |  /")
    print(" \  \           | `._   `\\\  |  //'X  _,' |           /  /")
    print("  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'")
    print("     ``       /     \    ,='/ \`=.    /     \       ''")
    print("             |__   /|\_,--.,-.--,--._/|\   __|")
    print("             /  `./  \\\`\ |  |  | /,//' \,'  \\")
    print("            /   /     ||--+--|--+-/-|     \   \\")
    print("           |   |     /'\_\_\ | /_/_/`\     |   |")
    print("            \   \__, \_     `~'     _/ .__/   /")
    print("             `-._,-'   `-._______,-'   `-._,-'")
    print()
    print()
    wait3()
    print(f"There lied the corpse of the Demon Lord.")
    wait3()
    print(f"{heroName} had done it and now they can finally get their well deserved rest.")
    print(f"End game stats\nLvl: {level} | HP: \033[1;31;40m{curHealth}/{maxHealth}\033[0m | ATK: {attack} | DEF: "
          f"{defence} | $: {gold} g | EXP: {experience}/{reqExperience}\n"
          f"\nTotal kills: {totalKills}\n")


def playAgain():
    """
    asks the user if they would like to play again
    """
    inAgain = ""
    inAgain = str(input("\nCongrats on beating the game. I hope that this game was able to entertain you for a while."
                        "\nWould you like play again? (1 = yes, 2 = no): ")).strip()

    # to account if the user doesn't type in "1" or "2"
    while inAgain != "1" and inAgain != "2":
        inAgain = str(input("A valid input was not entered. Would you like play again? (1 = yes, 2 = no): ")).strip()

    if inAgain == "1":
        return True

    else:
        return False


if __name__ == "__main__":

    game = startGame()

    while game:

        name = ""
        name = str(input("Please enter the name of the hero: "))

        intro(name)

        # Hero starting stats
        level = 1
        maxHealth = 10 + (level * 5)
        curHealth = maxHealth
        attack = 5 + (level * 2)
        defence = level * 3
        gold = 10
        experience = 0
        reqExperience = 10 + int(level * 1.5)
        kills = 0

        # Shop item variables
        smallSword = 1
        normalSword = 1
        bigSword = 1
        rustyArmor = 1
        standardArmor = 1
        strongArmor = 1

        # Enemy starting stats
        enemyType = ["Enemy Skeleton", "Enemy Goblin", "Enemy Slime", "Giant Enemy Spider"]
        enemyLevel = level
        enemyMaxHealth = int(maxHealth * (4 / 5))
        enemyAttack = attack // 2

        # Loop that causes the player to always return back to the village
        inVillageArea = True
        while inVillageArea:

            # shows the player stats to the user
            print("-----------------------------------------------")
            print(f"\n{name}'s stats\nLvl: {level} | HP: \033[1;31;40m{curHealth}/{maxHealth}\033[0m | ATK: {attack} | "
                  f"DEF: {defence} | $: {gold} g | EXP: {experience}/{reqExperience}")

            inP = ""
            # gives the user the option to pick where to go
            inP = str(input(f"\n{name} is in the Village. What should they do?\n"
                            f"1) Enter the shop\n"
                            f"2) Sleep at the inn (heals to full hp but -2 gold per night)\n"
                            f"3) Venture into the forest towards the Astodia Kingdom\n"
                            f"\nEnter a choice (1,2,3): ")).strip()

            # checking valid inputs
            while inP != "1" and inP != "2" and inP != "3":
                inP = str(input(f"\n\033[1;31;40mA valid choice was not chosen, please enter a valid choice.\033[0m\n"
                                f"1) Enter the shop\n"
                                f"2) Rest at the inn (heals to full hp cost -2 gold per night)\n"
                                f"3) Venture into the forest towards the Astodia Kingdom\n"
                                f"\nEnter a choice (1,2,3): ")).strip()

            # the entire code for the shop (the items themselves only give the user a stat boost)
            if inP == "1":
                print("-----------------------------------------------")
                inPShop = ""
                inPShop = str(input(f"\n{name} enters the shop and sees that it has the following items on display.\n"
                                    f"Swords\n"
                                    f"1) {smallSword} small sword (cost 20 gold, +5 attack)\n"
                                    f"2) {normalSword} normal sword (cost 40 gold, +15 attack)\n"
                                    f"3) {bigSword} big sword (cost 100 gold, +45 attack)\n"
                                    f"\n"
                                    f"Armors\n"
                                    f"4) {rustyArmor} rusty armor (cost 20 gold, +5 defence)\n"
                                    f"5) {standardArmor} standard armor (cost 40 gold, +15 defence)\n"
                                    f"6) {strongArmor} strong armor (cost 100 gold, +45 defence\n"
                                    f"7) Exit\n"
                                    f"\nEnter a choice (1,2,3,4,5,6,7): ")).strip()

                # checking valid inputs
                while inPShop != "1" and inPShop != "2" and inPShop != "3" and inPShop != "4" and inPShop != "5" and \
                        inPShop != "6" and inPShop != "7":
                    inPShop = str(input(f"\n\033[1;31;40mA valid choice was not chosen, please enter a valid choice."
                                        f"\033[0m\n"
                                        f"Swords\n"
                                        f"1) {smallSword} small sword (cost 20 gold, +5 attack)\n"
                                        f"2) {normalSword} normal sword (cost 40 gold, +15 attack)\n"
                                        f"3) {bigSword} big sword (cost 100 gold, +45 attack)\n"
                                        f"\n"
                                        f"Armors\n"
                                        f"4) {rustyArmor} rusty armor (cost 20 gold, +5 defence)\n"
                                        f"5) {standardArmor} standard armor (cost 40 gold, +15 defence)\n"
                                        f"6) {strongArmor} strong armor (cost 100 gold, +45 defence\n"
                                        f"7) Exit\n"
                                        f"\nEnter a choice (1,2,3,4,5,6,7): ")).strip()

                # shop system where after buying an item, it no longer becomes available.
                if inPShop == "1" and smallSword == 1:
                    if gold < 20:
                        print(f"It seems that {name} can't afford to buy the small sword and decided to exit the shop.")

                    else:
                        print(f"{name} has bought the small sword \033[1;31;40m(+5 attack).\033[0m")
                        gold -= 20
                        attack += 5
                        smallSword = 0

                elif inPShop == "2" and normalSword == 1:

                    if gold < 40:
                        print(
                            f"It seems that {name} can't afford to buy the normal sword and decided to exit the shop.")

                    else:
                        print(f"{name} has bought the normal sword \033[1;31;40m(+15 attack).\033[0m")
                        gold -= 40
                        attack += 15
                        normalSword = 0

                elif inPShop == "3" and bigSword == 1:

                    if gold < 100:
                        print(f"It seems that {name} can't afford to buy the big sword and decided to exit the shop.")

                    else:
                        print(f"{name} has bought the big sword \033[1;31;40m(+45 attack).\033[0m")
                        gold -= 100
                        attack += 45
                        bigSword = 0

                elif inPShop == "4" and rustyArmor == 1:

                    if gold < 20:
                        print(f"It seems that {name} can't afford to buy the rusty armor and decided to exit the shop.")

                    else:
                        print(f"{name} has bought the rusty armor \033[1;31;40m(+5 defence).\033[0m")
                        gold -= 20
                        defence += 5
                        rustyArmor = 0

                elif inPShop == "5" and standardArmor == 1:

                    if gold < 40:
                        print(f"It seems that {name} can't afford to buy the standard armor and decided to exit the "
                              f"shop.")
                    else:
                        print(f"{name} has bought the standard armor \033[1;31;40m(+15 defence).\033[0m")
                        gold -= 40
                        defence += 15
                        standardArmor = 0

                elif inPShop == "6" and strongArmor == 1:

                    if gold < 100:
                        print(
                            f"It seems that {name} can't afford to buy the strong armor and decided to exit the shop.")

                    else:
                        print(f"{name} has bought the strong armor \033[1;31;40m(+45 defence).\033[0m")
                        gold -= 100
                        defence += 45
                        strongArmor = 0

                elif inPShop == "7":

                    print(f"{name} decided to exit the shop.")

                else:
                    print(f"\nIt seems that the item is out of stock. So {name} decided to leave.\n")

            # The entire code for the inn
            elif inP == "2":
                print("-----------------------------------------------")

                # this pity system is here so that the user doesn't get soft locked in the game (for being at 1 hp and
                # being unable to get any gold drops from the enemy.
                pity = random.randint(1, 5)

                if curHealth == maxHealth:
                    print(f"\n{name} is already at full health and doesn't need to rest.\n")

                elif gold < 2 and pity == 1:
                    print(f"\nIt seems that {name} can't afford to sleep at the inn.\nHowever, it seems that the inn "
                          f"keeper felt bad for {name} for being soo poor so they decided to let them stay a night for "
                          f"free.\n")

                    curHealth = maxHealth

                # wanted to give the user a "hint" that there's be pity system
                elif gold < 2:
                    print(f"\nIt seems that {name} can't afford to sleep at the inn. Maybe if {name} "
                          f"\n\033[1;31;40mbegs enough times\033[0m, the inn keeper might let them stay a night for "
                          f"free.\n")

                else:
                    print(f"\n{name} decided to rest at the inn for one night (+full health recovered).\n")
                    gold -= 2
                    curHealth = maxHealth

            # entire code the forest area which includes the combat system as well as the exp and gold gain system
            else:
                print("-----------------------------------------------")
                print(f"\n{name} has decided to venture into the forest to head to the ruin Kingdom of Astodia.")

                inForestArea = True

                while inForestArea:

                    # Generates random enemy with random stats
                    enemyCurHealth = random.randint(2, enemyMaxHealth)
                    curEnemyType = random.choice(enemyType)

                    print(f"\n\033[1;31;40m# {curEnemyType} has appeared! #\033[0m")

                    # the turn base combat system
                    while enemyCurHealth > 0:
                        inFighting = ""
                        inFighting = str(input(f"\n{name}'s HP: \033[1;31;40m{curHealth}\033[0m\n"
                                               f"{curEnemyType}'s HP: {enemyCurHealth}\n"
                                               f"\n"
                                               f"1) Attack the {curEnemyType}\n"
                                               f"2) Run away\n"
                                               f"What should {name} do? (1,2): ")).strip()

                        # checking valid inputs
                        while inFighting != "1" and inFighting != "2":
                            inFighting = str(input(f"\n\033[1;31;40mA valid choice was not chosen, please enter a "
                                                   f"valid choice. \033[0m\n"
                                                   f"\n{name}'s HP: \033[1;31;40m{curHealth}\033[0m\n"
                                                   f"{curEnemyType}'s HP: {enemyCurHealth}\n"
                                                   f"\n"
                                                   f"1) Attack the {curEnemyType}\n"
                                                   f"2) Run away\n"
                                                   f"What should {name} do? (1,2): ")).strip()

                        # for when the user chooses to fight
                        if inFighting == "1" and curHealth > 0:
                            print("-----------------------------------------------")

                            # generates a random battle stat (the user and the "enemy" attacks at the same time)
                            damageDealt = random.randint(attack - 2, attack + 2)
                            damageTaken = int(random.randint(1, enemyAttack) * ((100 - defence) / 100))

                            curHealth -= damageTaken
                            enemyCurHealth -= damageDealt

                            # displays damage results to the user
                            print(f"\n{name} strikes the {curEnemyType} for {damageDealt} damage.\n"
                                  f"{name} receives {damageTaken} damage in retaliation!\n")

                            # the "death" system (note: that I made it so that the user can't really die)
                            if curHealth <= 0:
                                print(f"\n\033[1;31;40mOh it would seem that {name} has taken too much damage and has "
                                      f"to run away!\033[0m\n")
                                inForestArea = False
                                curHealth = 1
                                break

                        else:
                            inForestArea = False
                            print(f"{name} has decided to run away.")
                            break

                        # after the user wins a battle while also being alive
                        if enemyCurHealth <= 0:

                            # Randomly generates the exp and gold earned based on the enemy level
                            expGain = random.randint((enemyLevel // 2) + 1, enemyLevel + 2)
                            goldGain = random.randint((enemyLevel // 2) + 1, enemyLevel + 5)

                            experience += expGain
                            gold += goldGain

                            # for leveling up the player
                            if experience >= reqExperience:
                                print(f"\n\033[1;31;40mWow {name} has leveled up to level {level + 1} (HP will be "
                                      f"refreshed to max)\033[0m\n")

                                level += 1
                                maxHealth += (level * 5)
                                curHealth = maxHealth
                                attack += level * 2
                                defence += 2

                                # Because I made my defence represent a percentage, I didn't want the player to get
                                # to the point there they would take 0 damage.
                                if defence > 99:
                                    defence = 99

                                experience = 0
                                reqExperience = 10 + int(level * 1.5)

                                # I wanted to make the enemies to somewhat scale with the player as well.
                                enemyLevel = level
                                enemyMaxHealth += int(level * enemyLevel)
                                enemyAttack += attack // 4

                            kills += 1
                            print("-----------------------------------------------")

                            # if the user wants to continue grinding in the forest
                            inPContinueFighting = str(input(f"\n{name} has defeated the {curEnemyType}\n"
                                                            f"\nGold Gain: {goldGain}\n"
                                                            f"EXP gains: {expGain}\n"
                                                            f"| $: {gold} g | EXP: {experience}/{reqExperience}\n"
                                                            f"\nWould you like to continue exploring? (1 = yes, 2 = no)"
                                                            f": ")).strip()

                            # checks for valid inputs
                            while inPContinueFighting != "1" and inPContinueFighting != "2":
                                inPContinueFighting = str(input(f"\n\033[1;31;40mA valid choice was not chosen, "
                                                                f"please enter a valid choice. \033[0m\n"
                                                                f"\nWould you like to continue exploring? (1 = yes, 2 ="
                                                                f" no): ")).strip()

                            if inPContinueFighting == "2":
                                inForestArea = False

            # after a certain condition (this being once the user reaches lvl 18 and over), I wanted to give the user
            # the option to fight the boss
            if level > 17:
                fightBoss = ""
                print(f"\n{name}'s stats\nLvl: {level} | HP: \033[1;31;40m{curHealth}/{maxHealth}\033[0m | ATK: "
                      f"{attack} | DEF: {defence} | $: {gold} g | EXP: {experience}/{reqExperience}")

                fightBoss = str(input(f"\nAs {name} was exploring through the forest, {name} was able to discover the "
                                      f"old ruin Kingdom of Astodia that's now being ruled over by the Demon Lord.\n"
                                      f"Should {name} fight with the Demon Lord now? (\033[1;31;40mYOU CANNOT "
                                      f"GO BACK ONCE YOU HAVE SAID YES\033[0m) (1 = no, 2 = yes): ")).strip()

                # checks for invalid inputs
                while fightBoss != "1" and fightBoss != "2":
                    fightBoss = str(input(f"\nA valid choice was not chosen, please enter a valid choice.\n"
                                          f"Should {name} fight with the Demon Lord now? (\033[1;31;40mYOU CANNOT "
                                          f"GO BACK ONCE YOU HAVE SAID YES\033[0m) (1 = no, 2 = yes): ")).strip()

                if fightBoss == "2":
                    inVillageArea = False

        demonLordIntro(name)

        demonLordHealth = 99999
        demonLordAttack = 9999

        print("\033[36mThe Demon Lord has appeared\033[0m")

        print(f"Demon Lord's stats\nlvl: ??? | HP: {demonLordHealth} | ATK: {demonLordAttack} | DEF: ???")

        deathCounter = 0
        cutScene = 0

        # basically just the same combat system as the forest area but this time for the final boss
        while demonLordHealth > 0:
            print("-----------------------------------------------")

            # just the standard "press a button to attack" combat system.
            inFightingBoss = str(input(f"\n{name}'s HP: \033[1;31;40m{curHealth}\033[0m\n"
                                       f"Demon Lord's HP: {demonLordHealth}\n"
                                       f"\n"
                                       f"ATTACK) Attack the Demon Lord: (press enter to attack)")).strip()

            # combat stat calculator
            damageDealt = random.randint(attack - 2, attack + 2)
            damageTaken = int(random.randint(1, demonLordAttack) * ((100 - defence) / 100))

            curHealth -= damageTaken
            demonLordHealth -= damageDealt

            print(f"\n{name} strikes the Demon Lord for {damageDealt} damage.\n"
                  f"{name} receives {damageTaken} damage from the Demon Lord in retaliation!\n")

            if demonLordHealth <= 0:
                curHealth = 1
                kills += 1
                outro(name, kills)

            # this fight was a rigged auto win
            elif curHealth <= 0 and deathCounter == 0:
                deathCounter += 1
                print(f"\033[31m\n{name}, in their heaving last stand begins to feel tired, almost like there's a "
                      f"mountain on their back.\033[0m\n")
                wait3()
                print(f"\033[31mBut then {name} starts to remember. They remember all the evil the Demon Lord has done."
                      f"\033[0m")
                wait3()
                print(f"\033[31m{name} remembers all the deaths the Demon Lord has caused.\033[0m")
                wait3()
                print(f"\033[31m{name} remembers the vow that they made.\033[0m")
                wait3()
                print(f"\033[31mAnd with that, {name} refuses to give up.\033[0m")

                curHealth = 1
                attack = 9999

            elif curHealth <= 0 and deathCounter > 0:

                print(f"\033[31mbut {name} refuses to give up.\033[0m")

                curHealth = 1

            if curHealth < maxHealth * (1 / 4) and cutScene == 2:
                print(f"\033[31m{name} has now received some major damage and isn't sure if they can continue with "
                      f"this.\033[0m")
                cutScene = 3

            elif curHealth < maxHealth * (2 / 4) and cutScene == 1:
                print(f"\033[31m{name} is starting to lose their breath.\033[0m")
                cutScene = 2

            elif curHealth < maxHealth * (3 / 4) and cutScene == 0:
                print(f"\033[31m{name} starts to bleed a little from the damage taken. But they know that they mustn't "
                      f"give up.\033[0m")
                cutScene = 1

        game = playAgain()
