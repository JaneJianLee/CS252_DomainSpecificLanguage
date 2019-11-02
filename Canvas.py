from tkinter import *

class Canvas:
    def __init__(self, width=0, height=0):
        self.root = Tk()
        self.w = Canvas(self.root, width=width, height=height)
        self.shapes = [] #Shape class

    def addShape(self, shape):
        self.shapes.append(shape)

    def draw(self):

        for s in self.shapes:
            if s.shapeType == "line":
                self.w.create_line(*s.params)
            elif s.shapeType == "circle":
                self.w.create_oval(*s.params)
            elif s.shapeType == "oval":
                self.w.create_oval(*s.params)
            elif s.shapeType == "text":
                self.w.create_text(*s.params)
            else:
                self.w.create_polygon(*s.params)
        self.w.pack()
        mainloop()


class Shape:
    def __init__(self, shapeType):
        self.shapeType = shapeType
        self.params = []
        self.color = Color()
        self.fillColor = Color(colorStr="white", bColorStr=True)

    def setParams(self, params):
        self.params = params



class Color:
    """ Available colorStr: "white", "black", "red", "green", "blue", "cyan", "yellow", and "magenta"
            Or check: http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
    """
    def __init__(self, redVal=0, greenVal=0, blueVal=0, colorStr="black", bColorStr=False):
        self.redVal = redVal
        self.greenVal = greenVal
        self.blueVal = blueVal
        self.colorStr = colorStr
        self.bColorStr = bColorStr #boolean to check if returning a pre-defined color

    def rgb2Hex(self):
        return "#" + '{:02x}'.format(self.redVal) + '{:02x}'.format(self.greenVal) + '{:02x}'.format(self.blueVal)

    def getColor(self):
        if self.bColorStr:
            return self.colorStr
        return self.rgb2Hex()