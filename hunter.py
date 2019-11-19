# A Hunter is both a  Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.
 
 
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2
 
 
 
class Hunter(Pulsator,Mobile_Simulton):
    distance = 200
     
    def __init__(self, x, y):
        self.randomize_angle()
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self,x,y,width = Pulsator.radius,height = Pulsator.radius,angle = self._angle,speed = 5)
         
    def update(self, model):
        self.move()
        result = dict()
        for item in model.find(lambda x: isinstance(x, Prey)):
            if Mobile_Simulton.distance(self, (item._x, item._y)) < Hunter.distance:
                result[Mobile_Simulton.distance(self, item.get_location())] = item
        if result != dict():
            m = min(result)
            min_location = result[m].get_location()
            hunter_location = self.get_location()
            new_x_angle = min_location[0] - hunter_location[0]  
            new_y_angle = min_location[1] - hunter_location[1]  
            Mobile_Simulton.set_angle(self, atan2(new_y_angle, new_x_angle))
        Pulsator.update(self, model)
 
 
         
         
         
         
                 
