from cmath import pi

# classes
class Cylinder():
     
    def __init__(self, h, r):
        self.height = h
        self.radius = r

    def calc(self):
        return self.radius * self.radius * self.height * pi

class Rectangle():
     
    def __init__(self, h, w, d):
        self.height = h
        self.width = w
        self.depth = d

    def calc(self):
        return self.height * self.width * self.depth

# this will do validation and methods return True or False
class Validator():
     
    def isNonNegNumber(self, inNumber):
        _returnValue = False
        if (inNumber<0):
            _returnValue = False
        else:
            _returnValue = True
        return _returnValue
       

# main program starts here
_continue = True

# outer loop to control when to stop
while(_continue):
    _validator = Validator()
    _shape = input("What shape would you like to get calculate volume for? cylinder, \
    rectangle, stop (to end program): ")
    
    if (_shape == "stop"):
        _continue = False
    elif (_shape == "cylinder"):

        _height = float(input("please input the height (must be positive number): "))
        _check = _validator.isNonNegNumber(_height)
        while(_check == False):
            _height = float(input("please input the height (must be positive number): "))
            _check = _validator.isNonNegNumber(_height)

        _radius = float(input("please input the radius (must be positive number): "))
        _check = _validator.isNonNegNumber(_radius)
        while (_check == False):
            _radius = float(input("please input the radius (must be positive number): "))
            _check = _validator.isNonNegNumber(_radius)

        _cylinder = Cylinder(_height, _radius) # instantiate new object
        _calc = _cylinder.calc()
        print("cylinder volume is " + str(_calc))
    elif (_shape == "rectangle"):

        _height = float(input("please input the height (must be positive number): "))
        _check = _validator.isNonNegNumber(_height)
        while (_check == False):
            _height = float(input("please input the height (must be positive number): "))
            _check = _validator.isNonNegNumber(_height)

        _width = float(input("please input the width (must be positive number): "))
        _check = _validator.isNonNegNumber(_width)
        while (_check == False):
            _width = float(input("please input the width (must be positive number): "))
            _check = _validator.isNonNegNumber(_width)


        _depth = float(input("please input the depth (must be positive number): "))
        _check = _validator.isNonNegNumber(_depth)
        while(_check == False):
            _depth = float(input("please input the depth (must be positive number): "))
            _check = _validator.isNonNegNumber(_depth)

        _rec = Rectangle(_height, _width, _depth)
        _calc = _rec.calc()
        print("retangle volume is " + str(_calc))

print("thanks for using Geometry Calc")
