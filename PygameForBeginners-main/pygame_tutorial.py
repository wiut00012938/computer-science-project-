import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

White = (255, 255, 255)

FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('PygameForBeginners-main','Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('PygameForBeginners-main','Assets', 'spaceship_yellow.png'))

def draw_window():
    WIN.fill(White)
    #draw a surface on the screen
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (300,100))
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    #quit the application itself while run = False clases the while run
    pygame.quit()
#functions that specifies where the main function will be work in terms of mentioning. If I execute the second phyton speed where the main function is mentioned, it will not be executed
if __name__ == "__main__":
    main()