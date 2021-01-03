import pygame

flag = False
wh = input().split(' ')
w = wh[0]
h = wh[1]
if not w.isdigit() or not h.isdigit():
    print('Неправильный формат ввода')
    flag = True


if __name__ == '__main__':
    if not flag:
        pygame.init()
        size = width, height = int(w), int(h)
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
    pygame.quit()
