
from pygame import *
from random import *
lost = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image), (size_x, size_y))ншш
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 620:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            self.speed = randint(1, 2)
            lost = lost + 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
mixer.init()
font.init()
fire = mixer.Sound('fire.ogg')
win_width = 700
win_heigth = 500
window = display.set_mode((win_width, win_heigth))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_heigth))
mixer.music.load('space.ogg')
mixer.music.play()
font1 = font.SysFont(None, 36)
font2 = font.SysFont(None, 70)
youlose = font2.render('YOU LOSE!', True, (255, 255, 255))
rocket = Player('rocket.png', 5, win_heigth - 100, 80, 100, 7)
ufos = sprite.Group()
ufo1 = Enemy('ufo.png', randint(0, 600), 10, 100, 60, randint(1, 2))
ufo2 = Enemy('ufo.png', randint(0, 600), 10, 100, 60, randint(1, 2))
ufo3 = Enemy('ufo.png', randint(0, 600), 10, 100, 60, randint(1, 2))
ufo4 = Enemy('ufo.png', randint(0, 600), 10, 100, 60, randint(1, 2))
ufo5 = Enemy('ufo.png', randint(0, 600), 10, 100, 60, randint(1, 2))
ufos.add(ufo1)
ufos.add(ufo2)
ufos.add(ufo3)
ufos.add(ufo4)
ufos.add(ufo5)
FPS = 120
clock = time.Clock()
game = True
finish = False
while game:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
         
        window.blit(background, (0, 0))
        lose = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
        win = font1.render('Счёт: 0', 1, (255, 255, 255))
        window.blit(lose, (10, 50))
        window.blit(win, (10, 20))
        rocket.update()
        ufos.update()
        rocket.reset()
        ufos.draw(window) 
        if lost >= 40:
            finish = True 
            window.blit(youlose, (200, 200))
        if score >= 100:
            window.blit(win, (200, 200))
            game = False
    display.update()
