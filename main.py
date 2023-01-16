# 1. Імпортувати модуль pygame
import pygame 
#
import modules.area as area
import modules.settings as settings
import modules.sprites as sprites
import modules.enemy as enemys
import modules.heart as heart
import modules.button as button
# 3. Ініціалізувати налаштування pygameeeeeeeeeee
pygame.init()

win_height = 800
win_width = 800
 
 
 
 
def can_kill_enemy(list, enemy):
    if sprites.sprite.flag_attack == True:
        sword = pygame.Rect(sprites.sprite.X + sprites.sprite.WIDTH, sprites.sprite.Y, 60, 90)
        if sword.colliderect(enemy.RECT):
            list.remove(enemy)
            print(enemy)
# 4.Cтворюємо ігровое вікно з ім'ям win 
win = pygame.display.set_mode((win_width,win_height))
# 5. Задаємо назву ігрового вікна
pygame.display.set_caption("Advanture of man")
# 6. Створюємо основну функцію гри run_game:
def run_game():
    list_rect = []
    list_create_area = []
    scene = "menu"

    clock = pygame.time.Clock()
    
    # - задаємо змінну game, що відповідає за роботу циклу   
    game = True
    # - задаємо ігровий цикл while, 
    while game:
    # - задаємо умову закриття ігрового вікна,
        if scene == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_cor = pygame.mouse.get_pos()
                    if button.check_mouse_cor(button.play_button, mouse_cor):
                        scene = "lvl1"
                        list_rect,list_create_area = area.create_area(area.list_area_1)
            settings.start.blit_sprite(win)
            button.play_button.blit_sprite(win)
            # button.settings_button.blit_sprite(win)
    # - задіємо об'єкт sprite і викликаємо його метод blit_sprite(), малюємо зображення на ігровому вікні, в центрі екрану
        
        if scene == "lvl1":
            if sprites.sprite.X >= 600 and sprites.sprite.Y >= 0 and sprites.sprite.Y <= 100:
                scene = "lvl2"
                list_rect,list_create_area = area.create_area(area.list_area_2)
        if scene == "lvl2":
            if sprites.sprite.X >= 600 and sprites.sprite.Y >= 0 and sprites.sprite.Y <= 100:
                scene = "lvl3"
                list_rect,list_create_area = area.create_area(area.list_area_3)
        if scene == "lvl3":
            if sprites.sprite.X >= 600 and sprites.sprite.Y >= 0 and sprites.sprite.Y <= 100:
                scene = "lvl4"
                list_rect,list_create_area = area.create_area(area.list_area_4)
            # if not heart.game_over and not start_game:
        if "lvl" in scene:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            settings.fon1.blit_sprite(win)
            for el in list_create_area:
                el.blit_sprite(win)
            #
            heart.show_hearts(win)
            sprites.sprite.blit_sprite(win)

            #
            sprites.sprite.can_move_right(list_rect)
            sprites.sprite.can_move_left(list_rect)
            #
            sprites.sprite.move_sprite(list_rect)
            
            #           
            sprites.sprite.jump(list_rect)
            #
            sprites.sprite.gravity(list_rect= list_rect)
            if "lvl1" in scene:
                for el in enemys.enemy_list1:
                    el.blit_sprite(win)
                    el.move_enemy(list_rect, name_folder="robot_shoot", count_while= 4, last_img= 13, first_img= 2)
                    el.gravity(list_rect= list_rect)
                    el.shoot(win, 200, list_rect= list_rect, width=80, height=25, name_sprite= sprites.sprite)
                    can_kill_enemy(enemys.enemy_list1 ,el)
            
            if "lvl2" in scene:
                for el in enemys.enemy_list2:
                    el.blit_sprite(win)
                    el.move_enemy(list_rect, name_folder="robot_shoot", count_while= 4, last_img= 13, first_img= 2)
                    el.gravity(list_rect= list_rect)
                    el.shoot(win, 200, list_rect= list_rect, width=80, height=25, name_sprite= sprites.sprite)
                    can_kill_enemy(enemys.enemy_list2 ,el)
            
            if "lvl3" in scene:
                for el in enemys.enemy_list3:
                    el.blit_sprite(win)
                    el.move_enemy(list_rect, name_folder="robot_shoot", count_while= 4, last_img= 13, first_img= 2)
                    el.gravity(list_rect= list_rect)
                    el.shoot(win, 200, list_rect= list_rect, width=80, height=25, name_sprite= sprites.sprite)
                    can_kill_enemy(enemys.enemy_list3 ,el)
                    
            if "lvl4" in scene:
                for el in enemys.enemy_list4:
                    el.blit_sprite(win)
                    el.move_enemy(list_rect, name_folder="robot_shoot", count_while= 4, last_img= 13, first_img= 2)
                    el.gravity(list_rect= list_rect)
                    el.shoot(win, 200, list_rect= list_rect, width=80, height=25, name_sprite= sprites.sprite)
                    can_kill_enemy(enemys.enemy_list4 ,el)

            if heart.game_over:
                scene = "tulen"
        if scene == "tulen":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            settings.end.blit_sprite(win)
    # - задаємо оновлення ігрового екрану
        clock.tick(60)
        pygame.display.flip()
# 11. І найголовніше – викликаємо основну функцію гри
run_game()