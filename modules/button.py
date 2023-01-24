import pygame
import os

from modules.settings import *

# 
def check_mouse_cor(sprite,mouse_cor):
    if mouse_cor[0] > sprite.X and mouse_cor[0] < sprite.X + sprite.WIDTH and mouse_cor[1] > sprite.Y and mouse_cor[1] < sprite.Y + sprite.HEIGHT:
        return True

play_button = Settings(
    x = 150,
    y = 167,
    width= 500,
    height= 120,
    name_image= ("images/buttons/button_Play_ork_styl.png")
)

settings_button = Settings(
    x = 150,
    y = 370,
    width= 500,
    height= 120,
    name_image= ("images/buttons/button_Settings.png")
) 

exit_button = Settings(
    x = 0,
    y = 0,
    width= 50,
    height= 50,
    name_image= ("images/buttons/exit.png")
    
)

troll_button = Settings(
    x = 123,
    y = 221,
    width= 580,
    height= 349,
    name_image= ("images/buttons/troll_button.png")
    
)