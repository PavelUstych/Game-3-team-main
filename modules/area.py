import pygame
import os
import modules.settings as settings
import modules.sprites as sprits


win_height = 800
win_width = 800

area_w = 100
area_h = 75
wir = 0


level_counter = 2
winwin = False
list_area_1 = [
    "000000031",
    "000000001",
    "500001111",
    "100000011",
    "111100001",
    "000000001",
    "000001111",
    "110000001",
    "000110001",
    "504000011",
    "111111111"
]

list_area_2 = [
    "000000031",
    "000000001",
    "500001111",
    "100000011",
    "111100001",
    "000000001",
    "000001111",
    "110000001",
    "000110001",
    "504000011",
    "111111111"
]

list_area_3 = [
    "000000031",
    "000000001",
    "500001111",
    "100000011",
    "111100001",
    "000000001",
    "000001111",
    "110000001",
    "000110001",
    "504000011",
    "111111111"
]

list_area_4 = [
    "000000031",
    "000000001",
    "500001111",
    "100000011",
    "111100001",
    "000000001",
    "000001111",
    "110000001",
    "000110001",
    "504000011",
    "111111111"
]

list_create_area = []
list_rect = []
class Area(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def draw_rect(self, win, rect):
    #     pygame.draw.rect(win, self.COLOR, rect)

def create_area(level):
    x = 0
    y = 0
    list_create_area = []
    list_rect = []
    for string in level:
        for el in string:
            if el == "1":
                area = Area(
                    x= x,
                    y= y,
                    width= area_w,
                    height= area_h,
                    color= (255, 165, 0),
                    name_image= ("images/platforms/pl4.png")
                )
                list_create_area.append(area)
                list_rect.append(area.RECT)
            elif el == "3":
                portal_area = Area(
                    x= x,
                    y= y,
                    width= 100,
                    height= 150,
                    color= (20, 30, 10),
                    name_image= ("images/platforms/portal.png.png")
                )
                list_create_area.append(portal_area)
                list_rect.append(portal_area.RECT)
            elif el == "4":
                sprits.sprite.X = x
                sprits.sprite.Y = y
                sprits.sprite.RECT.x = x
                sprits.sprite.RECT.y = y
            x += area_w
        x = 0
        y += area_h
    return list_rect, list_create_area




