#!/usr/bin/env python
import sys
import pprint
import ply.yacc as yacc

from lexer import tokens
from tkinter import *

master = Tk()
canvas_width=0
canvas_height=0

def p_expression_canvas(t):
    'expression : CANVAS LBRACE expression COMMA expression RBRACE NEWLINE'
    global canvas_width
    canvas_width = t[3]
    global canvas_height
    canvas_height = t[5]

    
def p_expression_number(t):
    'expression : NUMBER'
    t[0]=t[1]

#line(125, 0, 125, 500, 10)
def p_expression_line(t):
    'expression : LINE LBRACE expression COMMA expression COMMA expression COMMA expression COMMA expression RBRACE NEWLINE'
    w.create_line(t[3],t[5],t[7],t[9],width=t[11])
    
def p_error(t):
    print("please end!")

filename = sys.argv[1]

parser = yacc.yacc()

pp = pprint.PrettyPrinter(indent=4)

with open(filename, 'r') as f:
    input = f.read()
    pp.pprint(parser.parse(input))

w = Canvas(master,width= canvas_width,height=canvas_height)
w.pack()

mainloop()
