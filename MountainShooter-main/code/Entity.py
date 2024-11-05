#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        try:
            self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        except pygame.error:
            print(f"Erro: Imagem para '{name}' não encontrada em './asset/'.")
            raise
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH.get(self.name, 0)  
        self.damage = ENTITY_DAMAGE.get(self.name, 0)
        self.score = ENTITY_SCORE.get(self.name, 0)
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass
