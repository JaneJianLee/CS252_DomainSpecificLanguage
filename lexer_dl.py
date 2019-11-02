import ply.lex as lex
import sys

tokens = ('CANVAS',
         'NUMBER',
         'LINE',
         'CIRCLE',
         'OVAL',
         'RECT',
         'WRD',
         'IMG',
         'TEXT',
         'BKGDCOLOR',
         'COLOR'
         )

def t_CANVAS(t):
    r'canvas'
    return t

def t_BKGDCOLOR(t):
    r'backgroundColor'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_LINE(t):
    r'line'
    return t

def t_COLOR(t):
    r'color'
    return t

def t_CIRCLE(t):
    r'circle'
    return t

def t_OVAL(t):
    r'oval'
    return t

def t_RECT(t):
    r'rectangle'
    return t

def t_TEXT(t):
    r'text'
    return t

def t_WRD(t):
    r'\w+'
    return t
    
def t_IMG(t):
    r'image'
    return t

def t_LBRACE(t):
    r'\('
    pass
    
def t_RBRACE(t):
    r'\)'
    pass

#debug the newline
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    #pass

# user parser_dl.py line 108 to skip the extra lines - Ai-Linh
# def t_WHITESPACE(t):
#     r"[\n\t ]"
#     pass

def t_COMMA(t):
    r','
    pass

def t_QUOT(t):
    r'\"'
    pass

t_ignore = ' \t'
    
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)
	#sys.exit(1)

lexer = lex.lex()

