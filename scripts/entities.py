import pygame as pg
from pygame.math import Vector2
from pygame import Surface
from random import randint, random


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size, sprite):
        self.game = game
        self.type = e_type
        self.pos = pos
        self.size = size
        self.sprite = sprite
        self.velocity = Vector2(0, 0)

    def update(self, input_movement=Vector2(0, 0)):
        frame_movement = input_movement + self.velocity

        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    def render(self, surface: Surface):
        surface.blit(self.sprite, self.pos)


class JitterSquare(pg.sprite.Sprite):
    def __init__(self, game, sprite: Surface, player: PhysicsEntity, pos=Vector2(0, 0)):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.rect = sprite.get_rect()
        self.rect.center = pos
        self.image = sprite
        self.player = player

        self.walking = False
        self.walk_goal = Vector2(0, 0)
        self.walk_speed = 1

    def update(self):
        # TODO: this might work better wiht some subpixel position precision.
        if not self.walking and random() < 0.01:
            self.walk_goal = self.player.pos + Vector2(
                randint(-50, 50), randint(-50, 50)
            )
            self.walk_speed = 0.75 + random() * 0.8
            self.walking = True
            return
        elif self.walking:
            self.rect.center = Vector2(self.rect.center).move_towards(
                self.walk_goal, self.walk_speed
            )
            if self.rect.center == self.walk_goal:
                self.walking = False
            return

    # def render(self, surface: Surface):
    #     pg.draw.rect(surface, pg.Color("cyan"), self.rect)
