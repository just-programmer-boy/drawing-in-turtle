# first of all you should install sketchpy in your vs code terminal by typing
# pip install sketchpy

# these are codes to import the module
from sketchpy import library as lib

# codes create an object of rdj()
obj = lib.rdj()

# you can change speed using pen.speed()
obj.pen.speed(2)

# and the draw method
obj.draw() 
