import sys
import pygame as pg
from pygame import Rect
from pygame.math import Vector2
from pygame.sprite import Group
from scripts.entities import PhysicsEntity, JitterSquare
from scripts.utils import load_image, sheet_to_sprite
from scripts.tilemap import Tilemap


class MainClass:
    def __init__(self):
        pass
        # initialize
        pg.init()
        # enable screen
        self.screen = pg.display.set_mode((1280, 960))
        self.display = pg.Surface((640, 480))

        pg.display.set_caption("test")
        self.clock = pg.time.Clock()

        self.movement = Vector2(0, 0)
        self.movement_speed = 3
        self.collision_obstacle = Rect(50, 50, 300, 50)
        self.assets = {
            "fighter": load_image("art/sword_guy.png"),
            "wizard": load_image("art/wand_guy.png"),
            "skeleton": load_image("art/skeleton.png"),
            "dirt": load_image("art/dirt.png"),
            "gravestone": load_image("art/gravestone.png"),
            "tomato": load_image("art/tomato.png"),
        }
        self.player = PhysicsEntity(
            self,
            "player",
            Vector2(50, 50),
            self.assets["wizard"].get_size(),
            self.assets["wizard"],
        )
        # ground_sheet = load_image("art/ground.png")
        # self.empty_tile: Rect = sheet_to_sprite(ground_sheet, Rect(0, 0, 34, 20))
        # self.empty_tile_rect = self.empty_tile.get_rect(center=(0, 0))
        # self.jitter_square = JitterSquare(self, pos=Vector2(300, 300))
        self.square_group = Group(
            JitterSquare(self, self.assets["skeleton"], self.player, Vector2(300, 300)),
            JitterSquare(self, self.assets["skeleton"], self.player, Vector2(280, 280)),
            JitterSquare(self, self.assets["skeleton"], self.player, Vector2(280, 200)),
            JitterSquare(self, self.assets["skeleton"], self.player, Vector2(200, 300)),
            JitterSquare(self, self.assets["skeleton"], self.player, Vector2(250, 310)),
            JitterSquare(self, self.assets["skeleton"], self.player, Vector2(330, 320)),
            JitterSquare(self, self.assets["skeleton"], self.player, Vector2(310, 340)),
            JitterSquare(self, self.assets["skeleton"], self.player, Vector2(325, 317)),
        )

        self.tilemap = Tilemap(
            self, [self.assets["dirt"], self.assets["tomato"]], (16, 16), (12, 10, 2)
        )
        self.tilemap.set_cell(0, 0, 0, 0)
        self.tilemap.set_cell(0, 0, 1, 1)

    def main(self):
        while True:
            # deltatime
            _delta = self.clock.get_time()
            # fill bg
            self.display.fill((14, 64, 128))
            # quit boilerplate. Consider moving to generic outer loop
            for event in pg.event.get():
                if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_F8
                ):
                    self.quit()
            # ----------main body------------#
            self.handle_key_input()

            pg.draw.rect(self.display, (40, 40, 40), self.collision_obstacle)

            # update entities
            self.player.update(self.movement)
            self.square_group.update()

            # draw bg
            self.tilemap.render(self.display)
            # draw entities
            self.square_group.draw(self.display)
            self.player.render(self.display)

            player_collision = pg.Rect(*self.player.pos, *self.player.size)
            if player_collision.colliderect(self.collision_obstacle):
                pg.draw.rect(self.display, (150, 20, 20), player_collision, 1)

            # ----------/main body------------#
            # redraws frame
            self.screen.blit(
                pg.transform.scale(self.display, self.screen.get_size()), (0, 0)
            )
            pg.display.update()
            self.clock.tick(60)

    def handle_key_input(self):
        keys = pg.key.get_pressed()
        self.movement = Vector2(0, 0)
        self.movement.x = keys[pg.K_RIGHT] - keys[pg.K_LEFT]
        self.movement.y = keys[pg.K_DOWN] - keys[pg.K_UP]

    def quit(self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    MainClass().main()
