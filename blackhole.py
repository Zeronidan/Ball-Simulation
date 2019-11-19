# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey



class Black_Hole(Simulton):
    radius = 10
    def __init__(self, x, y):
        Simulton.__init__(self,x,y,width = Black_Hole.radius ,height = Black_Hole.radius)
        
    
    def contains(self, item):
        return Simulton.distance(self, (item._x, item._y)) < self._width
                   
            
    def update(self, model):
        result = set()
        remove_simultons = set()
        for item in model.find(lambda x: isinstance(x, Prey)): 
            if Black_Hole.contains(self, item):
                result.add(item)
        for s in model.simultons:
            for remove_item in result:
                remove_simultons.add(remove_item)
        for r in remove_simultons:
            model.simultons.remove(r)
        return result
        

    
    def display(self, canvas):
        d = self.get_dimension()
        canvas.create_oval(self._x-d[0]      , self._y-d[1],
                                self._x+d[0], self._y+d[1],
                                fill='black')