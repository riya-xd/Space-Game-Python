#HOW TO CREATE A PYCHARM SCREEN
import math
import random
import pygame
from pygame import mixer
#initialize the pygame
pygame.init()
#CREATING THE SCREEN
#HOW TO CHANGE THE TITLE OF GAME WINDOW ,LOGO
screen = pygame.display.set_mode((800,600))
#background
#background = pygame.image.load('spacegames/ufo.png')
#sound
mixer.music.load("spacegames/background.wav")
mixer.music.play(-1)

pygame.display.set_caption('MY SPACE GAME')
#SETTIING THE ICON OF THE WINDOW BY DOWNLOAD www.flaticon.com png image 32x32
icon = pygame.image.load('.\\spacegames\\ufo.png')
#PLAYER
playerimg = pygame.image.load('spacegames/player.png')
playerX = 370
playerY = 480
player_change=0
#ENEMY
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('spacegames/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 250))
    enemyX_change.append(4)
    enemyY_change.append(40)
#BULLET
bulletimg = pygame.image.load('spacegames/bullet.png')
#bullet ready state means not fire
#bullet fire state means currently fire
bulletX = 370
#bulletX = 0
bulletY = 480
bullet_changeX = 0
bullet_changeY = 30
bullet_state = 'ready'
bg = pygame.image.load('spacegames/background.png')

#score
score_value = 0
font = pygame.font.Font('FreeSans/FreeSansBold.ttf',32)
textX = 10
textY = 10

#GAME OVER
over_font = pygame.font.Font('FreeSans/FreeSansBold.ttf',64)
def show_score(x, y):

    score = font.render('Score: '+str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))  #here blit means draw
#methods to draw image on screen
def player(x,y):
    screen.blit(playerimg,(playerX,playerY)) #here blits means draw
    #screen.blit(playerimg,(x,y))
#spacegames = pygame.images
pygame.display.set_icon(icon)
def fireBullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)+(math.pow(enemyY-bulletY, 2)))
    if distance<27:
        return True
    else:
        return False
#INFINITE LOOP FOR STOP WINDOW ON THE SCREEN
running = True
while running:
    screen.blit(bg, (0, 0))
    #screen.blit(bg(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -5
            elif event.key == pygame.K_RIGHT:
                player_change = 5
            elif event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletSound = mixer.Sound('spacegames/laser.wav')
                    bulletSound.play()
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0
    playerX = playerX + player_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 740:
        playerX = 740
    player(playerX, playerY)
#SETTING BACKGROUND COLOR ANYTHING THAT WE WANT INSIDE TO SCREEN CONTINUOUSLY, IT WILL GIVEN IN WHILE LOOP
#screen.fill(r,g,b) ANYTHING AFTER CHANGE WE NEED TO UPDATE THE DISPLAY
    #screen.fill((193,118,171))
#ENEMY MOVEMENT
    for i in range (num_of_enemies):
        #GAME OVER
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] = enemyX[i] + enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i]= -4
            enemyY[i] += enemyY_change[i]
        #COLLISION
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosionSound = mixer.Sound('spacegames/explosion.wav')
            explosionSound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value +=1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    #BULLET MOVEMENT
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fireBullet(bulletX,bulletY)
        #bulletX = 0
        bulletY -= bullet_changeY
    #player(playerX,playerY)
    show_score(textX, textY)
    pygame.display.update()

