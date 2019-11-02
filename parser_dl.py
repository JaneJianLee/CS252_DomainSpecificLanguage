#!/usr/bin/env python
import sys
import pprint
import ply.yacc as yacc
from lexer_dl import tokens
from MyCanvas import MyCanvas, Shape, Color

c = MyCanvas()
currentFillColor = Color(colorStr="black", bColorStr=True)
currentOutlineColor = Color(colorStr="black", bColorStr=True)

def p_expression_canvas(p):
    'expression : CANVAS expression expression'
    c.setCanvasSize(p[2], p[3])

def p_expression_bkgdcolor(p):
    '''expression : BKGDCOLOR expression
                  | BKGDCOLOR expression expression expression'''
    if(len(p) == 3):
        c.setBkgdColor(p[2])
    elif(len(p) == 5):
        c.setBkgdColor([p[2], p[3], p[4]])
    else:
        c.setBkgdColor("white")

def p_expression_number(p):
    'expression : NUMBER'
    p[0]=p[1]

def p_expression_word(p):
    'expression : WRD'
    p[0]=p[1]

def p_expression_color(p):
    """expression : COLOR expression
                  | COLOR expression expression expression"""
    global currentFillColor
    if (len(p) == 3):
        currentFillColor = Color(colorStr=p[2], bColorStr=True)
    elif (len(p) == 5):
        currentFillColor = Color(redVal=p[2], greenVal=p[3], blueVal=p[4])
    else:
        currentFillColor = Color(colorStr="black", bColorStr=True)

def p_expression_line(p):
    'expression : LINE expression expression expression expression'
    params = [p[2], p[3], p[4], p[5]]
    s = Shape("line")
    s.setParams(params)
    s.fillColor = currentFillColor
    s.color = currentOutlineColor
    c.addShape(s) #add shape to canvas

def p_expression_circle(p):
    'expression : CIRCLE expression expression expression'
    x0=p[2]-p[4]
    x1=p[3]-p[4]
    y0=p[2]+p[4]
    y1=p[3]+p[4]

    params = [x0, x1, y0, y1]
    s = Shape("circle")
    s.setParams(params)
    s.fillColor = currentFillColor
    s.color = currentOutlineColor
    c.addShape(s)

def p_expression_oval(p):
    'expression : OVAL expression expression expression expression'
    params = [p[2], p[3], p[4], p[5]]
    s = Shape("oval")
    s.setParams(params)
    s.fillColor = currentFillColor
    s.color = currentOutlineColor
    c.addShape(s)

def p_expression_rectangle(p):
    'expression : RECT expression expression expression expression'
    params = [p[2], p[3], p[4], p[5]]
    s = Shape("rectangle")
    s.setParams(params)
    s.fillColor = currentFillColor
    s.color = currentOutlineColor
    c.addShape(s)

def p_expression_text(p):    
    'expression : TEXT expression expression expression'
    params = [p[2], p[3], p[4]]
    s = Shape("text")
    s.setParams(params)
    s.fillColor = currentFillColor
    s.color = currentOutlineColor
    c.addShape(s)


def p_expression_image(p):
    'expression : IMG expression expression expression expression'
    #w.create_image(position, **options)
    
def p_error(p):
    print("Syntax error at '%s'" % p.value)

filename = sys.argv[1]
parser = yacc.yacc()

with open(filename) as fp:
    for line in fp:
        if line is "\n": #hacky solution for skipping the extra newlines :( - Ai-Linh
            continue
        print(line)
        try:
            parser.parse(line)
        except EOFError:
            break

c.draw() #canvas drawing shapes in this function