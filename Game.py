import random

gametime = True


while gametime == True:
  correct = False
  selection = input(" Do you want to play Number Guessing Game(1) or Rock Paper Scissors(2)?")
  gametime = False

  if selection == str(1):

    realNumber = random.randint(0,75)
    realNumber = int(realNumber)
    guesses = 0


    while (guesses < 6 and correct == False):
      guessedNumber = input("Guess a number, 1 - 75:  ")
      guessedNumber = int(guessedNumber)

      if guessedNumber == realNumber:
        print ("You got it!")
        print(" ")
        gametime = True
        correct = True

      if guessedNumber > realNumber:
        print("Too High!")
        guesses= guesses + 1

      if guessedNumber < realNumber:
       print("Too Low!")
       guesses= guesses + 1
  
    while (correct == False):

      print("You ran out of guesses, I was thinking of " + str(realNumber))
      correct = True
    gametime = True

  if selection == str(2):
    rpsnumber = random.randint(0,3)
    rpsnumber = int(rpsnumber)
    playerchoice = input ("Rock(1), Paper(2), or Scissors(3)")
    playerchoice=int(playerchoice)
    
    if rpsnumber == 1 and playerchoice ==1:
     print("Tie! We both went rock!")
    
    if rpsnumber == 1 and playerchoice == 2:
      print("You Win! Paper beats Rock!")
    
    if rpsnumber ==1 and playerchoice ==3:
      print("I win. Rock beats scissors ")
    
    if rpsnumber == 2 and playerchoice ==1:
      print("I win! Paper beat Rock!")
    
    if rpsnumber == 2 and playerchoice ==2:
      print("Tie! Paper and Paper!")
    
    if rpsnumber == 2 and playerchoice ==3:
      print ("You win. Scissors beat paper")
    
    if rpsnumber ==3 and playerchoice ==1 :
      print("You Win!!!Rock beats Scissors")
    
    if rpsnumber ==3 and playerchoice ==2:
      print("I Win! Scissors beat paper!")
    
    if rpsnumber ==3 and playerchoice ==3:
      print("Tie! Your Rock and My Rock!")
    
    print(" ")
    gametime = True

while gametime ==False:
  break
