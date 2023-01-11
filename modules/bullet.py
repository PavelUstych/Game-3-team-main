import pygame
import modules.settings as settings
import modules.heart as heart


pygame.init()

class Bullet(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.STEP = 5
        self.MOVE_BULLET = False

    def move_bullet(self, list_rect, name_sprite, derection= 1):
        for block in list_rect:
            if block.x <= self.RECT.x + self.RECT.width and block.x + block.width > self.RECT.x + self.WIDTH:
                if self.RECT.y > block.y - self.RECT.height and self.RECT.y + self.RECT.height < block.y + self.RECT.height + block.height:
                    self.MOVE_BULLET = False
                    break
                else:
                    self.MOVE_BULLET = True
            else:
                self.MOVE_BULLET = True

        if self.MOVE_BULLET:
            if name_sprite.RECT.collidepoint((self.RECT.x, self.RECT.y)):
                self.MOVE_BULLET = False
                heart.count_heart -= 1
            else:
                self.MOVE_BULLET = True

        if self.RECT.x <= 0:
            self.MOVE_BULLET = False

        if self.MOVE_BULLET:
            self.RECT.x += self.STEP * derection
            self.X += self.STEP * derection