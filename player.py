from global_param import *
import pygame
import math

class Player: # класс, описывающий игрока
    def __init__(self): # конструктор
        self.x, self.y = player_position # заполнение полей x и y
        self.angle = player_view_angle # заполнение поля угол камеры
        # Значения берутся из кортежей глобальных параметров
    
    def movement(self):
        sinA = math.sin(self.angle)
        cosA = math.cos(self.angle)
        keys = pygame.key.get_pressed() # получаем нажатые клавиши
        if keys[pygame.K_w]: # если нажат ключ W
            self.y += player_speed * sinA
            self.x += player_speed * cosA
        if keys[pygame.K_s]: # если нажат ключ S
            self.y += -player_speed * sinA
            self.x += -player_speed * cosA
        if keys[pygame.K_a]: # если нажат ключ A
            self.y += -player_speed * cosA
            self.x += player_speed * sinA
        if keys[pygame.K_d]: # если нажат ключ D
            self.y += player_speed * cosA
            self.x += -player_speed * sinA
        if keys[pygame.K_LEFT]: # если нажат ключ left_arrow
            self.angle -= 0.03
        if keys[pygame.K_RIGHT]: # если нажат ключ right_arrow
            self.angle += 0.03

    @property # возвращаем свойства объекта
    def get_coords(self): # геттер координат
        return (self.x, self.y)