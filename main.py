import pygame
from sys import exit
from pygame import mixer
from tkinter import Tk, filedialog
from renderpy import initalize_game, load_images, variables


config = {
    'music_playing': False,
    'screen': pygame.display.set_mode((800, 400)),
    'clock': pygame.time.Clock(),
    'test_font': pygame.font.Font('font/Pixeltype.ttf', 50),
    'display_string': 'on' if False else 'off',  
    'score': 0,
    'life': 5,
}

score = config['score']
life = config['life']
display_string = 'on' if config['music_playing'] else 'off'

screen, clock, test_font = initalize_game(config)
sky_surf, ground_surf, snail_surf1, player_surf1, player_surf2, music_surf, game_score_surf, lifes_surf, score_surf, lives_surf, Paused_surf = load_images(display_string, score, life, test_font, config)
(player_last_switch_time, player_switch_interval, paused, y_velocity, on_ground, collision_immune, collision_time, point_immune, point_time, gravity, player_moveable, snail_moveable, keys, keydown) = variables(test_font, config)

# Constants
GROUND = 300
GRAVITY = 1
JUMP = -20  
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")])
    if file_path:
        play_music(file_path)

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()


snail_rect1 = snail_surf1.get_rect(bottomright=(600, 300))
player_surfaces = [player_surf1, player_surf2]
player_surface_index = 0
player_rect = player_surfaces[player_surface_index].get_rect(midbottom=(80, 300))
score_rect = score_surf.get_rect(center=(700, 100))
lives_rect = lives_surf.get_rect(center=(700, 50))
Paused_rect = Paused_surf.get_rect(center=(400, 200))


player_last_switch_time = pygame.time.get_ticks()
player_switch_interval = 1000


#music
on = True
off = False
music_playing = False

def select_file():
    print('asking for file path')
    music_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")])
    if music_file:
        print('found file path yipeee')
        music_playing = on
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground and not paused:
                y_velocity = JUMP
                player_moveable = True
                on_ground = False
                print('jumpin')
            if event.key == pygame.K_s:
                print('pausin')
                paused = not paused
                player_moveable = False
                snail_moveable = False
            if event.key == pygame.K_m:
                print('vibin')
                music_playing = True
                select_file()

    # player movement
    player_rect.y += y_velocity
    y_velocity += gravity
    
    if music_playing == True:
        display_music = 'on'
    else:
        display_music = 'off'
    
    if snail_moveable == True:
        snail_rect1.x -= 4
    else:
        snail_rect1.x += 0
    
    if not paused:
        if keys[pygame.K_a]:
            if player_moveable:
                player_rect.x -= 8
        elif keys[pygame.K_d]:
            if player_moveable:
                player_rect.x += 8
        if keys[pygame.K_s]:
            if not event.type == pygame.KEYDOWN:
                snail_moveable = True
    
    
    # updating player's character
    current_time = pygame.time.get_ticks()
    if current_time - player_last_switch_time > player_switch_interval:
        player_surface_index = (player_surface_index + 1) % len(player_surfaces)
        player_last_switch_time = current_time

    # movement


    # check if the player is on ground
    if player_rect.y >= 220:
        player_rect.y = 220
        y_velocity = 0
        on_ground = True

    if snail_rect1.right <= 0:
        snail_rect1.left = 800
        
    if life < 1:
        snail_rect1.right += 4
        on_ground = False

    # check collision
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
        if player_rect.y < snail_rect1.y - 50:
            score += 1
            point_immune = True
            point_time = pygame.time.get_ticks()
        else:
            point_immune = False
            
    #check point immunity
    if point_immune and pygame.time.get_ticks() - point_time > 2300:
        point_immune = False  


    if paused:
        screen.blit(Paused_surf,Paused_rect)
        
    if music_playing == True:
        display_music = 'on'
    else:
        display_music = 'off'
    
    display_string = 'on' if music_playing else 'off'
    music_surf = test_font.render('Music: ' + display_string, False, 'LightBlue')
    music_rect = music_surf.get_rect(center=(100, 50))
        
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, GROUND))
    screen.blit(score_surf, score_rect)
    screen.blit(lives_surf, lives_rect)
    screen.blit(snail_surf1, snail_rect1)
    screen.blit(player_surfaces[player_surface_index], player_rect)
    screen.blit(music_surf, music_rect)

    game_score_surf = test_font.render(str(score), False, 'LightBlue')
    game_score_rect = score_surf.get_rect(center = (810, 102))
    
    screen.blit(game_score_surf, game_score_rect)
    
    lifes_surf = test_font.render(str(life), False, 'LightBlue')
    lifes_rect = lifes_surf.get_rect(center = (760, 50))
    screen.blit(lifes_surf, lifes_rect)
    
    pygame.display.update()
    
    clock.tick(60)

