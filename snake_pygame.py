import pygame
import sys
import random

screen_width = 600
screen_height = 800

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

light_green = (0,170,140)
dark_green = (0,140,120)
food_color = (250,200,0)
snake_color = (34,34,34)

up = (0,-1)
down = (0,1)
right = (1,0)
left = (-1,0)


class SNAKE:
    def __init__(self):
        self.position = [((screen_width/2),(screen_height/2))]
        self.length = 1
        self.direction = random.choice([up,down,left,right])
        self.color = snake_color ;
        self.scroe = 0
    def draw(self, surface):
        for p in self.positions:
            rect = pygame.Rect((p[0],p[1]),(gridsize,gridsize))
            pygame.draw.rect(surface,self.color,rect)
    def move(self):
        current = self.position[0]
        x,y =self.direction
        new = ((current[0]+(x*gridsize)),(current[1]+(y*gridsize)))

        if new[0] in range(0, screen_width) and new[1] in range(0, screen_width) and not new in self.position[2:]:
            

class Food:
    def __init__(self):
        self.position = (0,0)
        self.color = food_color
        self.random_position()
    def random_position(self):
        self.position = (random.randint(0,grid_width-1)*gridsize, random.randint(0,grid_height-1)*gridsize)
    def draw(self,surface):
        rect = pygame.Rect((self.position[0],self.position[1]),(gridsize,gridsize))
        pygame.draw.rect(surface,self.color,rect)

def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range (0, int(grid_width)):
            light = pygame.Rect((x*gridsize,y*gridsize),(gridsize,gridsize))
            pygame.draw.rect(surface,light_green,light)


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    font = pygame.font.SysFont("arial",20)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    food = FOOD()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255,0,0))
        rect = pygame.Rect(100,100,200,200)
        pygame.draw.rect(screen,(255,255,255),rect)
        score_text = font.render("Score:0",True,(0,0,0))
        screen.blit(score_text,(10,10))
        pygame.display.update()