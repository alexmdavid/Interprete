
# -----------------------------------------------------------------------------
# Rainman Sián
# 26-02-2020
#
# Ejemplo interprete sencillo con Python utilizando ply en Window
# -----------------------------------------------------------------------------
errorG = ""

reservadas = {
    'num' : 'NUMERO',
    'cheo' : 'BOOL',
    'verdadeiro' : 'TRUE',
    'embuste' : 'FALSE',
    'imp' : 'IMPRIMIR',
    'enquanto' : 'MIENTRAS',
    'finenq' : 'FINMIENTRAS',
    'sim' : 'IF',
    'sinao' : 'ELSE',
    'finsim' : 'FINSI',
    'par' : 'PARA',
    'finpar' : 'FINPARA',
    'fazer' : 'HACER'
}

tokens  = [
    'PTCOMA',
    'LLAVIZQ',
    'LLAVDER',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'CONCAT',
    'MENQUE',
    'MAYQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'ID',
    'DBPT'
] + list(reservadas.values())

# Tokens
t_PTCOMA    = r';'
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_IGUAL     = r'<-'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_CONCAT    = r'&'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_IGUALQUE  = r'=='
t_NIGUALQUE = r'!='
t_DBPT      = r':'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# digit = r'([o-9])'
# nondigit = r'([_A-Za-z])'
# identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r') *)'
# @TOKEN(identifier)
def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
from distutils.log import error
import ply.lex as lex
lexer = lex.lex()
# from ply.lex import TOKEN


# Asociación de operadores y precedencia
precedence = (
    ('left','CONCAT'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

# Definición de la gramática

from generadores.expresiones import *
from generadores.instrucciones import *


def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : imprimir_instr
                        | definicion_instr
                        | asignacion_instr
                        | mientras_instr
                        | hacerMientras_instr
                        | para_instr
                        | if_instr
                        | if_else_instr'''
    t[0] = t[1]

def p_instruccion_imprimir(t) :
    'imprimir_instr     : IMPRIMIR LLAVIZQ expresion_cadena LLAVDER'
    t[0] =Imprimir(t[3])

def p_instruccion_definicion(t) :
    'definicion_instr   : NUMERO ID'
    t[0] =DefinicionEntero(t[2])

def p_instruccion_definicionBool(t) :
    'definicion_instr   : BOOL ID'
    t[0] =DefinicionBooleano(t[2])

def p_valoresBooleanos(t) :
    '''expresion_logica     : ID'''
    t[0] =ExpresionLogica(t[1])    

def p_defiasigbool_instr(t) :
    'definicion_instr     : BOOL ID IGUAL expresion_logica'
    t[0] =DefinicionBooleano(t[2], t[4])

def p_asignacionbool_instr(t) :
    'asignacion_instr   : ID IGUAL expresion_logica'
    t[0] =AsignacionBooleano(t[1], t[3])

def p_defiasig_instr(t) :
    'definicion_instr   : NUMERO ID IGUAL expresion_numerica'
    t[0] =DefinicionEntero(t[2], t[4])

def p_asignacion_instr(t) :
    'asignacion_instr   : ID IGUAL expresion_numerica'
    t[0] =AsignacionEntero(t[1], t[3])

def p_mientras_instr(t) :
    'mientras_instr     : MIENTRAS LLAVIZQ expresion_logica LLAVDER DBPT instrucciones FINMIENTRAS'
    t[0] =Mientras(t[3], t[6])

def p_hacerMientras_instr(t) :
    'hacerMientras_instr     : HACER DBPT instrucciones MIENTRAS LLAVIZQ expresion_logica LLAVDER'
    t[0] = HacerMientras(t[6], t[3])

def p_para_instr(t) :
    'para_instr     : PARA LLAVIZQ definicion_instr PTCOMA expresion_logica PTCOMA asignacion_instr LLAVDER DBPT instrucciones FINPARA'
    t[0] = Para(t[3], t[5], t[7], t[10])

def p_if_instr(t) :
    'if_instr           : IF LLAVIZQ expresion_logica LLAVDER DBPT instrucciones FINSI'
    t[0] =If(t[3], t[6])

def p_if_else_instr(t) :
    'if_else_instr      : IF LLAVIZQ expresion_logica LLAVDER DBPT instrucciones ELSE DBPT instrucciones FINSI'
    t[0] =IfElse(t[3], t[6], t[9])

def p_expresion_binaria(t):
    '''expresion_numerica : expresion_numerica MAS expresion_numerica
                        | expresion_numerica MENOS expresion_numerica
                        | expresion_numerica POR expresion_numerica
                        | expresion_numerica DIVIDIDO expresion_numerica'''
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)

def p_expresion_unaria(t):
    'expresion_numerica : MENOS expresion_numerica %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])

def p_expresion_agrupacion(t):
    'expresion_numerica : PARIZQ expresion_numerica PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion_numerica   : ENTERO
                            | DECIMAL'''
    t[0] = ExpresionNumero(t[1])

def p_expresion_id(t):
    'expresion_numerica   : ID'
    t[0] = ExpresionIdentificador(t[1])

def p_expresion_concatenacion(t) :
    'expresion_cadena     : expresion_cadena CONCAT expresion_cadena'
    t[0] = ExpresionConcatenar(t[1], t[3])

def p_expresion_cadena(t) :
    'expresion_cadena     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])

def p_expresion_cadena_numerico(t) :
    'expresion_cadena     : expresion_numerica'
    t[0] = ExpresionCadenaNumerico(t[1])

def p_expresion_logica(t) :
    '''expresion_logica : expresion_numerica MAYQUE expresion_numerica
                        | expresion_numerica MENQUE expresion_numerica
                        | expresion_numerica IGUALQUE expresion_numerica
                        | expresion_numerica NIGUALQUE expresion_numerica'''
    if t[2] == '>'    : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == '<'  : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == '==' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE)

def p_error(t):
    global errorG
    errorG = (t+"\nError sintáctico en '%s'" % t.value)
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)