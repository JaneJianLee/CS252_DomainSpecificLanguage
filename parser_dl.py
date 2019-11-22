#!/usr/bin/env python
import sys
import pprint
import ply.yacc as yacc
from lexer_dl import tokens
from tkinter import *
import time
root = Tk()
w = None
last_obj = None
width, height = 0, 0

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
    global last_obj
    if len(p) == 6: #default
        last_obj = w.create_line(p[2],p[3],p[4],p[5])
    else:
        last_obj = w.create_line(p[2],p[3],p[4],p[5], fill=p[6])

def p_expression_circle(p):
    '''expression : CIRCLE x-coor y-coor radius color
                  | CIRCLE x-coor y-coor radius'''
    global last_obj
    x0=p[2]-p[4]
    x1=p[3]-p[4]
    y0=p[2]+p[4]
    y1=p[3]+p[4]

    if len(p) == 5: #default
        last_obj = w.create_oval(x0, x1, y0, y1, fill="black", outline="black", width=4)
    else:
        last_obj = w.create_oval(x0, x1, y0, y1, fill=p[5], outline="black", width=4)

def p_expression_oval(p):
    '''expression : OVAL x-coor y-coor x-coor y-coor color
                  | OVAL x-coor y-coor x-coor y-coor'''
    global last_obj
    if len(p) == 6: #default
        last_obj = w.create_oval(p[2], p[3], p[4], p[5])
    else:
        last_obj = w.create_oval(p[2], p[3], p[4], p[5], fill=p[6])


def p_expression_rectangle(p):
    '''expression : RECT x-coor y-coor x-coor y-coor color
                  | RECT x-coor y-coor x-coor y-coor'''
    global last_obj
    if len(p) == 6:
        last_obj = w.create_rectangle(p[2], p[3], p[4], p[5])
    else:
        last_obj = w.create_rectangle(p[2],p[3],p[4],p[5], fill=p[6])

def p_expression_text(p):    
    'expression : TEXT x-coor y-coor WRD'
    global last_obj
    last_obj = w.create_text(p[2],p[3],fill="black",font="Times 20 italic bold",text=p[4])

def p_expression_move(p):
    'expression : MOVE speed direction'
    print("inside0")
    if p[3] == 'h':
        print("inside1")
        if p[2] == 'fast':
            xspeed = 10
            print("inside2")
        elif p[2] == 'slow':    
            xspeed = 5
        while True:
            pos = w.coords(last_obj)
            if pos[0] >= width:
                print("breaking",pos,width,height)
                break
            w.move(last_obj,xspeed,0)
            print("moving",pos,width,height)
            root.update()
            w.pack()
            time.sleep(0.1)

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
            time.sleep(0.1)    

def p_expression_image(p):
    'expression : IMG expression expression expression expression'
    #w.create_image(position, **options)
    
def p_error(p):
    print("Syntax error at '%s'" % p.value)

filename = sys.argv[1]
parser = yacc.yacc()

with open(filename, 'r') as fp:
    for line in fp:
        print(line)
        try:
            parser.parse(line)
        except EOFError:
            break
w.pack()
root.mainloop()