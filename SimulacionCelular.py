import pygame
import math
import random

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1380

FACTOR = 5

class Planet:
    def __init__(self, nombre, radio, distancia, angulo, color):
        self.name = nombre
        self.radius = radio
        self.distance = distancia
        self.angle = angulo
        self.color = color

    def paint(self, screen):
        center_x = int(SCREEN_WIDTH / 2)
        center_y = int(SCREEN_HEIGHT / 2)
        x = round(self.distance * math.cos(self.angle) + center_x)
        y = round(self.distance * math.sin(self.angle) + center_y)
        pygame.draw.circle(screen, self.color, (x, y), self.radius)
        font = pygame.font.Font(None, 20)
        text = font.render(self.name, 1, (255, 255, 255))
        screen.blit(text, (x - 30, y - 30))



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    done = False

    clock = pygame.time.Clock()

    mercury = Planet(nombre="Mercurio", radio=2, distancia=257 / FACTOR, angulo=random.randint(0, 360), color=(200, 200, 200))
    # 6051
    venus = Planet("Venus", 6 / FACTOR, 308 / FACTOR, random.randint(0, 360), (127, 127, 127))
    # 6371
    earth = Planet("Tierra", 6 / FACTOR, 349 / FACTOR, random.randint(0, 360), (0, 255, 255))
    # 3389
    mars = Planet("Marte", 3 / FACTOR, 527 / FACTOR, random.randint(0, 360), (255, 0, 0))
    # 69911
    jupiter = Planet("Jupiter", 69 / FACTOR, 978 / FACTOR, random.randint(0, 360), (100, 40, 0))
    # 58232
    saturn = Planet("Saturno", 58 / FACTOR, 1684 / FACTOR, 0, (115, 0, 0))
    # 25362
    uranus = Planet("Urano", 25 / FACTOR, 3071 / FACTOR, 0, (200, 200, 200))
    # 24622
    neptune = Planet("Neptuno", 24 / FACTOR, 4695 / FACTOR, 0, (0, 0, 255))

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    done = True

        screen.fill((0, 0, 0))

        pygame.draw.circle(screen, (random.randint(240, 255), random.randint(240, 255), 0),
                           (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)), SCREEN_WIDTH/25)

        for p in planets:
            p.angle = p.angle + 0.01
            p.paint(screen)

        pygame.display.flip()
        clock.tick(40)
