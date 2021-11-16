import pygame as py
from pygame.draw import rect
py.init()

#programIcon = py.image.load('')
#py.display.set_icon(programIcon)
py.display.set_caption("Atlas's Voyage")
screen = py.display.set_mode((720,480))

color = (255,0,0)
x = 100
y = 445
width = 30
height = 30

class spaceship:
    vel = 0.4
    def __init__(self):
        # self.color = (255,0,0)
        # self.x = 100
        # self.y = 445
        # self.width = 30
        # self.height = 30
        #Images of spaceship goes here
        # self.player = py.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
        pass

    
    def update(self,x,vel):
        keys = py.key.get_pressed()
        if keys[py.K_a] and x > vel + 5:
            x -= vel
        # vel + 5 = 5.4, this is so that the border spacing on the right side is the same as the left side
        if keys[py.K_d] and x < 720-self.width-5.4:
            x += vel
        #elif so that by holding eg. d and left arrow keys together, player won't double in speed
        elif keys[py.K_LEFT] and x > vel + 5:
            x -= vel
        elif keys[py.K_RIGHT] and x < 720-self.width-5.4:
            x += vel
    
    def draw(self, screen):
        screen.blit(self.player)

def main():
    player = spaceship()
    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        screen.fill((255,255,255))
        player.draw(screen)
        py.display.flip()

main()










py.quit()   