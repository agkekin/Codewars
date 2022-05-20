import pygame as pg
import sys

pg.font.init()
sc = pg.display.set_mode((800, 600))

# здесь будут рисоваться фигуры
YELLOW = (225, 69, 0)
WHITE = (225, 225, 225)
pg.draw.rect(sc, YELLOW, (20, 20, 600, 400), 1)

f2 = pg.font.SysFont('Arial', 22)
text2 = f2.render("ДИСПЛ", False, WHITE)
sc.blit(text2, (25, 20))
sc.blit(text2, (100, 20))


pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1000)