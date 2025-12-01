import time
import math
import random
from colorama import Fore, Back

#Introduction
print(Fore.BLUE + "---INSTRUCTIONS---\n")
print(Fore.LIGHTYELLOW_EX,"• Use the Arrow Keys to move")
print(Fore.LIGHTYELLOW_EX,"• Don't touch the enemies, because you will die if you do")
print(Fore.LIGHTYELLOW_EX,"• To win, you must get all the treasures before the countdown finishes\n")

print(Fore.LIGHTGREEN_EX + "---NOTES---\n")
print(Fore.LIGHTYELLOW_EX,"• Play in full screen mode to see the borders")
print(Fore.LIGHTYELLOW_EX,"• You are the blue square")
print(Fore.LIGHTYELLOW_EX,"• The enemies are the red triangles")
print(Fore.LIGHTYELLOW_EX,"• The treasures are the yellow circles\n")
print(Fore.LIGHTYELLOW_EX,"• If you get close (3 or less blocks) to the enemies, they will follow you")

print(Fore.MAGENTA + "***HINT***\n")
print(Fore.LIGHTYELLOW_EX,"• There are multiple safe zones throughout the maze")

s = 0
print(Fore.RED)

while(s < 20):
  time.sleep(1)
  s += 1
  print(f"Starting in {21 - s} seconds...")

import turtle
  
#Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Countdown Maze")

#Score
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("cyan")
score_pen.penup()
score_pen.setposition(-142.5,200)
score_print = f"Score:\n{score} of 5"
score_pen.clear()
score_pen.write(score_print, False, align = "left", font = ("Comic Sans", 14, "normal"))
score_pen.hideturtle()

#Create a timer
timer_text = turtle.Turtle()
timer_text.hideturtle()
timer_text.color("cyan")
timer_text.penup()
timer_text.setposition(189.5,190)


start = time.time()

#Drawing the maze
class Maze_pen(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("orange")
    self.shapesize(0.8,0.8)
    self.penup()
    self.speed(0)

#Create the player
class Player(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("blue")
    self.shapesize(0.8,0.8)
    self.penup()
    self.speed(0)
  def go_up(self):
    move_to_x = player.xcor()
    move_to_y = player.ycor() + 19

    if(move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)
    
  def go_down(self):
    move_to_x = player.xcor()
    move_to_y = player.ycor() - 19

    if(move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)
    
  def go_right(self):
    move_to_x = player.xcor() + 19
    move_to_y = player.ycor()

    if(move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)
    
  def go_left(self):
    move_to_x = player.xcor() - 19
    move_to_y = player.ycor()

    if(move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)

  def collision(self, other):
    a = self.xcor() - other.xcor()
    b = self.ycor() - other.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))

    if(distance < 5):
      return True
    else:
      return False

#Create the treausure
class Treasure(turtle.Turtle):
  def __init__(self, x, y):
    turtle.Turtle.__init__(self)
    self.shape("circle")
    self.color("gold")
    self.shapesize(0.75,0.75)
    self.penup()
    self.speed(0)
    self.goto(x,y)

  def destroy(self):
    self.goto(2000,2000)
    self.hideturtle()

#Create the enemy
class Enemy(turtle.Turtle):
  def __init__(self, x, y):
    turtle.Turtle.__init__(self)
    self.shape("triangle")
    self.color("red")
    self.shapesize(0.8,0.8)
    self.penup()
    self.speed(0)
    self.goto(x, y)
    self.direction = random.choice(["up", "down", "left", "right"])

  def move(self):
    if(self.direction == "up"):
      enemy_x = 0
      enemy_y = 19
      self.setheading(90)
    elif(self.direction == "down"):
      enemy_x = 0
      enemy_y = -19
      self.setheading(270)
    elif(self.direction == "left"):
      enemy_x = -19
      enemy_y = 0
      self.setheading(180)
    elif(self.direction == "right"):
      enemy_x = 19
      enemy_y = 0
      self.setheading(0)
    else:
      enemy_x = 0
      enemy_y = 0

    #Check if the player is close
    #If so head in that direction
    if self.close(player):
      if(player.xcor() < self.xcor()):
        self.direction = "left"
      elif(player.xcor() > self.xcor()):
        self.direction = "right"
      elif(player.ycor() > self.ycor()):
        self.direction = "up"
      elif(player.ycor() < self.ycor()):
        self.direction = "down"

    #Calculate the spot to move to
    move_to_x = self.xcor() + enemy_x
    move_to_y = self.ycor() + enemy_y

    #Check if the space has a wall
    if((move_to_x, move_to_y) not in walls):
      if((move_to_x, move_to_y) not in limit):
        self.goto(move_to_x, move_to_y)
      elif((move_to_x, move_to_y) in limit):
        self.direction = random.choice(["up", "down", "left", "right"])
    else:
      #Choose a different direction
      self.direction = random.choice(["up", "down", "left", "right"])

    #Set timer to move next time
    turtle.ontimer(self.move, t = 250)

  def close(self, other):
    a = self.xcor() - other.xcor()
    b = self.ycor() - other.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))

    if(distance < 60):
      return True
    else:
      return False

#Create list for levels
levels = [""]

#Define first level
level_1 = [
"XXXXSSSSSXXXXXXXXXXXXXXXX",
"XP XSSSSSX          X   X",
"X  XXXXXXX  XXXXXX  X   X",
"X        L  XXXXXX EXXXXX",
"X        L  XXX        XX",
"XXXXXX  XX  XXXT       XX",
"XXXXXXLLXXLLXXXXXX  XXXXX",
"XXXXXX         XXX  XXXXX",
"XT XXX        EXXX      X",
"X  XXX  XXXXXXXXXXXXXXX X",
"X         XXXXXXXXXXXXX X",
"X                XXXXX  X",
"XXXXXXXXXXXX     XXXXLL X",
"XXXXXXXXXXXXXXXLLXXXXLLXX",
"XXXT XXXXXXXXXXLL       X",
"XXX                    EX",
"XXX       LLXXXXXXXXXXXXX",
"XXXXXXXXXXLLXXXXXXXXXXXXX",
"XXXXXXXXXXLL           TX",
"XXT  XXXXXE             X",
"XX   XXXXXXXXXXXXXLLXXXXX",
"XX     XXXXXXXXXXXLLXXXXX",
"XX          XXXX  LL    X",
"XXXX                   EX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Create a list for the treasures
treasures = []

#Create a list for the enemies
enemies = []

#Add mazes to maze list
levels.append(level_1)

def setup_maze(level):
  for y in range(len(level)):
    for x in range(len(level[y])):
      character = level[y][x]
      screen_x = -230 + (x * 19)
      screen_y = 230 - (y * 19)

      if(character == "X"):
        maze_pen.goto(screen_x, screen_y)
        maze_pen.stamp()
        walls.append((screen_x, screen_y))

      if(character == "L"):
        limit.append((screen_x, screen_y))

      if(character == "P"):
       player.goto(screen_x, screen_y)

      if(character == "T"):
        treasures.append(Treasure(screen_x, screen_y))

      if(character == "E"):
        enemies.append(Enemy(screen_x, screen_y))

maze_pen = Maze_pen()
player = Player()

walls = []
limit = []

setup_maze(levels[1])

#Keyboard controls
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

screen.tracer(0)

#Start moving the enemies
for enemy in enemies:
  turtle.ontimer(enemy.move, t = 400)

game = True

while game == True and time.time() - start < 155:
  timer_text.clear()
  timer_text.write(155 - int(time.time() - start), False, align = "center", font=("Comic Sans", 14))
  turtle.onkey(player.go_left, "Left")
  turtle.onkey(player.go_right, "Right")
  turtle.onkey(player.go_up, "Up")
  turtle.onkey(player.go_down, "Down")
  for treasure in treasures:
    if player.collision(treasure):
      treasure.destroy()
      treasures.remove(treasure)
      #Increase the score
      score += 1
      score_pen.setposition(-142.5,200)
      score_print = f"Score:\n{score} of 5"
      score_pen.clear()
      score_pen.write(score_print, False, align = "left", font = ("Comic Sans", 14, "normal"))
    if(score == 5):
      print("You win")
      score_pen.setposition(-154,210)
      score_print = "You win!"
      score_pen.clear()
      score_pen.write(score_print, False, align = "left", font = ("Comic Sans", 14, "normal"))
      game = False

  #Check for collisions between player and enemies
  for enemy in enemies:
    if(player.collision(enemy) or time.time() - start > 160):
      score_pen.setposition(-158.5,210)
      score_print = "You died!"
      score_pen.clear()
      score_pen.write(score_print, False, align = "left", font = ("Comic Sans", 14, "normal"))
      game = False
  screen.update()