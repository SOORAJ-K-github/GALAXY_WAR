import pygame, sys, math, random, time
from pygame import mixer
#intilosing pygame
pygame.init
pygame.font.init()
pygame.mixer.init()

#making screen width 800 and height 600
screen=pygame.display.set_mode((800,640))

#making caption for window "GALAXY"
pygame.display.set_caption("GALAXY WAR")

#setting icon image as image and making it as a icon 
image=pygame.image.load('spaceship_icon.png')
pygame.display.set_icon(image)

background=pygame.image.load('space_background_1.jpg')

mixer.music.load('song.wav')
mixer.music.play(-1)

chicken_speed=1.5
bullet_speed=4
player_speed=2
#setting player image as player_1 and its postions
player_1=pygame.image.load('player.png')
playerx=370
playery=500
p_x=0

enemy=[]
enemyx=[]
enemyy=[]
e_x=[]
k_e=1
collision_e=1
number_of_enimies=6
for i in range(number_of_enimies):
        enemy.append(pygame.image.load('a_1.png'))
        enemyx.append(random.randint(0,735))
        enemyy.append(random.randint(50,150))
        e_x.append(chicken_speed)

bulletimg=[]
bulletx=[]
bullety=[]
b_y=[]
b_fire=[]
max_bullet=10000
for i in range(max_bullet):
        bulletimg.append(pygame.image.load('bullet.png'))
        bulletx.append(0)
        bullety.append(500)
        b_y.append(bullet_speed)
        b_fire.append("ready")
        
multiple_bull=0

score_value=0
font = pygame.font.Font(None, 45)
font1 = pygame.font.Font(None, 100)
font2 = pygame.font.Font(None, 30)
textx=10
testy=10

game_close = pygame.font.Font(None, 100)

level_font= pygame.font.Font(None, 50)

def level(level):
    level = font.render('level : '+str(level), True, (0, 255, 0))
    screen.blit(level, (650, 10))


def show_score(scorer):
    score = font.render('score : '+str(scorer), True, (0, 255, 0))
    screen.blit(score, (10, 10))

def game_over():
         over = game_close.render('Game over', True, (255, 0, 0))
         screen.blit(over, (250, 280))
momo1=pygame.image.load('a_2.png')
def momo():
         screen.blit(momo1, (500, 300))
         
#it is for players visual in display
def player1(x,y):
    screen.blit(player_1,(x, y))
    
def enemy1(x,y,i):
    screen.blit(enemy[i], (x,y))
    
def bullet(x,y,i):
    global b_fire
    b_fire[i]="fire"
    screen.blit(bulletimg[i],(x+16,y+10))

def Collision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow(bulletx-enemyx,2)) + (math.pow(bullety-enemyy,2)))
    if distance<27:
     return True
    else:
        return False

def start(x,y,choice):
    if not choice:
        animation=font1.render("start", True, (255, 255, 255),(0,255,0))
    else:
        animation=font1.render("start", True, (255, 255, 255),)
    screen.blit(animation,(x,y))

def exiti(xx,yy,choice):
    if choice:
        animation=font1.render("exit", True, (255, 255, 255),(0,255,0))
    else:
        animation=font1.render("exit", True, (255, 255, 255))
    screen.blit(animation,(xx,yy))

def welcome_text(xxx,yyy):
    animation=font2.render("Press space button", True, (255, 255, 255))
    screen.blit(animation,(xxx,yyy))
    
ss="redy"
x=160
y=100
xx=160
yy=300
xxx=500
yyy=30
choice=False
s="ready"


running=True
kl=0
while running:
    #setting display background as black
  screen.fill((0, 0, 0))
  if ss=="redy":
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                choice=False
            if event.key==pygame.K_DOWN:
                choice=True
            if event.key==pygame.K_SPACE:          
                s="fire"
                
      if s=="fire":
        if choice:
              pygame.quit()
        else:
            ss="start"
      elif kl==0:
          v=mixer.Sound('voice.wav')
          v.play()
          kl+=10
      else:
        welcome_text(xxx,yyy)
        start(x,y,choice)
        exiti(xx,yy,choice)
        momo()
  else:
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                p_x=player_speed
            if event.key == pygame.K_LEFT:
                p_x=-player_speed
            if event.key == pygame.K_SPACE:
                multiple_bull+=1
                j=multiple_bull-1
                if b_fire[j] == "ready":
                    bullet_sound=mixer.Sound('laser1.wav')
                    bullet_sound.play()
                    bulletx[j]=playerx
                    bullet(bulletx[j],bullety[j],j)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
             p_x=0
             
    for i in range(multiple_bull):          
            if b_fire[i] == "fire":
                bullet(bulletx[i],bullety[i],i)
                bullety[i]-=b_y[i]
            if bullety[i]<=0:
                b_fire[i]="ready"
                bullety[i]=500
        
    playerx+=p_x
    if playerx >=736:
        playerx=736
    elif playerx<=0:
        playerx=0
        
    for i in range(number_of_enimies):
        for l in range(number_of_enimies):
                if enemyy[l]>430:
                        game_over()
                        running=False       
        enemyx[i]+=e_x[i]
        if enemyx[i]>=736:
            e_x[i]=-chicken_speed
            enemyy[i]+=40
        elif enemyx[i]<=0:
            e_x[i]=chicken_speed
            enemyy[i]+=40
        for j in range(multiple_bull):
                collision=Collision(enemyx[i],enemyy[i],bulletx[j],bullety[j])
                if collision:
                    r=mixer.Sound('cluck2.wav')
                    r.play()
                    bullety[j]=500
                    b_fire[j]="ready"
                    score_value+=1
                    enemyx[i]=random.randint(0,735)
                    enemyy[i]=random.randint(50,150)
            
        enemy1(enemyx[i], enemyy[i],i)
    ##level(k_e)   
    player1(playerx,playery)
    show_score(score_value)
    #updating screen
  pygame.display.update()
