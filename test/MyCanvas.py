from tkinter import *

class MyCanvas:
    """
    This class uses Tkinter Canvas to draw shapes provided by Shape class.

    Attributes:
        root (Tk): Goshujin-sama
        width (int): width of canvas
        height (int): height of canvas
        bkgdColor (Color): color of canvas given as a string of 3-param red, green, blue values
        w (Canvas): Tkinter Canvas
        shapes (Shape[]): list of shapes
    """

    def __init__(self, width=0, height=0):
        """
        Constructor for MyCanvas.

        :param width: width of canvas
        :param height: height of canvas
        """
        self.root = Tk()
        self.bkgdColor = Color(colorStr="white", bColorStr=True)
        self.w = Canvas(self.root)
        self.shapes = [] #Shape class

    def setCanvasSize(self, width, height):
        """
        Set config of w to new width and height

        :param width: width of canvas
        :param height: height of canvas
        """
        self.w.config(width=width, height=height)

    def setBkgdColor(self, colors):
        """
        Sets background color of Canvas.

        :param colors (str or int[3]): color string type or [red, green, blue]
        """
        if isinstance(colors, str):
            c = Color(colorStr=colors, bColorStr=True)
        else:
            c = Color(redVal=colors[0], greenVal=colors[1], blueVal=colors[2])
        self.w.config(background=c.getColor())

    def addShape(self, shape):
        """
        Appends new shape to list shapes.

        :param shape: new Shape object
        """
        self.shapes.append(shape)

    def draw(self):
        """
        Draw list of shapes onto canvas.
        """
        for s in self.shapes:
            if s.shapeType == "line":
                #Draw line
                self.w.create_line(*s.params, fill=s.fillColor.getColor())
            elif s.shapeType == "circle":
                #Draw circle
                self.w.create_oval(*s.params, fill=s.fillColor.getColor(), outline=s.color.getColor())
            elif s.shapeType == "oval":
                #Draw oval
                self.w.create_oval(*s.params, fill=s.fillColor.getColor(), outline=s.color.getColor())
            elif s.shapeType == "rectangle":
                #Draw rectangle
                self.w.create_rectangle(*s.params, fill=s.fillColor.getColor(), outline=s.color.getColor())
            elif s.shapeType == "text":
                #Draw text
                param = s.params
                self.w.create_text(param[0], param[1],
                                      fill=s.color.getColor(), font="Times 20 italic bold", text=param[2])
            else:
                #TODO: Draw polygon
                self.w.create_polygon(*s.params, fill=s.fillColor.getColor(), outline=s.color.getColor())

        self.w.pack()
        mainloop()


class Shape:
    """
    Shape class.

    Attributes:
        shapeType (str): "line", "circle", "oval", "rectangle", "text"
        params (int[]): Parameters given by expression values. Usually of int type unless its text (str).
        color (Color): outline color of the shape
        fillColor (Color): fill color of the shape
    """

    def __init__(self, shapeType):
        """
        Constructor for Shape.

        :param shapeType: "line", "circle", "oval", "rectangle", "text"
        """
        self.shapeType = shapeType
        self.params = []
        self.color = Color(colorStr="white", bColorStr=True)
        self.fillColor = Color(colorStr="white", bColorStr=True)

    def setParams(self, params):
        """
        Set new parameters.

        :param params: parameters for the shape
        """
        self.params = params



class Color:
    """
    Color class.

    Attributes:
        redVal (int), greenVal (int), blueValue(int): for the 3-parameter color function. Each value is 0-255.
        colorStr (str): "white", "black", "red", "green", "blue", "cyan", "yellow", and "magenta"
            Or check: http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        bColorStr (bool): if True, then 1-param color is used and colorStr is set to a pre-defined color. Else, use
            redVal, greenVal, blueVal.
    """
    def __init__(self, redVal=0, greenVal=0, blueVal=0, colorStr="black", bColorStr=False):
        """
        Constructor for Color.

        :param redVal: value from 0-255
        :param greenVal: value from 0-255
        :param blueVal: value from 0-255
        :param colorStr: any pre-defined Tkinter color
        :param bColorStr: if True, then colorStr is used
        """
        self.redVal = redVal
        self.greenVal = greenVal
        self.blueVal = blueVal
        self.colorStr = colorStr
        self.bColorStr = bColorStr #boolean to check if returning a pre-defined color

    def rgb2Hex(self):
        """
        Convert redVal, greenVal, and blueVal to hexidecimal for Tkinter color.

        :return: hex color value as str
        """
        return "#" + '{:02x}'.format(self.redVal) + '{:02x}'.format(self.greenVal) + '{:02x}'.format(self.blueVal)

    def getColor(self):
        """
        Get the color string for Tkinter color.

        :return: color string or hexidecimal
        """
        if self.bColorStr:
            return self.colorStr
        return self.rgb2Hex()