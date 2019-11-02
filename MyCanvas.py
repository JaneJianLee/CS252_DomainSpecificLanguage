from tkinter import *

class MyCanvas:
    def __init__(self, width=0, height=0):
        self.root = Tk()
        self.bkgdColor = Color(colorStr="white", bColorStr=True)
        self.w = Canvas(self.root)
        self.shapes = [] #Shape class

    def setCanvasSize(self, width, height):
        self.w.config(width=width, height=height)

    def setBkgdColor(self, colors):
        if isinstance(colors, str):
            c = Color(colorStr=colors, bColorStr=True)
        else:
            c = Color(redVal=colors[0], greenVal=colors[1], blueVal=colors[2])
        self.w.config(background=c.getColor())

    def addShape(self, shape):
        self.shapes.append(shape)

    def draw(self):

        for s in self.shapes:
            if s.shapeType == "line":
                self.w.create_line(*s.params, fill=s.fillColor.getColor())
            elif s.shapeType == "circle":
                self.w.create_oval(*s.params, fill=s.fillColor.getColor(), outline=s.color.getColor())
            elif s.shapeType == "oval":
                self.w.create_oval(*s.params, fill=s.fillColor.getColor(), outline=s.color.getColor())
            elif s.shapeType == "rectangle":
                self.w.create_rectangle(*s.params, fill=s.fillColor.getColor(), outline=s.color.getColor())
            elif s.shapeType == "text":
                param = s.params
                self.w.create_text(param[0], param[1],
                                      fill=s.color.getColor(), font="Times 20 italic bold", text=param[2])
            else:
                self.w.create_polygon(*s.params, fill=s.fillColor.getColor(), outline=s.color.getColor())

        self.w.pack()
        mainloop()


class Shape:
    def __init__(self, shapeType):
        self.shapeType = shapeType
        self.params = []
        self.color = Color(colorStr="white", bColorStr=True)
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