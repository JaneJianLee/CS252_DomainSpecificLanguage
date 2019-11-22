#!/usr/bin/env python
import sys
import pprint
import ply.yacc as yacc
from lexer_dl import tokens
from tkinter import *
root = Tk()
w = None

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
    
def p_expression_canvas(p):
    '''expression : CANVAS expression expression color
                  | CANVAS expression expression'''
    global w

    if len(p) == 4: #default
        w = Canvas(root, bg="white", width=p[2], height=p[3])
    else:
        w = Canvas(root, bg=p[4], width=p[2], height=p[3])

def p_expression_line(p):
    '''expression : LINE x-coor y-coor x-coor y-coor color
                  | LINE x-coor y-coor x-coor y-coor'''

    if len(p) == 6: #default
        w.create_line(p[2],p[3],p[4],p[5])
    else:
        w.create_line(p[2],p[3],p[4],p[5], fill=p[6])

def p_expression_circle(p):
    '''expression : CIRCLE x-coor y-coor radius color
                  | CIRCLE x-coor y-coor radius'''
    x0=p[2]-p[4]
    x1=p[3]-p[4]
    y0=p[2]+p[4]
    y1=p[3]+p[4]

    if len(p) == 5: #default
        w.create_oval(x0, x1, y0, y1, fill="black", outline="black", width=4)
    else:
        w.create_oval(x0, x1, y0, y1, fill=p[5], outline="black", width=4)

def p_expression_oval(p):
    '''expression : OVAL x-coor y-coor x-coor y-coor color
                  | OVAL x-coor y-coor x-coor y-coor'''

    if len(p) == 6: #default
        w.create_oval(p[2], p[3], p[4], p[5])
    else:
        w.create_oval(p[2], p[3], p[4], p[5], fill=p[6])


def p_expression_rectangle(p):
    '''expression : RECT x-coor y-coor x-coor y-coor color
                  | RECT x-coor y-coor x-coor y-coor'''
    if len(p) == 6:
        w.create_rectangle(p[2], p[3], p[4], p[5])
    else:
        w.create_rectangle(p[2],p[3],p[4],p[5], fill=p[6])

def p_expression_text(p):    
    'expression : TEXT x-coor y-coor WRD'
    w.create_text(p[2],p[3],fill="black",font="Times 20 italic bold",text=p[4])
    

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