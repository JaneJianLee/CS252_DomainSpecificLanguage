import ply.lex as lex

tokens = ('CANVAS',
         'NUMBER',
         'LINE',
         'CIRCLE',
         'OVAL',
         'RECT',
         'WRD',
         'TEXT',
         'QUOT',
         'MOVE',
         'BIGGER',
         'SMALLER',
         'SHOW',
         'ROTATE',
         'LEFT',
         'RIGHT',
         'BOUNCEBALL',
         'MIRRORX',
         'MIRRORY'
         )

def t_CANVAS(t):
    r'canvas'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_LINE(t):
    r'line'
    return t

def t_CIRCLE(t):
    r'circle'
    return t

def t_OVAL(t):
    r'oval'
    return t

def t_MOVE(t):
    r'move'
    return t

def t_BIGGER(t):
    r'makeBigger'
    return t

def t_SMALLER(t):
    r'makeSmaller'
    return t

def t_ROTATE(t):
    r'turn'
    return t

def t_LEFT(t):
    r'left'
    return t

def t_RIGHT(t):
    r'right'
    return t

def t_MIRRORX(t):
    r'mirrorx'
    return t

def t_MIRRORY(t):
    r'mirrory'
    return t

def t_SHOW(t):
    r'show'
    return t

def t_RECT(t):
    r'rectangle'
    return t
    
def t_BOUNCEBALL(t):
    r'bounceball'
    return t

def t_TEXT(t):
    r'text'
    return t

def t_WRD(t):
    r'\w+'
    return t

def t_QUOT(t):
    r'\"'
    return t

def t_LBRACE(t):
    r'\('
    pass
    
def t_RBRACE(t):
    r'\)'
    pass

def t_NEWLINE(t):
    r'\n+'
    pass

def t_WHITESPACE(t):
    r"[\n\t ]"
    pass

def t_COMMA(t):
    r','
    pass


t_ignore = ' \t'
    
def t_error(t):
	print('Undefined token translation!')
	sys.exit(1)

lexer = lex.lex()

