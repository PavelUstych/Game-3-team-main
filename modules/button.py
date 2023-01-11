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
    name_image= ("images/buttons/button_Play.png")
)

# settings_button = Settings(
#     x = 150,
#     y = 370,
#     width= 500,
#     height= 120,
#     name_image= ("images/buttons/button_Settings.png")
# )   