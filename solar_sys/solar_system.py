import pygame
import math
pygame.init()

WIDTH, HEIGHT =  1200, 1012
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System _pre-alpha_")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
VENUS = (187, 122, 28)
JUPITER = (235, 167, 119)
SATURN = (190, 164, 118)
URANUS = (27, 194, 188)
NEPTUNE = (61, 80, 246)
PLUTO = (196, 146, 125)

class Planet:
    
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.i=0
        self.sun=False
        self.x_start=0
        self.points=[]

    def draw(self, win):
        x = self.x 
        y = self.y 
        if len(self.points) > 2:
            pygame.draw.lines(win, self.color, False, self.points, 1)
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def movement(planet):
        if planet.i <= 360 and planet.sun==False: 
                angle = planet.i * (3.14 / 180) 
                planet.x = (planet.x_start-WIDTH/2) * math.cos(angle) + WIDTH/2
                planet.y = (planet.x_start-WIDTH/2) * math.sin(angle) + HEIGHT/2
                planet.i += -planet.speed 
                planet.points.append((planet.x,planet.y))
        else:
            planet.i = 0 



def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(WIDTH/2, HEIGHT/2, 25, YELLOW, 0)
    sun.sun=True

    earth = Planet(WIDTH/2+200, HEIGHT/2, 8, BLUE, 1)
    earth.x_start=WIDTH/2+200

    mars = Planet(WIDTH/2+250, HEIGHT/2, 4, RED, 0.8)
    mars.x_start=WIDTH/2+250

    mercury = Planet(WIDTH/2+100, HEIGHT/2, 4, DARK_GREY, 1.6)
    mercury.x_start=WIDTH/2+100

    venus = Planet(WIDTH/2+150, HEIGHT/2, 7, VENUS, 1.17)
    venus.x_start=WIDTH/2+150

    jupiter = Planet(WIDTH/2+300, HEIGHT/2, 20, JUPITER, 0.43)
    jupiter.x_start=WIDTH/2+300

    saturn = Planet(WIDTH/2+350, HEIGHT/2, 16, SATURN, 0.33)
    saturn.x_start=WIDTH/2+350

    uranus = Planet(WIDTH/2+400, HEIGHT/2, 12, URANUS, 0.23)
    uranus.x_start=WIDTH/2+400

    neptune = Planet(WIDTH/2+450, HEIGHT/2, 11, NEPTUNE, 0.18)
    neptune.x_start=WIDTH/2+450

    pluto = Planet(WIDTH/2+500, HEIGHT/2, 2, PLUTO, 0.15)
    pluto.x_start=WIDTH/2+500

    planets = [sun,earth, mars, mercury, venus, jupiter, saturn, uranus, neptune, pluto]



    while run:
        clock.tick(30)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.movement()
            planet.draw(WIN)


            

        pygame.display.update()
    pygame.quit()


main()
