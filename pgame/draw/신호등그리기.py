import pygame
import random

pygame.init()

#3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

#4. pygame 무한루프
def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        
        pygame.draw.circle(screen, (255,0,0), (100, 100), 30)
        pygame.draw.circle(screen, (255,255,0), (100, 160), 30)
        pygame.draw.circle(screen, (0,255,0), (100, 220), 30)
        pygame.draw.rect(screen, (0, 0, 0), (40, 40, 120, 240),1)
        pygame.draw.line(screen,(0, 0, 0,), (100, 280), (100, 380), 1)
        pygame.display.update()

runGame()
# pygame.quit()