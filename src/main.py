import pygame, os, random, time

pygame.init()

width, height = 750, 600 
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Atlas's Voyage")

score = 450

#Sprites
##Debris
rock1 = pygame.image.load(os.path.join("assets", "rock1.png"))
##Spaceship
atlas = pygame.image.load(os.path.join("assets", "atlas.png"))
##Laser beam
laser = pygame.image.load(os.path.join("assets", "laser_beam.png"))
##Background
bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Background.png")),(width,height))
##Flaashing Text
flashing_text = pygame.image.load(os.path.join("assets", "ThoughtAcropolis.png"))

class spaceship:
    def __init__(self, x, y, health = 1):
        self.ship_sprite = atlas
        self.laser_sprite = laser
        self.x = x
        self.y = y
        self.laser_cooldown = 0
        self.mask = pygame.mask.from_surface(self.ship_sprite)
        self.max_health = health

    def draw_ship(self, window):
        window.blit(self.ship_sprite, (self.x, self.y))

# class debris():
#     def __init__(self, image, type):
#         self.image = image
#         self.type = type
#         self.rect = self.image[self.type].get_rect()
#         self.rect.y = height

#     def draw_ship(self, window):
#         window.blit(self.image[self.type], self.rect)

# class normalRock(debris):
#     def __init__(self, image):
#         self.type = random.randint(0, 2)
#         super().__init__(image, self.type)


def main():
    running = True
    FPS = 120
    clock = pygame.time.Clock()
    vel = 5
    player = spaceship(90, 365)
    surface = pygame.Surface((750, 600))
    speed = 3

    # score = 0

    #To get sprites onto window surface
    def draw():
        global score

        window.blit(surface,(0, 0))

        font = pygame.font.Font("assets\Aliens Among Us.ttf", 25)
        #Need to fix score adding system
        text_surface = font.render(f"Score: {score}", 1, (255,255,255))
        window.blit(text_surface, (10, 10))

        player.draw_ship(window)
            
        if score > 100 and score % 500 <= 100:
            window.blit(flashing_text, (300,200))


        pygame.display.update()
    
    global frames
    frames = 0

    def score_keeping():
            global score, frames

            if FPS/12 == frames:
                score += 1
                frames = 0

            frames += 1


    y = 0 

    while running:
        clock.tick(FPS)
        
        draw()

        score_keeping()

        #To check event in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #bg
        rel_y = y % bg.get_rect().height
        surface.blit(bg,(0, rel_y - bg.get_rect().height))
        if rel_y < height:
            surface.blit(bg,(0, rel_y))
            y += speed

        if score % 100 == 0:
            speed += 0.1
        
        if score > 100 and score % 1000 == 0:
            speed -= 1

            pygame.display.update()

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - vel > -220:
            player.x -= vel
        # vel + 5 = 5.4, this is so that the border spacing on the right side is the same as the left side
        if keys[pygame.K_d] and player.x + vel < 415:
            player.x += vel
        #elif so that by holding eg. d and left arrow keys together, player won't double in speed
        elif keys[pygame.K_LEFT] and player.x - vel > -220:
            player.x -= vel
        elif keys[pygame.K_RIGHT] and player.x + vel < 415:
            player.x += vel


main()
