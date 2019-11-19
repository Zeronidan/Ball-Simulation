# The special simulton is like a black hole.
# It eats the preys and moves randomly. 
# Whenever it eats a prey it changes shape. 
# The first shape that appears is selected randomly. 
from blackhole import Black_Hole
from random import randrange 
from mobilesimulton import Mobile_Simulton
class Special(Black_Hole, Mobile_Simulton):
    shape = None
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.randomize_angle()
        Mobile_Simulton.__init__(self, x, y, Black_Hole.radius, Black_Hole.radius, self._angle, speed = 5 )
    def update(self, model):
        self.move()
        for item in Black_Hole.update(self, model):
            if Special.shape == 'rectangle':
                Special.shape = 'oval'
            else:
                Special.shape = 'rectangle'

    
    def display(self, canvas):
        shape_dict = {1: 'rectangle', 2: 'oval'}
        if Special.shape == None:
            num = randrange(1,3)
            Special.shape = shape_dict[num]
            
        if Special.shape == 'rectangle':
            canvas.create_rectangle(self._x-Black_Hole.radius      , self._y-Black_Hole.radius,
                                self._x+Black_Hole.radius, self._y+Black_Hole.radius, fill = 'purple' )
            
        if Special.shape == 'oval':
            canvas.create_oval(self._x-Black_Hole.radius      , self._y-Black_Hole.radius,
                                self._x+Black_Hole.radius, self._y+Black_Hole.radius,
                                fill='yellow')
            
            
            
        
            
            
    