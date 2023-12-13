import pygame
from sys import exit

# Constants
GROUND = 300
GRAVITY = 1
JUMP = -20

# Initialize pygame
pygame.init()

# Create display surface
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Load images
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

snail_surf1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect1 = snail_surf1.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

# Variables
score = 0
y_velocity = 0
on_ground = True
life = 5
collision_immune = True
collision_time = 0
point_immune = True
point_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                y_velocity = JUMP
                on_ground = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.x -= 5
    if keys[pygame.K_d]:
        player_rect.x += 5

    # Update player's vertical position with gravity
    player_rect.y += y_velocity
    y_velocity += GRAVITY
    snail_rect1.x -= 4

    # Check if the player is on the ground
    if player_rect.y >= GROUND:
        player_rect.y = GROUND
        y_velocity = 0
        on_ground = True

    if snail_rect1.right <= 0:
        snail_rect1.left = 800

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, GROUND))

    # ... (other blit calls)

    # Check for collisions and update game state
    # ...

    # Render score and lives
    game_score_surf = test_font.render(str(score), False, 'LightBlue')
    game_score_rect = game_score_surf.get_rect(center=(810, 102))
    screen.blit(game_score_surf, game_score_rect)

    lifes_surf = test_font.render(str(life), False, 'LightBlue')
    lifes_rect = lifes_surf.get_rect(center=(760, 50))
    screen.blit(lifes_surf, lifes_rect)

    pygame.display.update()
    clock.tick(60)
