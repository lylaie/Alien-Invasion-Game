import sys
import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    pygame.init()
    ai_settings = Settings()
    window = pygame.display.set_mode((ai_settings.window_width, ai_settings.window_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, window, "Play")
    

    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, window)
    sb = ScoreBoard(ai_settings, window, stats)

    bullets = Group()
    aliens = Group()
    
    gf.create_fleets(ai_settings, window, ship, aliens)

    while True:
        gf.check_events(ai_settings, window, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, window, stats, sb, ship, bullets, aliens)
            gf.update_aliens(ai_settings, window, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, stats, sb, window, aliens, ship, bullets, play_button)

run_game()
