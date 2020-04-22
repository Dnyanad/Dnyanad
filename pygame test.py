import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("PYGAME TEST")

x = 250
y = 250
width = 50
height = 50
vel = 5

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -=vel
    if keys[pygame.K_RIGHTT]:
        x +=vel
    if keys[pygame.K_UP]:
        y -=vel
    if keys[pygame.K_DOWN]:
        y +=vel
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update
pygame.quit
    