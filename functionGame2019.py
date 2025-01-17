# Based on code at:
# http://programarcadegames.com/python_examples/f.php?file=array_backed_grid.py

# 1 - Import pygame library ####################################################
import pygame
from pygame.locals import *

# 2 - Set game global variables ################################################
boardsize = (512, 512)
screen = pygame.display.set_mode(boardsize)
width, height, margin = 100, 100, 2
BLACK = (0, 0, 0)
WHITE = (255,255,255)
grid = [] # 2D array (list of lists) for board
player = pygame.image.load('player.jpg').convert()
player2 = pygame.image.load('player.jpg').convert()
playerCoord = [0,0]
icon0 = pygame.image.load('icon0.jpg').convert() 
icon1 = pygame.image.load('icon1.jpg').convert()
icon2 = pygame.image.load('icon2.jpg').convert()
icon3 = pygame.image.load('icon3.jpg').convert()

# 3 - Define game functions ####################################################
## 3a - Initialize the game board
def initBoard(): 
  for row in range(5):
    grid.append([])
    for column in range(5):
        grid[row].append(0) # all values set to 0
  # Set hard-coded start locations for player and icons:        
  grid[4][4] = 1  # player icon; value of 1 is player location
  grid[0][0] = 2
  grid[0][2] = 10 # icon 0 location set by a value of 10
  grid[4][1] = 11 # icon 1 location set by a value of 11
  grid[2][3] = 12 # icon 2 location set by a value of 12
  grid[2][0] = 13 # icon 3 location set by a value of 13

## 3b - Draw player/icon on the board
def drawIcon(rw,cl,iconName):
  screen.blit(iconName,((margin+width)*cl + margin,(margin+height)*rw + margin))
  
## 3c - Update the grid for the board
def updateBoard():
  for row in range(5):
    for column in range(5):
      color = BLACK
      pygame.draw.rect(screen,color,[(margin + width) * column + margin,
                                     (margin + height) * row + margin,
                                      width, height])
      if grid[row][column] == 10:  #icon0 location
        drawIcon(row,column,icon0)  
      if grid[row][column] == 11:  #icon1 location
        drawIcon(row,column,icon1)  
      if grid[row][column] == 12:  #icon2 location
        drawIcon(row,column,icon2)  
      if grid[row][column] == 13:  #icon3 location
        drawIcon(row,column,icon3)    
      if grid[row][column] == 1:  #player location
        drawIcon(row,column,player)
      if grid[row][column] == 2:  #player location
        drawIcon(row,column,player2)  

## 3d - Adjust score and print out a message if increased
def adjustScore(scoreP):
  if grid[playerCoord[0]][playerCoord[1]] >= 10:
    scoreP += 1
    print("You have learned "+str(scoreP)+" of the Core 4")
  return scoreP

## 3e - Handle player movement
def movePlayer(scoreParam, stepcount):
  # Based on how-to at:
  # https://opensource.com/article/17/12/game-python-moving-player
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True; pygame.quit()
        sys.exit(); numlitter == 0
      # only handle key releases for simplicity (KEYUP not KEYDOWN)
      elif event.type == pygame.KEYUP:
        stepcount += 1
        if event.key == ord('a'):
          if playerCoord[1] > 0:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[1] -= 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 1          
        elif event.key == ord('d'):
          if playerCoord[1] < 4:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[1] += 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 1
        elif event.key == ord('w'):
          if playerCoord[0] > 0:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[0] -= 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 1          
        elif event.key == ord('s'):
          if playerCoord[0] < 4:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[0] += 1
            scoreParam = adjustScore(scoreParam)    
            grid[playerCoord[0]][playerCoord[1]] = 1
            ###
        elif event.key == pygame.K_LEFT:
          if playerCoord[1] > 0:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[1] -= 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 2          
        elif event.key == pygame.K_RIGHT:
          if playerCoord[1] < 4:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[1] += 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 2
        elif event.key == pygame.K_UP:
          if playerCoord[0] > 0:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[0] -= 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 2          
        elif event.key == pygame.K_DOWN:
          if playerCoord[0] < 4:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[0] += 1
            scoreParam = adjustScore(scoreParam)    
            grid[playerCoord[0]][playerCoord[1]] = 2
        elif event.key == ord('q'):
          print('quit game'); pygame.quit()
          break          
  return scoreParam, stepcount


# 4 - Define main game #########################################################
def gameFunct():
  ## 4a - Initialize game
  pygame.init()
  initBoard()
  clock = pygame.time.Clock()
  score = 0
  steps = 0
  print("Collect all of the Core 4 to increase your knowledge!\n")
  ## 4b - keep looping until exit condition met
  while (score < 4):
    score, steps = movePlayer(score, steps)  # Handle player movement
    updateBoard() # Update the grid for the board
    clock.tick(60) # In milliseconds (https://www.pygame.org/docs/ref/time.html)
    pygame.display.flip() # Redraw the board
    if score == 4: # Check for exit condition congratulatory message
      print("Congratulations you have completed Core 4!")
      print("The goal is 10 steps or less, you took " + str(steps))
      print("Now practice practice practice and create cool code!")
  pygame.quit() # Quit the game

# Run automatically upon load/F5 ###############################################
if __name__ == "__main__":
  gameFunct()
