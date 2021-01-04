import pygame
import random
import os
import sys

pygame.font.init()
pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Feel the beat')
pygame.display.set_icon(pygame.image.load('data/note.png'))


def msg(screen, text, color=(55, 55, 55), size=36, pos=(-1, -1)):
    if pos[0] == -1:
        pos = (screen.get_rect().centerx, pos[1])
    if pos[1] == -1:
        pos = (pos[0], screen.get_rect().centery)
    font = pygame.font.Font(None, size)
    text = font.render(text, 1, color)
    textpos = text.get_rect()
    textpos.centerx = pos[0]
    textpos.centery = pos[1]
    screen.blit(text, textpos)


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
    def __init__(self):
        super().__init__()
        self.loosing = []

    def play_jbr(self):
        song_jbr = load_sound('JBR.mp3')
        song_jbr.play()
        song_jbr.set_volume(0.3)

    def lose(self, name):
        pygame.mixer.stop()
        loosing1 = load_sound('Проигрыш (1).mp3')
        loosing2 = load_sound('Проигрыш (2).mp3')
        loosing3 = load_sound('Проигрыш (3).mp3')
        loosing = [loosing1, loosing2, loosing3]
        random.choice(loosing).play()


class Menu:
    Game.play_jbr('JBR')


class Tile:
    x = 0
    y = -700 // 5
    h = 1000 // 4 - 1
    len_ = 700 // 5
    flag = True

    def pos(self, name):
        self.x = name * 1000 // 4

    def update(self, screen):
        if self.flag:
            pygame.draw.rect(screen, (0, 0, 0),
                             [self.x, self.y, self.h, self.len_])
        else:
            pygame.draw.rect(screen, (180, 180, 180),
                             [self.x, self.y, self.h, self.len_])

    def click(self, position):
        if position[0] in range(self.x, self.h + self.x):
            if position[1] in range(self.y, self.len_ + self.y):
                self.flag = False
                return 0
        return 1


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    my_cursor_image = load_image('arrow.png')
    my_cursor = pygame.sprite.Sprite(all_sprites)
    my_cursor.image = my_cursor_image
    my_cursor.rect = my_cursor.image.get_rect()
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()
    map_ = [0, 1, 2, 1, 1, 2, 3, 3, 2, 1, 2, 3, 3, 1, 2, 3, 1, 0, 2, 3, 1, 0,
            1, 2, 3, 0, 1, 2, 3]
    lost = 0
    time = 0
    delta = 60
    sb = []
    speed = 5
    score = 0
    while lost == 0:
        for i in map_:
            sb.append(Tile())
            sb[-1].pos(i)
            if lost != 0:
                break
            for j in range(700 // (5 * speed)):
                time += 1 / delta
                clock.tick(delta)
                screen.fill((224, 224, 255))
                if lost != 0:
                    break
                for k in range(len(sb)):
                    try:
                        sb[k].y += speed
                        sb[k].update(screen)
                        if sb[k].y > 700 - sb[k].len_ and sb[k].flag:
                            lost = 1
                    except:
                        pass
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or \
                            (event.type == pygame.KEYDOWN and event.key
                             == pygame.K_ESCAPE):
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        lost = sb[score].click(pygame.mouse.get_pos())
                        if lost != 0:
                            Game.lose('', '')
                        score += 1
                msg(screen, "СЧЁТ " + str(score), color=(0, 128, 255),
                    pos=(-1, 30))
                pygame.display.update()
        speed += 1
    pygame.mixer.music.stop()
    msg(screen, "ВЫ ПРОИГРАЛИ ", color=(110, 128, 225), size=100, pos=(-1, -1))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                my_cursor.rect.topleft = event.pos
        pygame.display.flip()
    pygame.quit()
