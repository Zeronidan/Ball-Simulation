# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random, uniform


class Floater(Prey):
    radius = 5
    
    def __init__(self, x, y):
        self.randomize_angle()
        Prey.__init__(self,x,y,width = Floater.radius *2,height = Floater.radius*2,angle = self._angle,speed = 5)
        
    def update(self, model):
        random_chance = random()
        random_speed = uniform(-.5, +.51)
        random_angle = uniform(-.5, +.51)
        if random_chance <= 0.3:    
            new_speed = self._speed + random_speed
            new_angle = self._angle + random_angle
            while True:
                if 3 <= new_speed <= 7:
                    break
                else:
                    random_speed = uniform(-.5, .51)
                    new_speed = self._speed + random_speed 
            self.set_velocity(new_speed, new_angle)
        self.move()
        self.wall_bounce()
        
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='red')
        
        
    