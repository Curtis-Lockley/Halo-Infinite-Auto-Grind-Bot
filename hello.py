from platform import platform
from re import T
import pyautogui
import time
from random import randrange
import threading

moves = ['w','s','a','d']

doStuff = 0
def randomKeyboard():
 print("keyboard thread started")
 global doStuff
 while True:
  while doStuff == 1:

   time.sleep(randrange(5,17))
   randomNum = randrange(0,len(moves))
   randomMove = moves[randomNum]
   pyautogui.keyDown(randomMove)
   time.sleep(randrange(0,2))
   pyautogui.keyUp(randomMove)

def randomMouse():
 global doStuff
 return

keyThread = threading.Thread(target=randomKeyboard)
keyThread.start()
screenWidth, screenHeight = pyautogui.size()
FAILSAFE = False

while True:
 #Focus game window
 # unFocused = pyautogui.locateOnScreen('HaloLogo.png',confidence = 0.8)
 # pyautogui.click(pyautogui.center(unFocused).x,pyautogui.center(unFocused).y)

 #Locate play button
 playBtn = pyautogui.locateOnScreen('button.png')

 playBtnX = pyautogui.center(playBtn).x
 playBtnY = pyautogui.center(playBtn).y

 #Find game
 pyautogui.moveTo(playBtnX,playBtnY)
 pyautogui.mouseDown()
 pyautogui.sleep(0.5)
 pyautogui.mouseUp()

 #Finding game
 while True:
     try:
      print("finding game.....")
      progress = pyautogui.locateOnScreen('progress.png',confidence=0.95)
      x = progress.left * 0
      break
     except:
      pass
 print("game found!")


 #Waiting for game to start
 while True:
     try:
      progress = pyautogui.locateOnScreen('progress.png',confidence=0.95)
      print("waiting for game to start")
      x = progress.left * 0
     except:
      break
 print("loading screen")
 while True:
     try:
      print("waiting match to begin...")
      loadScreen = pyautogui.locateOnScreen('loading.png')
      x = loadScreen.left * 0
      pass
     except:
         break

 time.sleep(15)
 print("in game, random input time")
 doStuff = 1

 #Spam random inputs

 #Game over, go back to main menu
 while True:
     try:
      print("waiting for game to end....")
      loadScreen = pyautogui.locateOnScreen('loading.png')
      x = loadScreen.left * 0
      break
     except:
         pass


 doStuff = 0
 print("game ended, waiting for menu to load")
 
 #Check if lvl up
 lvlup = False
 while True:
     try:
      loadScreen = pyautogui.locateOnScreen('next.png')
      x = loadScreen.left * 0
      print("lvled up!")
      lvlup = True
      time.sleep(3)
      print("next btn found! pressing ESC")
      pyautogui.keyDown('esc')
      time.sleep(1)
      pyautogui.keyUp('esc')
      print("ESC pressed")
      break
     except:
      try:
       print("lvlup not found!")
       loadScreen = pyautogui.locateOnScreen('close.png')
       x = loadScreen.left * 0
       print("close btn found! pressing ESC")
       time.sleep(5)
       pyautogui.keyDown('esc')
       time.sleep(2)
       pyautogui.keyUp('esc')
       print("ESC pressed")
       break
      except:
        pass

 if lvlup == True:
  while True:
     try:
      print("waiting for menu to appear....")
      loadScreen = pyautogui.locateOnScreen('close.png')
      x = loadScreen.left * 0
      time.sleep(2)
      pyautogui.keyUp('esc')
      break
     except:
         pass


 print("starting over")
 time.sleep(2)