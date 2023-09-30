import pygame
import sys
import random
import math

random.seed(2137)


class ManyPoints:
    def __init__(self, number_of_points):
        self.number_of_points = number_of_points
        self.list_of_points = []
        self.angle = 0
        self.RADIUSES_SET = True
        for i in range(number_of_points):
            x, y = random.randint(0, screen_width), random.randint(0, screen_height)
            self.list_of_points.append((x, y))

    def display_points(self):
        for x, y in self.list_of_points:
            screen.set_at((int(x), int(y)), pixel_color)
    def simple_walk(self, speedx=1,speedy=1):
        new_list = []
        for x, y in self.list_of_points:
            if x > screen_width:
                x = 0
                y = y + speedy
            elif x < 0:
                x = screen_width
                y = y + speedy
            if y > screen_height:
                y = 0
                x = x + speedx

            elif y < 0:
                y = screen_height
                x = x + speedx
            else:

                x = x + speedx
                y = y + speedy
            new_list.append((x, y))

        self.list_of_points = new_list


    def random_walk(self, speed=1):
        new_list = []
        for x, y in self.list_of_points:
            if x > screen_width:
                x = 0
                y = y + random.randint(-speed, speed)
            elif x < 0:
                x = screen_width
                y = y + random.randint(-speed, speed)
            if y > screen_height:
                y = 0
                x = x + random.randint(-speed, speed)

            elif y < 0:
                y = screen_height
                x = x + random.randint(-speed, speed)
            else:

                x = x + random.randint(-speed, speed)
                y = y + random.randint(-speed, speed)
            new_list.append((x, y))

        self.list_of_points = new_list

    def rotate(self,delta_angle = 100):
        

        delta_angle_radians = delta_angle *(10**(-7)) * (180/math.pi)
        def get_radiuses():
            radiuses=[]
            lock_x, lock_y = int((screen_width / 2)), int((screen_height / 2))
            for x, y in self.list_of_points:
                x = x - lock_x
                y = y - lock_y
                radius = (x**2 + y**2)**(1/2)
                radiuses.append(radius)
            return radiuses
        def new_coordinates():
            for i in range(len(self.list_of_points)):
                r = self.radiuses[i]
                x , y =self.list_of_points[i]
                new_x =   math.cos(delta_angle_radians) * (x-center_x) - math.sin(delta_angle_radians) * (y-center_y)  +center_x
                new_y =   math.sin(delta_angle_radians) * (x-center_x) + math.cos(delta_angle_radians) * (y-center_y)  +center_y
                self.list_of_points[i] = (new_x , new_y)
        
        if self.RADIUSES_SET:
            for i in range(len(self.list_of_points)):
                x, y = random.randint(-300, screen_width+300), random.randint(-300, screen_height+300)
                self.list_of_points[i]=(x, y)

            self.radiuses =get_radiuses()
            self.RADIUSES_SET = False
        new_coordinates()
        
        
        
                


        

# Define screen dimensions
screen_width, screen_height = 800, 800



## initialize amount of points
points = ManyPoints(10000)
########


pixel_color = (255, 255, 255)
# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the initial position and radius of the circle
center_x, center_y = screen_width // 2, screen_height // 2
# Set the pixel color (white in RGB)
# Main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.fill((0, 0, 0))
    # Set the pixel color at the calculated position
    ##points.random_walk(1)
    points.display_points()
    #points.simple_walk(speedx=0.1 , speedy=0.2)
    points.rotate()
    

    # Update the screen
    pygame.display.flip()
# Quit Pygame
pygame.quit()
sys.exit()
