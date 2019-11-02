#!/usr/bin/env python
import sys
import pprint
import ply.yacc as yacc
from lexer_dl import tokens
from tkinter import *
root = Tk()
w = None
#w = Canvas(root,width=200,height=400)
#w.create_line(0,0,200,200)

def p_expression_canvas(p):
    'expression : CANVAS expression expression'
    global w
    w = Canvas(root,width=p[2],height=p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0]=p[1]

def p_expression_line(p):
    'expression : LINE expression expression expression expression'
    w.create_line(p[2],p[3],p[4],p[5])
    
def p_error(p):
    print("please end!")

filename = sys.argv[1]
parser = yacc.yacc()

with open(filename, 'r') as fp:
    for line in fp:
        print(line)
        try:
            print(id(w))
            parser.parse(line)
            print(id(w))
        except EOFError:
            break
w.pack()
root.mainloop()