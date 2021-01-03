import pygame
import os
import sys


pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Feel the beat')


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_sound(name):
    if not pygame.mixer or not pygame.mixer.get_init():
        pass
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error:
        print(f'Файл со звуком "{sound}" не найден')
    return sound


class Menu(object):
    pass


class Game(object):
    load_sound('JBR')


if __name__ == '__main__':
    screen.fill((255, 255, 255))
    all_sprites = pygame.sprite.Group()

    my_cursor_image = load_image('arrow.png')
    my_cursor = pygame.sprite.Sprite(all_sprites)
    my_cursor.image = my_cursor_image
    my_cursor.rect = my_cursor.image.get_rect()

    pygame.mouse.set_visible(False)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                my_cursor.rect.topleft = event.pos
        screen.fill((0, 0, 0))
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
