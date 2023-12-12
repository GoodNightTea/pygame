import pygame
from sys import exit
import time


score = 0 
ground = 300
gravity = 1
jump = -20
y_velocity = 0
on_ground = True
collision = False
life = 5
collision = False
collision_immune = True
collision_time = 0
point_counted = False
dt = 0

# starts pygame and helps render sounds etc.
pygame.init()

# creates a display surface 800, 400
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

titel_surf = test_font.render('My Game :3', False, 'LightBlue')
titel_rect = titel_surf.get_rect(center = (400, 50))

snail_surf1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect1 = snail_surf1.get_rect(bottomright = (600, 300))

snail_surf2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_rect2 = snail_surf2.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

player_surf2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_rect2 = player_surf.get_rect(midbottom = (80,300))

player_standing = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_standing_rec = player_surf.get_rect(midbottom = (80,300))

lives_surf = test_font.render('Lives:', False, 'Black')
lives_rect = lives_surf.get_rect(center = (300, 50))

score_surf = test_font.render('Score:', False, 'Black')
score_rect = score_surf.get_rect(center = (425, 50))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                # Jump when space bar is pressed and the player is on the ground
                y_velocity = jump
                on_ground = False

    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_a]:
        player_rect.x -= 5
    else:
        screen.blit(player_standing, player_standing_rec)
    if keys[pygame.K_d]:
        player_rect.x += 5
    else:
         screen.blit(player_standing, player_standing_rec)
        
    point_counted = True
    
    if snail_rect1.right <= player_rect.left and not collision and not point_counted:
        score += 1
        point_counted = True
    elif snail_rect1.right > player_rect.left:
        point_counted = False
    
    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    screen.blit(score_surf,score_rect)
    screen.blit(lives_surf, lives_rect)
    
    # Update player's vertical position with gravity
    player_rect.y += y_velocity
    y_velocity += gravity
    snail_rect1.x -= 4
    
    # Check if the player is on the ground
    if player_rect.y >= 220:
        player_rect.y = 220
        y_velocity = 0
        on_ground = True
    
    if snail_rect1.right <=0: snail_rect1.left = 800
    
    screen.blit(snail_surf1, snail_rect1)
    screen.blit(player_surf, player_rect)

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
       
    elif snail_rect1.right <= 6:
        if collision_immune == False:
            score += 1
        
    
    if life < 1:
        snail_rect1.right += 4
        y_velocity = jump        
        
    game_score_surf = test_font.render(str(score), False, 'LightBlue')
    game_score_rect = score_surf.get_rect(center = (800, 50))
    screen.blit(game_score_surf, game_score_rect)
    lifes_surf = test_font.render(str(life), False, 'LightBlue')
    lifes_rect = lifes_surf.get_rect(center = (700, 50))
    screen.blit(lifes_surf, lifes_rect)

                                
    pygame.display.update()
    clock.tick(60)


