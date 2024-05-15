import pygame
from tkinter import Tk
pygame.init()


second_font = pygame.font.Font(None, 20) 

config = {
    'music_playing': False,
    'screen': pygame.display.set_mode((800, 400)),
    'window_screen': pygame.display.set_caption('Pixel Jumper'),
    'clock': pygame.time.Clock(),
    'test_font': pygame.font.Font('font/Pixeltype.ttf', 50),
    'second_font': pygame.font.Font(None, 30),
    'display_string': 'on' if False else 'off',  
    'score': 0,
    'life': 5,
}

    
def initalize_game(config):
    pygame.init()
    pygame.mixer.init()
    root = Tk()
    root.withdraw()
    screen = config['screen']
    clock = config['clock']
    test_font = config['test_font']
    second_font = config['second_font']
    window_screen = config['window_screen']

    return screen, clock, test_font, window_screen, second_font


def load_images(display_string, score, life, test_font, config):
    Sky_surf = pygame.image.load('graphics/Sky.png').convert()
    Background_surf = pygame.image.load('graphics/background.png').convert()
    snail_surf1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
    player_surf1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
    music_surf = second_font.render('Music: ' + display_string, False, 'LightBlue')
    game_score_surf = test_font.render(str(score), False, 'LightBlue')
    lifes_surf = test_font.render(str(life), False, 'LightBlue')
    score_surf = test_font.render('Score:', False, 'LightBlue')
    lives_surf = test_font.render('Lives: ', False, 'LightBlue')
    Paused_surf = test_font.render('Paused', False, 'Black')
    
    return Sky_surf, Background_surf, snail_surf1, player_surf1, music_surf, game_score_surf, lifes_surf, score_surf, lives_surf, Paused_surf


def variables(test_font, second_font, config):
    display_string = 'on' if config['music_playing'] else 'off' 
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
    
    return paused, y_velocity, on_ground, collision_immune, collision_time, point_immune, point_time, gravity, player_moveable, snail_moveable, keys, keydown


