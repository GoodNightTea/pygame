import pygame
from sys import exit

# starts pygame and helps render sounds etc.
pygame.init()

# creates a display surface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('', False, 'LightBlue')
score_rect = score_surf.get_rect(center = (400, 50))

gameover_surf = pygame.image.load('Game_Over.png').convert()
gameover_rect = gameover_surf.get_rect(center = (402, 253))

snail_surf1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect1 = snail_surf1.get_rect(bottomright = (600, 300))

snail_surf2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_rect2 = snail_surf2.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))




# stops python from finishing the code
gravity = 1
jump = -15
y_velocity = 0
on_ground = True  # Flag to check if the player is on the ground

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

    # Update player's vertical position with gravity
    player_rect.y += y_velocity
    y_velocity += gravity
    
    snail_rect1.x -= 4
    
    # Check if the player is on the ground
    if player_rect.y >= 300:
        player_rect.y = 300
        y_velocity = 0
        on_ground = True
        
    
    if snail_rect1.right <=0: snail_rect1.left = 800
    screen.blit(snail_surf1, snail_rect1)
    screen.blit(player_surf, player_rect)
    
    #checks for collitions
    if player_rect.colliderect(snail_rect1):
         
         gameover_surf = test_font.render('Game Over :/', False, 'Red')
         gameover_rect = gameover_surf.get_rect(center = (400, 50))
         snail_rect1.x += 4
         #snail_rect1 = snail_surf1.get_rect(bottomright = (600, 500))
         #player_rect = player_surf.get_rect(midbottom = (500,600))
         score_rect = score_rect.move(80, 500)
         screen.blit(gameover_surf, gameover_rect)

    
    #checks for mouse pos and mouse clicks
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())
    
   
    pygame.display.update()
    clock.tick(60)
