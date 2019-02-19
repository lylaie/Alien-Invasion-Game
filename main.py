import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    window = pygame.display.set_mode((ai_settings.window_width, ai_settings.window_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(ai_settings, window)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, window, ship)

run_game()
