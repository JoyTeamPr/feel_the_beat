import pygame

pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Feel the beat')

if __name__ == '__main__':
    pygame.mouse.set_visible(False)
    running = True
    while running:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
    pygame.quit()
