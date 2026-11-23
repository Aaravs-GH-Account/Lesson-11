import pygame,random
pygame.init()

score=0
S_W=500
S_H=800

screen=pygame.display.set_mode((S_W,S_H))

bckgrnd=pygame.image.load('background.png')
bckgrnd=pygame.transform.scale(bckgrnd,(S_W,S_H))

while True:
    screen.blit(bckgrnd,(0,0))
    pygame.display.update()

'''apple=pygame.image.load('apple.png')
apple=apple.transform.scale(apple(15,15))
def apple_fall():
    random.randint(20-480)'''