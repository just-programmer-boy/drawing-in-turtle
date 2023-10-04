#first of all you should install sketchpy in your vs by typing
#pip install sketchpy

#codes to import the module
from sketchpy import library as lib

#create an object of rdj()
obj = lib.rdj()

# you can change speed using pen.speed()
obj.pen.speed(2)

#the draw method
obj.draw() 
