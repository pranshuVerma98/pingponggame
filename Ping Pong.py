import pygame
import random

pygame.init()
width = 800
height = 600
disp = pygame.display.set_mode((width,height))
pygame.display.set_caption('Ping Pong Game')
clk = pygame.time.Clock()

def bar(y_left,y_right):
   pygame.draw.rect(disp,(255,255,255),[0,y_left,10,100])
   pygame.draw.rect(disp,(255,255,255),[width-10,y_right,10,100])

def player1(count):
   largetext = pygame.font.Font(None,25)
   textsurf = largetext.render("Player 1:"+str(count),True,(255,0,0),(0,0,0))
   textrect = textsurf.get_rect()
   textrect.center = (width*0.1,height*0.05)
   disp.blit(textsurf,textrect)

def player2(count):
   largetext = pygame.font.Font(None,25)
   textsurf = largetext.render("Player 2:"+str(count),True,(255,0,0),(0,0,0))
   textrect = textsurf.get_rect()
   textrect.center = (width*0.9,height*0.05)
   disp.blit(textsurf,textrect)

#default values
x_ball = random.randrange(100,width-100,10)
y_ball = random.randrange(0,height,10)
speed = 2
right = True
down = True

#bar y values
left_y = 0
right_y = 0
left_change = 0
right_change = 0

#scores
score_1 = 0
score_2 = 0
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         quit()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP:
            right_change = -5
         elif event.key == pygame.K_DOWN:
            right_change = +5
         if event.key == pygame.K_w:
            left_change = -5
         elif event.key == pygame.K_s:
            left_change = +5
      if event.type == pygame.KEYUP:
         left_change =0
         right_change =0
         
   if right == True:
      x_ball += speed
   else:
      x_ball -=speed
   if down == True:
      y_ball += speed
   else:
      y_ball -=speed

   #limiting ball moving left/right
   if x_ball>=width-10:
      right = False
   elif x_ball<=10:
      right = True

   #limiting ball moving Up/down
   if y_ball>=height-10:
      down = False
   elif y_ball<=10:
      down = True

   #making change in bars Y
   left_y += left_change
   right_y += right_change
   if left_y<=0:
      left_y=0
   if left_y+100>=height:
      left_y = 500
   if right_y<=0:
      right_y=0
   if right_y+100>=height:
      right_y = 500

   #writing code for Score
   if x_ball>=width-10:
      if y_ball<right_y or y_ball>right_y+100:
         score_1 +=1
         x_ball = 790
         y_ball = random.randrange(10,height-10,10)
   if x_ball<=10:
      if y_ball<left_y or y_ball>left_y+100:
         score_2 +=1
         x_ball = 10
         y_ball = random.randrange(10,height-10,10)
   
   disp.fill((0,0,0))
   player1(score_1)
   player2(score_2)
   pygame.draw.circle(disp, (0,0,255),(x_ball,y_ball),10)
   bar(left_y,right_y)
   pygame.display.update()
   clk.tick(60)
