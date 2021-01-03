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


class Game:
    def play_jbr(name):
        song_jbr = load_sound('JBR.mp3')
        song_jbr.play()
        song_jbr.set_volume(0.3)


class Menu:
    Game.play_jbr('JBR')


class Tile:
    def draw(self):
        pygame.draw.rect(screen, (1, 1, 1), (50, 50, 100, 160), 0)

    def clicked(self):
        if pos_mouse[0] in range(50, 100):
            if pos_mouse[1] in range(50, 160):
                pygame.draw.rect(screen, (44, 49, 54), (50, 50, 100, 160), 0)
                flag = True
        global flag


if __name__ == '__main__':
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                print(pos_mouse)
        screen.fill((255, 255, 255))
        Tile.draw('self')
        if flag:
            Tile.clicked('self')
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
