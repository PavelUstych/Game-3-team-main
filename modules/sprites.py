import pygame
import os
import modules.settings as settings
import modules.area as area


# pygame.init()
# nac = 1
win_height = 800
win_width = 800
#
# 6. Створити клас Sprite, в методі init задати 5 параметрів зі значенням за замовчуванням None
class Sprite(settings.Settings):
    def __init__(self, **kwargs):        
        # крок з яким буде рухатись спрайт 
        super().__init__(**kwargs)
        self.STEP = 3
        # швідкість зміни костюмів спрайта
        self.SPEED_ANIMATION = 0
        # властивість, що відповідає за номер костюма, для анімації бігу 
        self.COUNT_IMG = 5
        #
        self.FIX_COLLISION = True
        # флаг, що вказує напрямок руху спрайта
        self.DIRECTION = "R"
        #
        self.GRAVITY = 6
        self.ACTIVE_GRAVITY = False
        #
        self.CAN_MOVE_RIGHT = True
        #
        self.CAN_MOVE_LEFT = False
        #
        self.KEY_PRESSED = False
        #
        self.flag_attack = False
        #
        self.COUNT_ATTACK = 14
        #
        self.COUNT_JUMP = 0
        self.JUMP = False
    # Метод руху спрайта вліво та вправо 
    def move_sprite(self, list_rect):
        # отримуємо кортеж всіх ключів кнопок 
        event = pygame.key.get_pressed()
        # умова, що відповідає за рух спрайта у праву сторону        
        if event[pygame.K_RIGHT] and self.RECT.x + self.WIDTH <= win_width and self.flag_attack == False:
            self.DIRECTION = 'R' # задаємо напрямок руху
            if self.CAN_MOVE_RIGHT:
                self.can_move_right(list_rect)
                self.X += self.STEP
                self.RECT.x = self.RECT.x + self.STEP
            self.animation(folder= "player",count_while=3,last_img= 8, first_img=4) # метод класу, що виконує анімацію бігу спрайту
        elif event[pygame.K_LEFT] and self.RECT.x + 10 >= 0 and self.flag_attack == False:      
            self.DIRECTION = 'L'

            if self.CAN_MOVE_LEFT:
                self.X -= self.STEP
                self.RECT.x = self.RECT.x - self.STEP

            self.animation(folder= "player",count_while=4,last_img= 8, first_img=4)
        # умова, що відповідає за спокійний стан спрайта - спарайт стоїть на місці\
        elif event[pygame.K_e] and self.flag_attack == False:
            self.flag_attack = True
        else:
            if self.flag_attack == False:
                self.NAME_IMAGE = "images/player/1.png"
                self.direction()
        if self.flag_attack:
            self.NAME_IMAGE = f"images/player/{self.COUNT_ATTACK}.png"
            self.direction() # задаємо напрямок по горизонталі зображення 
            if self.COUNT_ATTACK == 17:
                self.flag_attack = False
                self.COUNT_ATTACK = 14
            self.COUNT_ATTACK += 1
    # def can_kill_enemy(self, name_enemy):
    #     if self.flag_attack == True:
    #         print(1)
    #         sword = pygame.Rect(self.X + self.WIDTH, self.Y, 60, 90)
    #         if pygame.Rect.colliderect(sword, name_enemy) == True:
                
    #             print(2)
#   
    def can_move_right(self, list_rect):        
        for block in list_rect:
            # нижняя точка y cпрайта
            if self.RECT.y + self.RECT.height - 10 < block.y + block.height and self.RECT.y + self.RECT.height - 10 > block.y:
                #
                if self.RECT.x + self.RECT.width > block.x and self.RECT.x < block.x:
                    self.CAN_MOVE_RIGHT = False
                    self.X -= 3
                    self.RECT.x -= 3
                    break
                else:
                    self.CAN_MOVE_RIGHT = True
            else:
                self.CAN_MOVE_RIGHT = True
    #       
    def can_move_left(self, list_rect):
        for block in list_rect:
            if self.DIRECTION == "L":
                # нижняя точка y cпрайта
                if self.RECT.y + self.RECT.height - 10 < block.y + block.height and self.RECT.y + self.RECT.height - 10 > block.y:
                    #
                    if self.RECT.x < block.x + block.width and self.RECT.x + self.RECT.width > block.x + block.width:
                        self.CAN_MOVE_LEFT = False
                        self.X += 3
                        self.RECT.x += 3
                        break
                    else:
                        self.CAN_MOVE_LEFT = True
                else:
                    self.CAN_MOVE_LEFT = True
    #
    def can_move_up(self, list_rect):
        for block in list_rect:
            if block.x <= self.RECT.x and block.x + block.width >= self.RECT.x:
                if self.RECT.colliderect(block) and block.y + block.height > self.RECT.y:
                    self.COUNT_JUMP = 41
                    self.ACTIVE_GRAVITY = True
            if block.x <= self.RECT.x + self.RECT.width and block.x + block.width >= self.RECT.x + self.RECT.width:
                if self.RECT.colliderect(block) and block.y + block.height > self.RECT.y:
                    self.COUNT_JUMP = 41
                    self.ACTIVE_GRAVITY = True
    #
    def can_move_down(self, list_rect):
        for block in list_rect:
            block = pygame.Rect(block.x, block.y, block.width, 1)
            if self.RECT.colliderect(block):
                self.ACTIVE_GRAVITY = False
                self.COUNT_JUMP = 0
                self.FIX_COLLISION = True
                self.KEY_PRESSED = False
                if self.FIX_COLLISION:
                    self.Y = block.y - self.HEIGHT
                    self.FIX_COLLISION = False
                break
            else:
                self.ACTIVE_GRAVITY = True
                
    def jump(self, list_rect):
        event = pygame.key.get_pressed()
        #
        if event[pygame.K_UP] and self.KEY_PRESSED == False:
            self.KEY_PRESSED = True
        #
        if self.KEY_PRESSED and self.COUNT_JUMP <= 40:
            self.JUMP = True
            self.COUNT_JUMP += 1
            self.RECT.y -= 11
            self.Y -= 12
            self.can_move_up(list_rect)
            self.NAME_IMAGE = "images/player/11.png"
            self.direction()
        if self.COUNT_JUMP > 40:
            self.JUMP = False
    # Метод, що виконує анімацію спрайта під час руху вправо та вліво
    def animation(self,folder= None, count_while= None, last_img= None, first_img= None):
        self.SPEED_ANIMATION += 1
        # Якщо залішок від ділення  значення self.SPEED_ANIMATION на 5 буде = 0, то буде задаватись новий номер зображення 
        if self.SPEED_ANIMATION % count_while == 0:
            if self.COUNT_IMG == last_img:
                self.COUNT_IMG = first_img
            self.NAME_IMAGE = f"images/{folder}/{self.COUNT_IMG}.png"
            self.direction() # задаємо напрямок по горизонталі зображення 
            self.COUNT_IMG += 1 # задаємо наступний номер зображення

    # Метод, що задає напрямок для спрайта по горизонталі
    def direction(self):
        if self.DIRECTION == 'R':
            self.load_image()
        elif self.DIRECTION == 'L':
            self.load_image(direction=True)
    # 
    def gravity(self, folder= "player/12.png", list_rect= None):
        self.can_move_down(list_rect)
        if self.ACTIVE_GRAVITY:
            self.Y += self.GRAVITY
            self.RECT.y = self.RECT.y + self.GRAVITY
        
        
                
        
sprite = Sprite(
        width = 50,
        height = 75,
        x = 91,
        y = 690,
        name_image = "images/player/1.png",
        color= (255, 0, 0)
    )

sprite.RECT.width = 20
# sprite.RECT.height = 120
sprite.RECT.x = sprite.X + sprite.WIDTH // 2 - sprite.RECT.width // 2
# sprite.RECT.y = sprite.Y + sprite.HEIGHT // 2 - sprite.RECT.height // 2 