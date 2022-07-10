import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import os, glob
from colour import Color
class Draw:


    pygame.init()
    clock = pygame.time.Clock()
    @classmethod
    def done(cls):
        pygame.quit()

    @classmethod
    def draw(cls, point_list : list, WIDTH= 750, HEIGHT = 550, xoff=True, yoff=True, HOLD=True, wait=0) -> None:

        # get win
        if not hasattr(cls, "win"):
            xboarder, yboarder = 50, 50
            cls.win = pygame.display.set_mode((WIDTH, HEIGHT))
            cls.xoff = (WIDTH) /2 * xoff
            cls. yoff = (HEIGHT) /2 * yoff
            
        # setup gradient
        red = Color("red")
        gradient = list(red.range_to(Color("green"), len(point_list)))
        

        # draw
        cls.win.fill((255,255,255))
        for i in range(len(point_list)-1):
            colour = [i*255 for i in gradient[i].rgb]#cls.__hex_to_rgb(gradient[i].hex)

            pygame.draw.line(cls.win, colour,
                     point_list[i] +   (cls.xoff,cls.yoff),
                     point_list[i+1] + (cls.xoff,cls.yoff), 1)
                    
        
        pygame.display.update()
        cls.clock.tick(wait) 

        # check for quit
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  exit()

        while HOLD:
            cls.clock.tick(5) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  exit()
   
   
    @staticmethod
    def __centerPoints(points : list, xoff = 0, yoff = 0) -> list:
        # return centered points
        try:
            return [i + (xoff, yoff) for i in points]
        except Exception as e:
            print(points)
            raise e



    @staticmethod
    def __hex_to_rgb(hex: str) -> tuple:
        hex = hex.ljust(6, "0")
        rgb = []

        for i in range(1,6,2):
            decimal = int(hex[i:i+2], 16)
            rgb.append(decimal)
        return tuple(rgb)


   