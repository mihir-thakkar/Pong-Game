# Pong Game
 
import pygame
import random
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = ( 0,     0, 255)

# defining a function to draw the paddles
def draw_paddles(screen,paddle1_x,paddle1_y,paddle2_x,paddle2__y):
    pygame.draw.line(screen,green,[5,paddle1_y],[5,paddle1_y+90],15)
    pygame.draw.line(screen,green,[width-5,paddle2_y],[width-5,paddle2_y+90],15)
#initialize the pygame engine
pygame.init()
  
# Set the height and width of the screen
width = 1200
height = 650
size=[width,height]
screen=pygame.display.set_mode(size)
#current position
paddle1_x = 0
paddle1_y = height/2
paddle2_x = width
paddle2_y = height/2

pygame.display.set_caption("SAMPLE PONG")
 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
 
# initialize the variables
ball_pos_x = width/2
ball_pos_y = height/2
ball_change_x = 0
ball_change_y = 0
paddle1_speed_x = 0
paddle1_speed_y = 0
paddle2_speed_x = 0
paddle2_speed_y = 0
score1 = "0"
score2 = "0"

# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    # Set the screen background
    screen.fill(black)
 
    # Draw the ball
    pygame.draw.circle(screen,white,[ball_pos_x,ball_pos_y],20)
    # Draw the centre line
    pygame.draw.line(screen,red,[width/2,0],[width/2,height],1)
    # Draw the paddles and gutters
    pygame.draw.line(screen,white,[width-15,0],[width-15,height],2)
    pygame.draw.line(screen,white,[15,0],[15,height],2)
    font = pygame.font.Font(None,30)
    text= font.render("PONG GAME",True,white)
    screen.blit(text,[460,620])
    text= font.render("Developed by MIHIR THAKKAR",True,white)
    screen.blit(text,[620,620])
    font = pygame.font.Font(None,50)
    text= font.render("Player 1",True,blue)
    screen.blit(text,[235,180])
    text= font.render(score1,True,white)
    screen.blit(text,[280,240])
    text= font.render("Player 2",True,blue)
    screen.blit(text,[860,180])
    text= font.render(score2,True,white)
    screen.blit(text,[905,240])
    
    
    # if user presses a key down 
    if event.type == pygame.KEYDOWN:
    # Figure out the key
    # adjust speed.
        
        if ball_change_y == 0 :
            ball_change_x = 5
            ball_change_y = 4
        if event.key ==  pygame.K_w:
            paddle1_speed_y =-10
        if event.key == pygame.K_s: 
            paddle1_speed_y =10
        if event.key ==  pygame.K_UP:
            paddle2_speed_y =-10
        if event.key == pygame.K_DOWN:
            paddle2_speed_y =10

                  
     # User releases up a key
    if event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
        
        if event.key == pygame.K_w: 
            paddle1_speed_y = 0
        if event.key == pygame.K_s: 
            paddle1_speed_y = 0
        if event.key == pygame.K_UP:
            paddle2_speed_y = 0
        if event.key == pygame.K_DOWN:
            paddle2_speed_y = 0


    
    # move the paddles
    paddle1_x = paddle1_x + paddle1_speed_x
    paddle1_y = paddle1_y + paddle1_speed_y
    
    paddle2_x = paddle2_x + paddle2_speed_x
    paddle2_y = paddle2_y + paddle2_speed_y
    
    draw_paddles(screen,paddle1_x,paddle1_y,paddle2_x,paddle2_y)
    
   # Move the ball starting point        
    ball_pos_x += ball_change_x
    ball_pos_y += ball_change_y

    # bounce the ball on paddles
    #if ball_pos_x == 1200-35 and ball_pos_y < paddle2_y and ball_pos_y > paddle2_y +90:
    #    if int(score1)>int(score2):

     #       font = pygame.font.Font(None,90)
     #       text= font.render("WINNER!!",True,white)
     #       screen.blit(text,[900,350])
     #   if int(score2)>int(score1):
     
     #      font = pygame.font.Font(None,90)
     #       text= font.render("WINNER!!",True,white)
      #      screen.blit(text,[300,350])
    #if ball_pos_x == 35 and ball_pos_y < paddle1_y and ball_pos_y > paddle1_y +90:
     #   if int(score1)>int(score2):

     #       font = pygame.font.Font(None,90)
     #       text= font.render("WINNER!!",True,white)
     #       screen.blit(text,[900,350])
     #   if int(score2)>int(score1):
      #      
      #      font = pygame.font.Font(None,90)
      #      text= font.render("WINNER!!",True,white)
      #      screen.blit(text,[300,350])
    if ball_pos_y > 650-35 or ball_pos_y < 35:
        ball_change_y = ball_change_y * -1
    if (ball_pos_x == 1200-35 and ball_pos_y > paddle2_y and ball_pos_y < paddle2_y +90):
        ball_change_x += (ball_change_x) * -2
    if (ball_pos_x == 35 and ball_pos_y > paddle1_y and ball_pos_y < paddle1_y + 90):
        ball_change_x += (ball_change_x) * -2
    #if ball_pos_x == 1200-35 and ball_pos_y > paddle2_y and ball_pos_y < paddle2_y +90:
        #score2 = str(int(score2) + 1)
    # if ball_pos_x == 35 and ball_pos_y > paddle1_y and ball_pos_y < paddle1_y +90:
        #score1 = str(int(score1) + 1)

            
    # Limit to 50 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
