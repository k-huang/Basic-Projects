#Word Blitz by Kaiwen Huang, 10191912, last modified July 9th, 2018

# This program allows the user to play a game of Word Blitz
# against another player or the computer. The text file is assumed to be in the
# same directory as Assignment1_KaiwenhuangCISC121.py

# Importing the sys and random modules
import random
import sys

# This function is the overall main game function, it initiates a game of
# Wordblitz, the rules as described in the assignment 1 requirements

def wordblitz():
    print("Welcome to Word Blitz")
    name1 = input("Please enter player 1's name: ")
    name2 = input("Please enter player 2's name: ")
    wordandclue = puzzleget()
    word = wordandclue['secretword']
    gameover = False
    guessedletters = []
    score1 = 0
    score2 = 0
    turnscore1 = 0
    turnscore2 = 0
    player1turn = True
    # This loop runs until a game-ending move is made: the word revealed or guessed
    while gameover == False:
        hangedman = hangman(word, guessedletters)
        if hangedman.replace(' ','').split() == list(word.replace(' ', '')):
            gameover == True
        # The following code shows the game balance, turn balance,
        #state of the secret word, guessed letters, and the category.
        print("_"*80 + "\n")
        print("The category for this game is:", wordandclue['category'])
        print("The secret word is:", hangedman,"         Guessed letters:",
        ' '.join(guessedletters))
        print(name1 + "'s game balance:", score1,'            ', name2\
        +"'s game balance:", score2)
        print(name1 + "'s turn balance:", turnscore1,'            ', name2\
        +"'s turn balance:", turnscore2)
        # The conditional determines who's turn it is and whose player turn code
        # to run.
        if player1turn == True:
            movemade = pickamove(name1)
            # This code represents player 1 guessing a consonant and spinning
            # the wheel
            if movemade == 1:
                spun = spinthewheel(name1)
                if spun == 0:
                    turnscore1 = 0
                    print(name1 + "'s turn ends. It is now",\
                    name2 + "'s turn.")
                    player1turn = False
                elif spun == 21:
                    score1 += turnscore1
                    turnscore1 = 0
                    print(name1 + "'s turn ends. It is now",\
                    name2 + "'s turn.")
                    player1turn = False
                else:
                    con = getcon(guessedletters)
                    earnings = isconinword(word, con, spun)
                    if earnings == 0:
                        score1 += turnscore1
                        turnscore1 = 0
                        print(con, "is not part of the word.", name1 + "'s turn ends. It is now",\
                        name2 + "'s turn.")
                        player1turn = False
                    else:
                        turnscore1 += earnings
                        print (con,"was in the word.", name1,\
                        'has won', earnings, 'Dollars,', name1 + "'s turn continues.\n")
                    guessedletters.append(con)
            # This code represents player 1 buying a vowel
            elif movemade == 2:
                turnscore1 -= 25
                vowel = getvow(guessedletters,name1)
                isit = isvowinword(word,vowel,name1,name2)
                if isit:
                    player1turn = True
                else:
                    score1 += 0
                    turnscore1 = 0
                    player1turn = False
                guessedletters.append(vowel)
            # This code represents player 1 guessing the word
            elif movemade == 3:
                wordguess = input("Guess the word: ")
                if wordguess.lower() == word:
                    leftmoney = hangedman.count('_')*5
                    print(name1, "guessed the word correctly!",name1,\
                    "has earned", leftmoney, "dollars.")
                    turnscore1 += leftmoney
                    score1 += turnscore1
                    gameover = True
                else:
                    print("Unfortunately,", name1, "guessed incorrectly.",\
                    name1 + "'s turn is over. It is now",\
                    name2 + "'s turn.")
                    score1 += turnscore1
                    turnscore1 = 0
                    player1turn = False
            # This code exits the function if player 1 quits the game
            else:
                print(name1,'has quit the game. Remember,', name1 +\
                ", quitters never win, and winners never quit. Goodbye!")
                sys.exit()
# This code block represents player2's turn
        else:
            movemade = pickamove(name2)
            # This code represents player 2 guessing a consonant and spinning
            # the wheel
            if movemade == 1:
                spun = spinthewheel(name2)
                if spun == 0:
                    turnscore2 = 0
                    player1turn = True
                elif spun == 21:
                    score2 += turnscore2
                    turnscore2 = 0
                    print(name2 + "'s turn ends. It is now",\
                    name1 + "'s turn.")
                    player1turn = True
                else:
                    con = getcon(guessedletters)
                    earnings = isconinword(word, con, spun)
                    if earnings == 0:
                        score2 += turnscore2
                        turnscore2 = 0
                        print(con, "is not part of the word.", name2 + "'s turn ends. It is now",\
                        name1 + "'s turn.")
                        player1turn = True
                    else:
                        turnscore2 += earnings
                        print (con,"was in the word.", name2,\
                        'has won', earnings, 'Dollars,', name2 + "'s turn continues.\n")
                    guessedletters.append(con)
            # This code represents player 2 buying a vowel
            elif movemade == 2:
                turnscore2 -= 25
                vowel = getvow(guessedletters,name2)
                isit = isvowinword(word,vowel,name2,name1)
                if isit:
                    player1turn = False
                else:
                    score2 += turnscore2
                    turnscore2 = 0
                    player1turn = True
                guessedletters.append(vowel)
            # This code represents player 2 guessing the word
            elif movemade ==3:
                wordguess = input("Guess the word: ")
                if wordguess.lower() == word:
                    leftmoney = hangedman.count('_')*5
                    print(name2, "guessed the word correctly!",name2,\
                    "has earned", leftmoney, "dollars.")
                    turnscore2 += leftmoney
                    score2 += turnscore2
                    gameover = True
                else:
                    score2 += turnscore2
                    turnscore2 = 0
                    print("Unfortunately,", name2, "guessed incorrectly.",\
                    name2 + "'s turn is over. It is now",\
                    name1 + "'s turn.")
                    player1turn = True
            # This code exits the function if player 2 quits the game
            else:
                print(name2,'has quit the game. Remember,', name2 +\
                ", quitters never win, and winners never quit. Goodbye!")
                sys.exit()
    # This block of code prints the ending statements and winner, as well as
    # the final game balance
    print("The word has been revealed. It was", word)
    print('_'*80)
    print("\n" + name1 + "'s final game balance was $" + str(score1),'.         ',\
      name2 +"'s final game balance was $" + str(score2) + ".\n")
    if score1>score2:
        print("Congratulations", name1 + "! You've won!")
    elif score2>score1:
        print("Congratulations", name2 + "! You've won!")
    else:
        print("It was a real nailbiter, but it was a tie in the end.",\
        "Congratulations", name1 ,"and", name2 + "!")

# This function gets a valid move input from the player and returns the
# move number to the main function
def pickamove(name):
    print("")
    move = input("It is " + name + """'s turn. What would you like to do?
    1 - Spin the wheel
    2 - Buy a vowel
    3 - Guess the word!
    4 - Quit the game\n""")
    while move not in '1234':
        move = input("Please enter a number from 1 to 4 to select your move. ").strip(' ')
    print(name, "chose", move + ".")
    return int(move)


# This function determines how much money is won when guessing a consonant
# and returns that amount
def isconinword(word,con,spun):
    if con in word:
        concount = word.count(con)
        money = concount*spun
    else:
        money = 0
    return money

# This function returns a statement saying whether the vowel was in the word
# and returns True if it was, False if it wasnt
def isvowinword(word,vow,playing,waiting):
    vowcount = word.count(vow)
    if vow in word:
        print('There were', vowcount, vow,"'s in the word.", playing + "'s turn continues.\n")
        return True
    else:
        print(vow, "is not a part of the word.", playing + "'s turn ends. It is now",\
        waiting + "'s turn.")
        return False

# This function takes the list of guessed letters, and checks whether the
# guessed vowel is a valid vowel that has not been previously guessed. It then
# returns the vowel.
def getvow(guessedletters,name):
    vow = input(name + " spent $25 to purchase a vowel. Please select a vowel. ")
    while vow.lower() not in "a,e,i,o,u":
        vow = input("Please enter a valid vowel.")
    while vow.lower() in guessedletters:
        vow = input("Please enter a vowel that has not been previously guessed. ")
    return vow

# This function takes the list of guessed letters, and checks whether the
# guessed consonant is a valid vowel that has not been previously guessed. It then
# returns the consonant.
def getcon(guessedletters):
    con = input("Please enter a consonant. ")
    while con.lower() not in "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z":
        con = input("Please enter a valid consonant.")
    while con.lower() in guessedletters:
        con = input("Please enter a consonant that has not been previously guessed. ")
    return con

# This function spins the wheel and returns the resulting number (between 0 and 21).
def spinthewheel(name):
    print (name, "has chosen to spin the wheel.")
    spun = random.randint(0,21)
    if spun == 0:
        print (name, "has spun a bankruptcy element. Their turn money is reset to zero.")
        return 0
    elif spun == 21:
        print (name, 'has spun a lose-a-turn element.')
        return 21
    else:
        print (name, "has spun a", str(spun) + '.')
        return spun

# This function takes a guessed consonant and checks
# whether the letter is in the secret word. It returns the hangman displayed.
def hangman(word, guessedletters):
    letters = list(word)
    hangman = ''
    for aletter in letters:
        if aletter in guessedletters:
            hangman += aletter + " "
        elif aletter == ' ':
            hangman += '  '
        elif aletter == "'":
            hangman += aletter + " "
        else:
            hangman += "_ "
    return hangman

# This function gets the secret word and category from the text file
# and stores them in a dictionary. It assumes the text file is in the same
# format as the example given on onQ, with the category preceding the
# secret word in each line.
def puzzleget():
    puzzletext = open('puzzles.txt', 'r')
    puzzles = []
    for line in puzzletext:
        puzzles.append(line.rstrip())
    picked = random.choice(puzzles).split()
    secretcat = {}
    secretcat['category'] = picked[0]
    secretcat['secretword'] = ' '.join(picked[1:])
    return secretcat

wordblitz()
