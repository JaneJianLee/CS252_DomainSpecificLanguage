#!/usr/bin/env python
import sys
import pprint
import ply.yacc as yacc
from lexer_dl import tokens
from tkinter import *
import time
import math

root = Tk()
w = None
last_obj = None
args_last = [] #args for the last shape
flag_shape_last = "" #flag for the last shape
width, height = 0, 0

#for scaling
scaleFactor = 1
prevScaleFactor = 1
bShowPrevScale = False

#for rotating
degrees = 0
rotateDirection = ""

def p_expression_number(p):
    'expression : NUMBER'
    p[0]=p[1]

def p_expression_color(p):
    'color : QUOT WRD QUOT'
    p[0]=p[2]

def p_expression_xcoor(p):
    'x-coor : NUMBER'
    p[0]=p[1]

def p_expression_ycoor(p):
    'y-coor : NUMBER'
    p[0]=p[1]
    
def p_expression_radius(p):
    'radius : NUMBER'
    p[0]=p[1]

def p_expression_degrees(p):
    'degrees : NUMBER'
    p[0]=p[1]

def p_expression_speed(p):
    'speed : WRD'
    p[0]=p[1]

def p_expression_direction(p):
    'direction : WRD'
    p[0]=p[1]
    
def p_expression_canvas(p):
    '''expression : CANVAS expression expression color
                  | CANVAS expression expression'''
    global w, width, height
    width=p[2]
    height=p[3]
    
    if len(p) == 4: #default
        w = Canvas(root, bg="white", width=p[2], height=p[3])
    else:
        w = Canvas(root, bg=p[4], width=p[2], height=p[3])

def p_expression_line(p):
    '''expression : LINE x-coor y-coor x-coor y-coor color
                  | LINE x-coor y-coor x-coor y-coor'''
    global last_obj, args_last, flag_shape_last
    flag_shape_last = "line"
    #1 deletes
    # arg = []
    # #2
    # setArgs(p)
    if len(p) == 6: #default
        last_obj = w.create_line(p[2],p[3],p[4]*scaleFactor,p[5]*scaleFactor)
        args_last = [p[2],p[3],p[4],p[5],"black"]
    else:
        last_obj = w.create_line(p[2],p[3],p[4]*scaleFactor,p[5]*scaleFactor, fill=p[6])
        args_last = [p[2],p[3],p[4],p[5],p[6]]

def p_expression_circle(p):
    '''expression : CIRCLE x-coor y-coor radius color
                  | CIRCLE x-coor y-coor radius'''
    global last_obj, args_last, flag_shape_last
    flag_shape_last = "circle"

    x0=p[2]-p[4]
    x1=p[3]-p[4]
    y0=p[2]+p[4]
    y1=p[3]+p[4]

    if len(p) == 5: #default
        last_obj = w.create_oval(x0, x1, y0, y1, fill="black", outline="black", width=2)
        args_last = [x0, x1, y0, y1, "black"]
    else:
        last_obj = w.create_oval(x0, x1, y0, y1, fill=p[5], outline="black", width=2)
        args_last = [x0, x1, y0, y1, p[5]]




def p_expression_oval(p):
    '''expression : OVAL x-coor y-coor x-coor y-coor color
                  | OVAL x-coor y-coor x-coor y-coor'''
    global last_obj, scaleFactor, prevScaleFactor, bShowPrevScale, flag_shape_last, args_last
    flag_shape_last = "oval"

    if len(p) == 6: #default
        last_obj = w.create_oval(p[2], p[3], p[4]*scaleFactor, p[5]*scaleFactor)
        args_last = [p[2], p[3], p[4], p[5], "black"]
    else:
        last_obj = w.create_oval(p[2], p[3], p[4]*scaleFactor, p[5]*scaleFactor, fill=p[6])
        args_last = [p[2], p[3], p[4], p[5], p[6]]

    # reset scaleFactor
    bShowPrevScale = False
    prevScaleFactor = 1
    scaleFactor = 1


def p_expression_rectangle(p):
    '''expression : RECT x-coor y-coor x-coor y-coor color
                  | RECT x-coor y-coor x-coor y-coor'''
    global last_obj, scaleFactor, prevScaleFactor, bShowPrevScale, args_last, flag_shape_last
    flag_shape_last = "rectangle"

    if len(p) == 6:
        last_obj = w.create_rectangle(p[2], p[3], p[4], p[5])
        args_last = [p[2], p[3], p[4], p[5], "black"]
    else:
        last_obj = w.create_rectangle(p[2],p[3],p[4],p[5], fill=p[6])
        args_last = [p[2], p[3], p[4], p[5], p[6]]

def p_expression_text(p):    
    'expression : TEXT x-coor y-coor QUOT WRD QUOT'
    global last_obj
    last_obj = w.create_text(p[2],p[3],fill="black",font="Times 20 italic bold",text=p[5])

def p_expression_move(p):
    'expression : MOVE speed direction'
    if p[3] == 'h':
        if p[2] == 'fast':
            xspeed = 10
        elif p[2] == 'slow':    
            xspeed = 5
        while True:
            pos = w.coords(last_obj)
            if pos[0] >= width:
                break
            w.move(last_obj,xspeed,0)
            root.update()
            w.pack()
            time.sleep(0.01)

    elif p[3] == 'v':
        if p[2] == 'fast':
            yspeed = 10
        elif p[2] == 'slow':    
            yspeed = 5
        while True:
            pos = w.coords(last_obj)
            if pos[1] >= height:
                break
            w.move(last_obj,0,yspeed)
            root.update()
            w.pack()
            time.sleep(0.01)

def p_expression_rotate(p):
    '''expression : ROTATE LEFT degrees
                  | ROTATE RIGHT degrees'''
    global degrees, rotateDirection, args_last, flag_shape_last, numPoints
    #print("I am in rotate~!")
    degrees = p[3]
    if p[2] == 'left':
        degrees = -1*degrees
    sinRad = math.sin(math.radians(degrees))
    cosRad = math.cos(math.radians(degrees))
    points = args_last[:-1]
    #x1, y1, x2, y2
    coords = [[points[0], points[1]], [points[2], points[1]], [points[2], points[3]], [points[0], points[3]]]
    center = [points[0], points[1]]
    #print(coords)
    newPoints = []
    for x, y in coords:
        x -= center[0]
        y -= center[1]
        xnew = x*cosRad - y*sinRad
        ynew = x*sinRad + y*cosRad
        newPoints.append([xnew + center[0], ynew + center[1]])


    #reset args = [[coords], colorstr]
    sColor = args_last[-1]
    args_last = newPoints
    args_last.append(sColor)

    flag_shape_last = "polygon" #rotated rectangles have to become polygon
    redrawShapeTransform()


def p_expression_scale(p):
    '''expression : BIGGER
                  | SMALLER
                  | BIGGER SHOW
                  | SMALLER SHOW'''
    global scaleFactor, prevScaleFactor, bShowPrevScale

    if len(p) == 3: #set previous scale factor if toggle "show" is executed
        bShowPrevScale = True
        prevScaleFactor = scaleFactor
    if p[1] == 'makeSmaller':
        scaleFactor = 0.5
    else:
        scaleFactor = 1.5

    #reset args_last
    redrawShapeTransform() #redraw shape here

def redrawShapeTransform():
    global last_obj, flag_shape_last, args_last, bShowPrevScale, prevScaleFactor, scaleFactor
    w.delete(last_obj)
    if flag_shape_last != "polygon":
        args_last[2] *= scaleFactor
        args_last[3] *= scaleFactor

    if flag_shape_last == "line":
        # Draw line
        last_obj = w.create_line(args_last[0], args_last[1], args_last[2], args_last[3], fill=args_last[4])
    elif flag_shape_last == "circle":
        # Draw circle
        last_obj = w.create_oval(args_last[0], args_last[1], args_last[2], args_last[3], fill=args_last[4])
    elif flag_shape_last == "oval":
        # Draw oval
        last_obj = w.create_oval(args_last[0], args_last[1], args_last[2], args_last[3], fill=args_last[4])
    elif flag_shape_last == "rectangle":
        # Draw rectangle
        last_obj = w.create_rectangle(args_last[0], args_last[1], args_last[2], args_last[3], fill=args_last[4], outline=args_last[4])
    elif flag_shape_last == "polygon":
        print(args_last)
        last_obj = w.create_polygon(args_last[:-1], fill=args_last[-1])

    # if bShowPrevScale:
    #     w.create_oval(x0, x1, y0 * prevScaleFactor, y1 * prevScaleFactor, dash=(5, 3), outline="snow3", width=4)
    # reset scaleFactor
    bShowPrevScale = False
    prevScaleFactor = 1
    scaleFactor = 1

def p_expression_mirror(p):
    '''expression : MIRRORX
                  | MIRRORY'''
    global width, height, args_last
    cx = width/2
    cy = height/2
    print("Centerpoints of canvas: ", cx, cy)
    sColor = args_last[-1]
    points = args_last[:-1]
    if p[1] == "mirrory":
        if flag_shape_last != "polygon":
            if flag_shape_last == "circle":
                if points[0] == cx:
                    print("Overlaps! No flipping over y-axis.")
                else:
                    dist1 = abs(cx - points[0])
                    print("MIRRORY DIST:", dist1)
                    if points[0] < cx:
                        x1new = cx + dist1
                    else:
                        x1new = cx - dist1
                    args_last[0] = x1new
                    redrawShapeTransform()

            if points[0] <= cx and points[2] >= cx:
                print("Overlaps! No flipping over y-axis.")
            else:
                dist1 = abs(cx - points[0])
                dist2 = abs(cx - points[2])
                if points[0] < cx:
                    x1new = cx + dist1
                    x2new = cx + dist2
                else:
                    x1new = cx - dist1
                    x2new = cx - dist2
                args_last[0] = x1new
                args_last[2] = x2new
                redrawShapeTransform()

    if p[1] == "mirrorx":
        if flag_shape_last != "polygon":
            if flag_shape_last == "circle":
                if points[1] == cy:
                    print("Overlaps! No flipping over x-axis.")
                else:
                    dist1 = abs(cy - points[1])
                    print("MIRRORX DIST:", dist1)
                    if points[1] < cy:
                        y1new = cy + dist1
                    else:
                        y1new = cy - dist1
                    args_last[1] = y1new
                    redrawShapeTransform()

            if points[1] <= cy and points[3] >= cy:
                print("Overlaps! No flipping over x-axis.")
            else:
                dist1 = abs(cy - points[1])
                dist2 = abs(cy - points[3])
                if points[1] < cy:
                    y1new = cy + dist1
                    y2new = cy + dist2
                else:
                    y1new = cy - dist1
                    y2new = cy - dist2
                args_last[1] = y1new
                args_last[3] = y2new
                redrawShapeTransform()




def p_expression_bounceball(p):
    'expression : BOUNCEBALL'
    ball = w.create_oval(5,5,60,60,fill="pink")
    x, y = 1, 3
    
    while True:
        w.move(ball,x,y)
        pos = w.coords(ball)
        if pos[3] >= width or pos[1] <=0:
            y=-y
        if pos[2] >= height or pos[0] <=0:
            x=-x
        
        root.update()
        w.pack()
        time.sleep(0.01)
        pass

def p_error(p):
    print("Syntax error at '%s'" % p.value)

filename = sys.argv[1]
parser = yacc.yacc()

with open(filename, 'r') as fp:
    for line in fp:
        if line is "\n":  # hacky solution for skipping the extra newlines :( - Ai-Linh
            continue
        print(line)
        try:
            parser.parse(line)
        except EOFError:
            break
w.pack()
root.mainloop()
