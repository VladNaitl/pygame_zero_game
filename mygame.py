import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)

import pgzrun
import random

WIDTH = 800
HEIGHT = 600

score = 0
MENU = 0
GAME = 1
gameover = 0


state = MENU
# Определение переменных для меню
menu_items = ["Start Game", "Music ON","Exit"]
selected_item = 0
music.play('music')


# Функция отрисовки меню
def draw_menu():
    screen.clear()
    for i, item in enumerate(menu_items):
        if i == selected_item:
            screen.draw.text(item, center=(WIDTH/2, HEIGHT/2 + i * 50), color="yellow", fontsize=40)
        else:
            screen.draw.text(item, center=(WIDTH/2, HEIGHT/2 + i * 50), color="white", fontsize=40)




class Hero:
    def __init__(self):
        self.actor = Actor('ufo', (WIDTH/2, HEIGHT-64))
        self.speed = 4
        self.direction = "stop"

    def draw(self):
        self.actor.draw()

    def update(self):
        pass
    
class Enemy:
  def __init__(self):
    self.actor = Actor('asteroid', (random.randint(25,WIDTH-25),random.randint(25, 75)))
    self.speed = 3
    self.direction = "bottom"

  def draw(self):
    self.actor.draw()
  

# spaceship = Actor('spaceship', (WIDTH/2, HEIGHT-64))
spaceship = Hero()
asteroid  = Enemy()
asteroid.speed = 5
asteroid2 = Enemy()
asteroid2.speed = 6
asteroid3 = Enemy()
asteroid3.speed = 7


def draw():
  if state == MENU:
        draw_menu()
  if state == GAME:
    screen.blit('background', (0, 0))
    spaceship.draw()
    asteroid.draw()
    asteroid2.draw()
    asteroid3.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
    if gameover == 1:
       screen.draw.text("GAME OVER", (WIDTH/2-195, HEIGHT/2-90), color=(255,255,255), fontsize=90)
       screen.draw.text("press 'SPACE' to play again", (WIDTH/2-140, HEIGHT/2), color=(255,255,255), fontsize=30)

def update():
  global score,gameover
  if state == GAME:
    if spaceship.actor.colliderect(asteroid.actor) or spaceship.actor.colliderect(asteroid2.actor) or spaceship.actor.colliderect(asteroid3.actor):
      asteroid.speed = 0
      asteroid2.speed = 0
      asteroid3.speed = 0
      spaceship.speed = 0
      gameover = 1


    if spaceship.direction == "left" and spaceship.actor.x > 32:
        spaceship.actor.x -= spaceship.speed

    if spaceship.direction == "right" and spaceship.actor.x < WIDTH - 32:
        spaceship.actor.x += spaceship.speed

    if asteroid.actor.y > HEIGHT:
      score += 10
      print(score)
      asteroid.actor = Actor('asteroid', (random.randint(25,WIDTH-25),random.randint(25, 75)))

    if asteroid2.actor.y > HEIGHT:
      score += 10
      print(score)
      asteroid2.actor = Actor('asteroid', (random.randint(25,WIDTH-25),random.randint(25, 75)))

    if asteroid3.actor.y > HEIGHT:
      score += 10
      print(score)
      asteroid3.actor = Actor('asteroid', (random.randint(25,WIDTH-25),random.randint(25, 75)))
      

    asteroid.actor.y += asteroid.speed
    asteroid2.actor.y += asteroid2.speed
    asteroid3.actor.y += asteroid3.speed


  

def on_key_down(key):
  global state, selected_item, gameover, score, spaceship, asteroid, asteroid2, asteroid3,menu_items
  if state == MENU:
      if key == keys.UP:
          selected_item = (selected_item - 1) % len(menu_items)
          print(selected_item)
      elif key == keys.DOWN:
          selected_item = (selected_item + 1) % len(menu_items)
          print(selected_item)
      elif key == keys.SPACE:
          if selected_item == 0:
              state = GAME
          elif selected_item == 1:
              if menu_items[1] == "Music ON":
                  music.stop()
                  menu_items[1] = "Music OFF"
              else:
                  menu_items[1] = "Music ON"
                  music.play('music')
          elif selected_item == 2:
              exit()
  elif state == GAME:
    if key == keys.LEFT:
      spaceship.direction = "left"

    if key == keys.RIGHT:
      spaceship.direction = "right"
    
    if key == keys.SPACE and gameover == 1:
      spaceship = Hero()
      asteroid  = Enemy()
      asteroid.speed = 5
      asteroid2 = Enemy()
      asteroid2.speed = 6
      asteroid3 = Enemy()
      asteroid3.speed = 7
      score = 0
      gameover = 0
      if menu_items[1] == "Music ON":
        music.play('music')
       
       




pgzrun.go()