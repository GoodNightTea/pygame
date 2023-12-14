import pygame
from sys import exit
import time

#todo sound system mit pycdio 2.1.1

# Constants
GROUND = 300
GRAVITY = 1
JUMP = -20

# Initialize pygame
pygame.init()

# Create display surface
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Jumper')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Load images
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

snail_surf1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect1 = snail_surf1.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

#Loads stat
score_surf = test_font.render('Score:', False, 'LightBlue')
score_rect = score_surf.get_rect(center = (700, 100))

lives_surf = test_font.render('Lives: ', False, 'LightBlue')
lives_rect = lives_surf.get_rect(center = (700, 50) )

#pause screen
Paused_surf = test_font.render('Paused', True, 'Black')
Paused_rect = Paused_surf.get_rect(center = (400, 200))

# Variables
paused = False
score = 0
y_velocity = 0
on_ground = True
life = 5
collision_immune = True
collision_time = 0
point_immune = True
point_time = 0
gravity = 1
player_moveable = True
snail_moveable = True
keys = pygame.key.get_pressed()
keydown = pygame.KEYDOWN



while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()           
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground and paused == False:
                y_velocity = JUMP
                player_moveable = True
                on_ground = False
                print('jump')
            if event.key == pygame.K_s:
                screen.blit(Paused_surf,Paused_rect)
                print('paused')
                paused = not paused
                player_moveable = False
                snail_moveable = False
            
    # Update player's vertical position with gravity
    player_rect.y += y_velocity
    y_velocity += gravity
    
    if snail_moveable == True:
        snail_rect1.x -= 4
    else:
        snail_rect1.x += 0
    

    if not paused:  # Only allow movement if the game is not paused
        if keys[pygame.K_a]:
            if player_moveable:
                player_rect.x -= 8
        elif keys[pygame.K_d]:
            if player_moveable:
                player_rect.x += 8
        if keys[pygame.K_s]:
            if not event.type == pygame.KEYDOWN:
                snail_moveable = True
        
    #check if the player is on ground
    if player_rect.y >= 220:
        player_rect.y = 220
        y_velocity = 0
        on_ground = True

    if snail_rect1.right <= 0:
        snail_rect1.left = 800

    #check collision
    if player_rect.colliderect(snail_rect1) and not collision_immune:
        collision_immune = True
        collision_time = pygame.time.get_ticks()
        life -= 1
        snail_rect1.x += 4
        collision = True
    else:
        collision = False
    
    
    # Check collision immunity
    if collision_immune and pygame.time.get_ticks() - collision_time > 1500:
        collision_immune = False
    
    elif player_rect.x > snail_rect1.x and not point_immune:
        if player_rect.y < snail_rect1.y -50:   
            score +=1
            point_immune = True
            point_time = pygame.time.get_ticks()
        else:
            point_immune = False
            
    #check point immunity
    if point_immune and pygame.time.get_ticks() - point_time > 2300:
        point_immune = False  

    if life < 1:
        snail_rect1.right += 4
        on_ground = False
        
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, GROUND))
    screen.blit(score_surf,score_rect)
    screen.blit(lives_surf, lives_rect)
    screen.blit(snail_surf1, snail_rect1)
    screen.blit(player_surf, player_rect)

    game_score_surf = test_font.render(str(score), False, 'LightBlue')
    game_score_rect = score_surf.get_rect(center = (810, 102))
    
    screen.blit(game_score_surf, game_score_rect)
    
    lifes_surf = test_font.render(str(life), False, 'LightBlue')
    lifes_rect = lifes_surf.get_rect(center = (760, 50))
    screen.blit(lifes_surf, lifes_rect)
    
    pygame.display.update()
    
    clock.tick(60)

