import time
import pygame
from sys import exit
from random import randrange
from pygame import mixer


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 553))
pygame.display.set_caption('Cosmo Game')
clock = pygame.time.Clock()

flying = False
running = True
game_over = False
collision = False
score = 0
col_count = 0

last_col_time = pygame.time.get_ticks()
delay_time = 1000

#background music
sound = mixer.Sound("sound.mp3")
#font
font1=pygame.font.Font("opp.ttf",80)
text1 = font1.render("GAME OVER",True,(255,255,255))

#background image
bg_surface = pygame.image.load('gamebg.jpg').convert()
bg = pygame.transform.scale(bg_surface, (1000, 553))
i=0

#lives
lives = pygame.image.load('heart.png')

#player
player = pygame.image.load('player.png')
player_x = 250
player_y = 250
player_rectangle= player.get_rect(topleft = (player_x, player_y))
player_rect = player_rectangle.inflate(-30,-35)

#enemy
enemy = pygame.image.load('ufo.png')
enemy_x_pos = 1024
enemy_y_pos = randrange(10, 450)
enemy_rectangle = enemy.get_rect(topleft = (enemy_x_pos, enemy_y_pos))
enemy_rect = enemy_rectangle.inflate(-30,-65)
enemy_speed = 5
#jump and gravity
gravity = 1
player_speed = 0

#screen_setup
#screen_size
#background_img
background_image=pygame.image.load("front.jpg")
gm=pygame.image.load("gameover.png")
pygame.display.set_caption("SuperCosmers")
font=pygame.font.Font(None,40)
text=font1.render("SUPER COSMO",True,(0,0,0))
start_button=pygame.Rect(400,450,200,50)
text4=font.render("START",True,(0,0,0))
font4=pygame.font.Font(None,80)
text22=font.render("SCORE:",True,(0,0,0))

#main game loop
running = True
maingame=False

while running:
    #blit background-img
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    screen.blit(background_image,(0,0)) 
    screen.blit(text,(150,180))
    pygame.draw.rect(screen, (170, 0, 237), start_button)
    screen.blit(text4,(start_button.x + 50,start_button.y + 12))
    pygame.display.update()    
    for event in pygame.event.get():
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] == 1:
            mouse_pos=pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_pos):
                maingame=True
                sound.play(-1)
    while maingame:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and flying == False :
                flying = True
        text21=font.render(str(score),True,(0,0,0))
        
        screen.fill((0,0,0))
        screen.blit(bg_surface, (i, 0))
        screen.blit(bg, (1000+i, 0))
        screen.blit(text22,(50,50))
        screen.blit(text21,(200,50))
        if i == -1000:
            screen.blit(bg, (1000+i, 0))
            i=0
        i -= 2

        tc=pygame.time.get_ticks()
        if tc%500==0 and flying==True:
            score+=5
            
            print(score)
            pygame.display.update()
        #displaying lives and game over
        if col_count == 0:
            for j in range(850, 1024, 50):
                screen.blit(lives, (j,20))
        elif col_count == 1:
            for j in range(900,960,50):
                screen.blit(lives, (j,20))
        elif col_count == 2:
            screen.blit(lives, (950,20))
        elif col_count == 3:
            print('Game Over')
            flying = False
            game_over = True
        while game_over:
                time.sleep(1)
                screen.blit(gm,(0,0))
                screen.blit(text1, (350, 180))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                sound.stop()
        enemy_x_pos -= enemy_speed
        if enemy_x_pos < -100:
            enemy_x_pos = 1024
            enemy_y_pos = randrange(40, 400)

        screen.blit(player,player_rect)
    

        if flying == True:
            enemy_rect = enemy.get_rect(topleft=(enemy_x_pos, enemy_y_pos))
            screen.blit(enemy, enemy_rect)
            player_speed += 0.5
            if player_speed > 5:
                player_speed = 5
            if player_rect.bottom < 533:
                player_rect.bottom += int(player_speed)

            # jump
            if pygame.mouse.get_pressed()[0] == 1:
                player_speed = -7

        current_time = pygame.time.get_ticks()
        #collision
        if current_time - last_col_time >= delay_time:
            if player_rect.colliderect(enemy_rect):
                col_count +=1
                print('collision')
                a= mixer.Sound("sound1.mp3")
                u=pygame.time.get_ticks()
                if u>3:
                    a.play()


                last_col_time = current_time


        #checking if player hit the ground
        if player_rect.bottom > 533:
            flying = False
            game_over = True
            col_count=3
            a = mixer.Sound("sound1.mp3")
            d=pygame.time.get_ticks()
            if d>3:
                a.play()
        pygame.display.update()       
        clock.tick(60)
pygame.quit()       
exit()