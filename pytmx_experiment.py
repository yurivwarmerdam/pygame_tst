import sys
import pygame as pg
from pytmx.util_pygame import load_pygame


screen = pg.display.set_mode((1280, 960))
display = pg.Surface((640, 480))

# self.tmx_data = load_pygame("art/tmx/field.tmx")
# tile_group = pg.sprite.Group()


class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf, *groups):
        # pg.sprite.Sprite.__init__(self)
        super().__init__(*groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

class Tilemap():
    def __init__(self,tmx_file):
        self.tmx_data=load_pygame(tmx_file)
        pass

    for layer in self.tmx_data.visible_layers:

        if hasattr(layer, "data"):
            for x, y, surf in layer.tiles():
                pos = (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight)
                Tile(pos, surf, self)



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_F8):
            pg.quit()
            sys.exit()

    display.fill((14, 64, 128))

    tile_group.draw(display)

    screen.blit(pg.transform.scale(display, screen.get_size()), (0, 0))
    pg.display.update()
    pg.time.Clock().tick(60)
