import ply.lex as lex

tokens = ('CANVAS',
         'NUMBER',
         'LINE'
         )

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CANVAS(t):
    r'canvas'
    return t

def t_LINE(t):
    r'line'
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

