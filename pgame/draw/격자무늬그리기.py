import pygame as pg
import random

pg.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

WHITE = (255, 255, 255)
size = [400,400]
screen =pg.display.set_mode(size)

done = False
clock = pg.time.Clock()

# 4. pygame 무한루프
def rungame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        
        for i in range(4): 
            pg.draw.line(screen, (255,0,0), (0,0), (0,(i+1)*100))
            # pg.draw.line(screen, (255,0,0), (0,0), ((i+1)*100,0))
        pg.display.update()




