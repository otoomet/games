import pygame as pg
import random as r
pg.init()
pg.mixer.init()
pic = pg.image.load("hullmyts.png")
pic2 = pg.image.load("hullmyts2.png")
star = pg.image.load("star.png")
pg.font
screen = pg.display.set_mode((0,0), pg.RESIZABLE)
screenw = screen.get_width()
screenh = screen.get_height()
pg.display.set_caption("movepic")
do = True
dist = 5
mup = False
mdown = False
mleft = False
mright = False
mup2 = False
mdown2 = False
mleft2 = False
mright2 = False
timer = pg.time.Clock()
lifes = 5
lifes2 = 5
font = pg.font.SysFont("Times", 24)
dfont = pg.font.SysFont("Times", 32)
pfont = pg.font.SysFont("Times", 50)
pause = False
gameover = False
player = pg.sprite.Group()
player2 = pg.sprite.Group()
stars = pg.sprite.Group()
class Player(pg.sprite.Sprite):
    def __init__(self,x,y,img):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self, mup, mdown, mleft, mright):
        if self.rect.y <= 0:
            up = False
        else:
            up = True
        if self.rect.y >= screenh-120:
            down = False
        else:
            down = True
        if self.rect.x <= 0:
            left = False
        else:
            left = True
        if self.rect.x >= screenw-148:
            right = False
        else:
            right = True
        if mup and up:
            self.rect.y -= dist 
        if mdown and down:
            self.rect.y += dist
        if mleft and left:
            self.rect.x -= dist
        if mright and right:
            self.rect.x += dist
class Star(pg.sprite.Sprite):
    def __init__(self,x,y,vx,vy):
        pg.sprite.Sprite.__init__(self)
        self.image = star
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
def reset():
    lifes = 5
    player.empty()
    hullmyts = Player(screenw/2,screenh/2)
    player.add(hullmyts)
hullmyts = Player(screenw/2,screenh/2,pic)
player.add(hullmyts)
hullmyts2 = Player(screenw/2,screenh/2-100,pic2)
player2.add(hullmyts2)
while do:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            do = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                mup = True
            elif event.key == pg.K_DOWN:
                mdown = True
            elif event.key == pg.K_LEFT:
                mleft = True
            elif event.key == pg.K_RIGHT:
                mright = True
            elif event.key == pg.K_w:
                mup2 = True
            elif event.key == pg.K_s:
                mdown2 = True
            elif event.key == pg.K_a:
                mleft2 = True
            elif event.key == pg.K_d:
                mright2 = True
            elif event.key == pg.K_p:
                pause = True
            elif event.key == pg.K_r:
                reset()
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                mup = False
            elif event.key == pg.K_DOWN:
                mdown = False
            elif event.key == pg.K_LEFT:
                mleft = False
            elif event.key == pg.K_RIGHT:
                mright = False
            elif event.key == pg.K_w:
                mup2 = False
            elif event.key == pg.K_s:
                mdown2 = False
            elif event.key == pg.K_a:
                mleft2 = False
            elif event.key == pg.K_d:
                mright2 = False
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pause = False
                do = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pause = False
        pd = "PAUSED"
        ptext = dfont.render(pd, True, (127,127,127))
        ptext_rect = ptext.get_rect()
        ptext_rect.centerx = screen.get_rect().centerx
        ptext_rect.y = 50
        screen.blit(ptext,ptext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
    if lifes == 0:
        uded = "GAME OVER"
        dtext = dfont.render(uded, True, (255,0,0))
        dtext_rect = dtext.get_rect()
        dtext_rect.centerx = screen.get_rect().centerx
        dtext_rect.y = 30
        screen.blit(dtext,dtext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
        gameover = True
    while gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = False
                do = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    gameover = False
                    reset()
    screen.fill((128,128,128))
    score = ("Lifes: " + str(lifes))
    text = font.render(score, True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx-200
    text_rect.y = 10
    screen.blit(text,text_rect)
    score = ("Lifes: " + str(lifes2))
    text = font.render(score, True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx+200
    text_rect.y = 10
    screen.blit(text,text_rect)
    player.update(mup,mdown, mleft, mright)
    player.draw(screen)
    player2.update(mup2,mdown2, mleft2, mright2)
    player2.draw(screen)
    pg.display.update()
    timer.tick(60)

pg.quit()
