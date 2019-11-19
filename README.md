# Ball-Simulation

A simple simulation of balls using MVC (Model, View, Controller) written in Python
and Tkinter as the GUI of the controller.  The View and Controller came written 
and I implemented the Model portion.  The purpose of this project is to understand
and experience Inheritance hands on. 



Simultons have a location on the canvas and a dimension.
- Preys inherit from Mobile Simultons
    - Balls (blue) move at constant speed and bounce off the walls.
    - Floaters (red) move at a random speed and direction
- Mobile Simultons inherit its location and dimension from Simultons and have a speed and angle
- Black Holes (Black) inherit from Simultons and are stationary and eat any prey that touch them (balls or floaters).
    - Pulsators inherit from Black Holes and act the same way but changes dimensions (grows/shrinks) depending on whether its "eaten" prey or not.
        - Hunters inherit from Pulsators but are mobile and chases the nearest prey

- Special inherits from Black Holes and Mobile Simultons. When a special eats a prey it changes to a random shape.
