# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    counter_constant = 30
    def __init__(self, x, y):
        Black_Hole.__init__(self,x,y)
        self.pulsator_counter = 0
         
    def update(self, model):
        self.pulsator_counter += 1
        if self.pulsator_counter == Pulsator.counter_constant:
            self.pulsator_counter = 0
            self.change_dimension(-1, -1)
        if self.get_dimension()[0] <= 0:
            model.simultons.remove(self)
        for item in Black_Hole.update(self, model):
            self.change_dimension(1, 1)
            self.pulsator_counter = 0