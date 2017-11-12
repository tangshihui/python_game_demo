import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GamesStats
from button import Button


def run_game():
    pygame.init()

    ai_setting=Settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button=Button(ai_setting,screen,"Play")

    ship=Ship(ai_setting,screen)
    bullets=Group()
    aliens=Group()

    gf.create_fleet(ai_setting,screen,ship,aliens)
    stats=GamesStats(ai_setting)

    while True:
        gf.check_events(ai_setting,screen,stats,play_button,ship,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting,screen,ship,aliens,bullets)
            gf.update_aliens(ai_setting,stats,screen,ship,aliens,bullets)
        
        gf.update_screen(ai_setting,screen,stats,ship,aliens,bullets,play_button)


run_game()