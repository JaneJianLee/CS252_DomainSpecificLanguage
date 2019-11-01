import ply.lex as lex
import re

tokens = ('CANVAS',
         'NUMBER',
         'LBRACE',
         'RBRACE',
         'COMMA',
         )

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CANVAS(t):
    r'canvas'
    return t

def t_LBRACE(t):
    r'\('
    return t

def t_RBRACE(t):
    r'\)'
    return t

def t_newline(t):
    r'\n+'
    return t

def t_COMMA(t):
    r','
    return t

def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    t.lexer.skip(1)

t_ignore = ' \t'

lexer = lex.lex()

