import pygame,sys,time,base64,os
from pygame.locals import *
from png_basketball import img as strawberry
from jpg_cxk import img as bing
from random import randint

strawberryFile = 'strawberryTmp.png'
bingFile = 'bingTmp.png'
def newTmpPic(file,data):
    tmp = open(file, 'wb+')
    tmp.write(base64.b64decode(data))
    tmp.close()
#加载临时图片
newTmpPic(strawberryFile,strawberry)
newTmpPic(bingFile,bing)
pygame.init()
# set up the window
WINDOWWIDTH = 500
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
strawberryImage = pygame.image.load(strawberryFile)
#加载完图片 删除临时文件
os.remove(strawberryFile)

bingImage = pygame.image.load(bingFile)
os.remove(bingFile)
bingStretchedImage = pygame.transform.scale(bingImage,(80,80))

strawberryStretchedImage = pygame.transform.scale(strawberryImage, (40, 40))
pygame.display.set_caption('Hello dear')
mainClock = pygame.time.Clock()
# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
MOVESPEED = 20

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# set up the block data structure
b1 = {'r': 20, 'color':RED, 'dir':UPRIGHT,'point':[300,50]}
b2 = {'r': 30, 'color':GREEN, 'dir':UPLEFT,'point':[300,0]}
b3 = {'r': 40, 'color':BLUE, 'dir':DOWNLEFT,'point':[300,500]}
blocks = [b1, b2, b3]
class Strawberry:
    def __init__(self,rect,speed):
        self.rect = rect
        self.speed = speed
    def getRect(self):
        return self.rect
    def getSpeed(self):
        return self.speed
bingImageRect = pygame.Rect(210, 320, 80, 80)      
strawberryImageRect = [Strawberry(pygame.Rect(randint(1,5) * 100, 100, 40, 40),randint(1,6)),Strawberry(pygame.Rect(randint(1,5) * 100, 100, 40, 40),randint(1,6))]
# set up fonts
basicFont = pygame.font.SysFont('SimHei', 48)


def isPointInsideCircle(x,y,block):
    x -= block['point'][0]
    y -= block['point'][1]
    if (x**2) + (y**2) < block['r']**2:
        print('true' + str(block['color']))
        return True
    else:
        return False
# set up the text
score = 0
tick = 40
text = basicFont.render('{}'.format(score),True,WHITE)
# textRect.centerx = windowSurface.get_rect().centerx
# textRect.centery = windowSurface.get_rect().centery

# draw the white background onto the surface
# windowSurface.fill(WHITE)

# draw a green polygon onto the surface
# pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236,277), (56, 277), (0, 106)))

# draw some blue lines onto the surface
# pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
# pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
# pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface
# pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# draw a red ellipse onto the surface
# pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# draw the text's background rectangle onto the surface
# pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get a pixel array of the surface
# pixArray = pygame.PixelArray(windowSurface)
# pixArray[480][380] = BLACK
# del pixArray

# draw the text onto the surface
# windowSurface.blit(text, textRect)

# draw the window onto the screen
# pygame.display.update()

def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False
def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
    # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True
    return False
moveLeft = False
moveRight = False
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveLeft = True
            if event.key == K_RIGHT:
                moveRight = True  
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONUP:
            for b in blocks:
                isPointInsideCircle(event.pos[0],event.pos[1],b)
    # draw the black background onto the surface
    windowSurface.fill(BLACK)
    # draw the window onto the screen
    if moveLeft:
        bingImageRect.left -= MOVESPEED
    if bingImageRect.left < 0:
        bingImageRect.left = 0
    if moveRight:
        bingImageRect.right += MOVESPEED
    if bingImageRect.right > WINDOWWIDTH:
        bingImageRect.right = WINDOWWIDTH
    if len(strawberryImageRect) < 10:
        strawberryImageRect.append(Strawberry(pygame.Rect(randint(0,460),0,40,40),randint(1,10)))
    for s in strawberryImageRect[:]:
        s.getRect().centery += s.getSpeed()
        if s.getRect().centery > WINDOWHEIGHT:
            strawberryImageRect.remove(s)
        elif  doRectsOverlap(s.getRect(),bingImageRect):
            score += 1
            if(score % 100 == 0):
                tick +=5
            text = basicFont.render('{}'.format(score),True,WHITE)
            strawberryImageRect.remove(s)
        windowSurface.blit(strawberryStretchedImage,s.getRect()) 
    windowSurface.blit(text, text.get_rect())
    windowSurface.blit(bingStretchedImage,bingImageRect)
    if score > 10000 :
        love = basicFont.render('I love u',True,WHITE)
        loveRect = love.get_rect()
        loveRect.centerx = 250
        loveRect.centery = 200
        windowSurface.blit(love, loveRect)
    pygame.display.update()
    mainClock.tick(tick)
Console.Readykey()