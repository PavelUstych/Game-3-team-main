import pygame
import os
import random

import modules.sprites as sprites
import modules.bullet as bullet
import modules.heart as heart

win_height = 800
win_width = 800

list_start_pos = [
    [0, -75, "R"],
    [750, -75, "L"]
]


class Enemy(sprites.Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.COUNT_MOVE = 0
        self.STEP = 2
        # self.RANGE_MOVE = 320
        self.COUNT_BULLET = 0
        self.LIST_BULLET = []
        
         
    def gravity(self, list_rect):
        super().gravity("player/1.png",list_rect)     

    #
    def move_enemy(self, list_rect, name_folder, count_while, last_img, first_img):
        # print(self.X)
        # print(self.Y)
        if self.RECT.x + self.RECT.width <= 0 or self.RECT.x >= win_width:
            list_cor = random.choice(list_start_pos)
            self.RECT.x = list_cor[0]
            self.X = list_cor[0]
            self.RECT.y = list_cor[1]
            self.Y = list_cor[1]
            self.DIRECTION = list_cor[2]
            self.direction()
            if self.DIRECTION == "L":
                self.CAN_MOVE_RIGHT = False
            if self.DIRECTION == "R":
                self.CAN_MOVE_LEFT = False
        if not self.ACTIVE_GRAVITY:
            if not self.CAN_MOVE_LEFT:
                self.DIRECTION = "R"
                self.can_move_right(list_rect)
                self.X += self.STEP
                self.RECT.x = self.RECT.x + self.STEP
            if not self.CAN_MOVE_RIGHT:
                self.DIRECTION = 'L'
                self.can_move_left(list_rect)
                self.X -= self.STEP
                self.RECT.x = self.RECT.x - self.STEP 

            self.animation(folder= name_folder,count_while= count_while,last_img= last_img, first_img=first_img)
            
            
        # if self.DIRECTION == "R" or self.DIRECTION == "L":
        #     if name_sprite.RECT.collidepoint((self.RECT.x, self.RECT.y)):
        #         heart.count_heart -= 1
                
                

    def shoot(self, win, count_while, list_rect, width, height, name_sprite):
        self.COUNT_BULLET += 1
        derection = 1
        if self.DIRECTION == "L":
            derection = -1
            width = 0
        if self.COUNT_BULLET % count_while == 0 and len(self.LIST_BULLET) < 1:
            bullet1 = bullet.Bullet(
                x = self.X + width,
                y = self.Y + height,
                width= 20,
                height= 10,
                name_image= "images/bullet/1.png",
                color= (255,0,0)
            )
            bullet1.load_image(True)
            self.LIST_BULLET.append(bullet1)

        if self.LIST_BULLET:
            for bullet1 in self.LIST_BULLET:
                bullet1.blit_sprite(win)
                bullet1.move_bullet(list_rect, name_sprite, derection)
                if bullet1.MOVE_BULLET == False:
                    self.LIST_BULLET.remove(bullet1)
                #     print("5")
                # print(bullet1.MOVE_BULLET)
enemy1 = Enemy(
    width = 80,
    height = 75,
    x = 800,
    y = 0,
    name_image = "images/robot/1.png",
    color= (255, 0, 0)
)
# боты которые стоят на месте
enemy2 = Enemy(
    width = 80,
    height = 75,
    x = 0,
    y = 0,
    name_image = "images/robot/1.png",
    color= (255, 0, 0)
)
enemy3 = Enemy(
    width = 80,
    height = 75,
    x = 0,
    y = 550,
    name_image = "images/robot/1.png",
    color= (255, 0, 0)
)
# enemy3.load_image(direction=True)
enemy4 = Enemy(
    width = 55,
    height = 65,
    x = 800,
    y = 0,
    name_image = "images/robot_shoot/1.png",
    color= (255, 0, 0)
)

enemy5 = Enemy(
    width = 55,
    height = 65,
    x = 800,
    y = 0,
    name_image = "images/robot_shoot/1.png",
    color= (255, 0, 0)
)


enemy6 = Enemy(
    width = 55,
    height = 65,
    x = 800,
    y = 0,
    name_image = "images/robot_shoot/1.png",
    color= (255, 0, 0)
)

enemy7 = Enemy(
    width = 55,
    height = 65,
    x = 800,
    y = 0,
    name_image = "images/robot_shoot/1.png",
    color= (255, 0, 0)
)

enemy8 = Enemy(
    width = 55,
    height = 65,
    x = 800,
    y = 0,
    name_image = "images/robot_shoot/1.png",
    color= (255, 0, 0)
)

enemy9 = Enemy(
    width = 55,
    height = 65,
    x = 800,
    y = 0,
    name_image = "images/robot_shoot/1.png",
    color= (255, 0, 0)
)
# enemy_rect_list = [enemy1.RECT, enemy2.RECT, enemy3.RECT, enemy4.RECT, enemy5.RECT]

# enemy_list = [enemy1, enemy2, enemy3]

enemy_list1 = [enemy1,enemy2,enemy3, enemy4, enemy5]
enemy_list2 = [enemy1,enemy2,enemy3, enemy4, enemy5, enemy6, enemy7]
enemy_list3 = [enemy1,enemy2,enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]
enemy_list4 = [enemy1,enemy2,enemy3, enemy4, enemy5,enemy6, enemy7, enemy8, enemy9]



