import random
import os
import keyboard

# instances
instance = 1
instances = {}

class game:
    def __init__(self):

        # intro
        print("\n \nTime to play Hangman!")

        # tries
        self.tries = 10

        # letters
        self.letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

        # words
        self.words = ["apple", "banana", "cherry", "diamond", "earth",
                      "forest", "grape", "helicopter", "icepick",
                      "jumpstart", "kickbox", "lioness", "mandible",
                      "northern", "opulent", "puberty", "question",
                      "resist", "succulent", "traverse", "useful",
                      "vertical", "wonderful", "xylophone", "yellow", "zebra"]

        # answer
        self.answer = self.words[random.randint(0,len(self.words))-1]
        self.answerlist = list(self.answer.upper())

        # display progress
        self.displaylist = ["_" for x in range(len(self.answerlist))]

        # win/loss
        self.winstate = 0

    # clear console
    def clear(self):
        _ = os.system("clear")

    # display progress
    def progdisplay(self):
        for i in range(0,len(self.answerlist)):
            letter = self.answerlist[i]
            if letter in self.letters:
                pass
            else:
                self.displaylist[i] = letter
        print("\n \nTries left: " + str(self.tries))
        print("\n" + " ".join(self.displaylist))
        print("\n" + " ".join(self.letters))

    # guess letter
    def guess(self):
        global instance
        global instances
        ans = self.answer
        while self.winstate == 0:
            self.clear()
            if self.tries < 1:
                self.clear()
                self.progdisplay()
                print("\n \nYou lost! \n \n")
                self.winstate = 2
                return
            if "_" not in self.displaylist:
                self.clear()
                self.progdisplay()
                print("\n \nYou won! \n \n")
                self.winstate = 1
                return
            self.progdisplay()
            print("\n \nPlease guess a letter (if you guess a whole word, make it count! You could lose a try): ")
            x = input("[Enter /stats to see your previous wins/losses] ")
            if x == "/stats":
                self.clear()
                self.progdisplay()
                print("\n \nGame | W/L")
                for key in instances:
                    print(str(key) + (" " * (4-len(str(key)))) + " | " + str(instances[key]))
                y = input("\nPress 'Return' key to resume game")
                return self.guess()
            elif x.isalpha():
                self.progdisplay()
                if len(x) > 1:
                    if x.upper() == self.answer.upper():
                        self.clear()
                        self.letters = ["_" if y in x.upper() else y for y in self.letters]
                        self.progdisplay()
                        print("\n \nYou correctly guessed " + self.answer.upper() + "! Great job!")
                    else:
                        self.clear()
                        self.progdisplay()
                        print("\n \nYou guessed incorrectly!")
                        y = input("\nPress 'Return' key to continue")
                        self.tries -= 1
                        self.clear()
                        return self.guess()
                else:
                    if x.upper() in self.letters and x.upper() in self.answerlist:
                        self.clear()
                        self.letters = ["_" if y == x.upper() else y for y in self.letters]
                        self.progdisplay()
                        print("\n \nNice guess!")
                        y = input("\nPress 'Return' key to continue")
                    elif x.upper() in self.letters:
                        self.clear()
                        self.letters = ["_" if y == x.upper() else y for y in self.letters]
                        self.progdisplay()
                        self.tries -= 1
                        print("\n \nNope, incorrect!")
                        y = input("\nPress 'Return' key to continue")
                    else:
                        self.clear()
                        self.progdisplay()
                        print("\n \nYou already guessed that!")
                        y = input("\nPress 'Return' key to continue")
                    print("\n")
                    return self.guess()
            else:
                self.clear()
                self.progdisplay()
                print("\n \nThat is not a letter. Try again!")
                y = input("\nPress 'Return' key to continue")
                return(self.guess())
            break

# play game
while True:
    play = game()
    play.clear()
    play.__init__()
    play.guess()
    while True:
        x = input("\n \nWould you like to play again? (y/n): ")
        if x.upper() in ("Y", "N"):
            if x.upper() == "Y":
                if play.winstate < 2:
                    instances[instance] = "W"
                    instance += 1
                else:
                    instances[instance] = "L"
                    instance += 1
                play.clear()
                play.__init__()
                play.guess()
            else:
                break
        else:
            play.clear()
            print("\nPlease enter 'y' or 'n' with no quotes.")
    break
