
from generadores import gramatica as g
from generadores import ts as TS
from generadores.expresiones import *
from generadores.instrucciones import *

s = ""

def procesar_imprimir(instr, ts) :
   global s 
   s +='> '+ resolver_cadena(instr.cad, ts) + '\n'

def procesar_definicionEntero(instr, ts) :
    val = resolver_expresion_aritmetica(instr.expNumerica, ts)
    if(val == None):
        val = 0
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
    ts.agregar(simbolo)

def procesar_asignacionEntero(instr, ts) :
    val = resolver_expresion_aritmetica(instr.expNumerica, ts)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
    ts.actualizar(simbolo)

def procesar_definicionBooleano(instr, ts) :
    val = None
    if(instr.valor != False):
        if (instr.valor == 'real'):
            val = True
        elif (instr.valor == 'falsus'):
            val = False
        else:    
            val = resolver_expreision_logica(instr.valor, ts)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEANO, val)
    ts.agregar(simbolo)

def procesar_asignacionBooleano(instr, ts) :
    val = None
    if (instr.valor == 'real'):
        val = True
    elif (instr.valor == 'falsus'):
        val = False
    else:    
        val = resolver_expreision_logica(instr.valor, ts)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOLEANO, val)
    ts.actualizar(simbolo)
    print(instr.valor)

def procesar_mientras(instr, ts) :
    while resolver_expreision_logica(instr.expLogica, ts) :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)

def procesar_hacerMientras(instr, ts) :
    ts_local = TS.TablaDeSimbolos(ts.simbolos)
    procesar_instrucciones(instr.instrucciones, ts_local)
    while resolver_expreision_logica(instr.expLogica, ts) :
        procesar_instrucciones(instr.instrucciones, ts_local)

def procesar_para(instr, ts) :
    ts_local = TS.TablaDeSimbolos(ts.simbolos)
    procesar_definicionEntero(instr.inicializacion, ts_local)
    while resolver_expreision_logica(instr.expLogica, ts) :
        procesar_instrucciones(instr.instrucciones, ts_local)
        procesar_asignacionEntero(instr.cambio, ts_local)
    simbolo = TS.Simbolo(instr.inicializacion.id, TS.TIPO_DATO.NUMERO, None)
    ts.remover(simbolo)

def procesar_if(instr, ts) :
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)

def procesar_if_else(instr, ts) :
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrIfVerdadero, ts_local)
    else :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrIfFalso, ts_local)

def resolver_cadena(expCad, ts) :
    if isinstance(expCad, ExpresionConcatenar) :
        exp1 = resolver_cadena(expCad.exp1, ts)
        exp2 = resolver_cadena(expCad.exp2, ts)
        return exp1 + exp2
    elif isinstance(expCad, ExpresionDobleComilla) :
        return expCad.val
    elif isinstance(expCad, ExpresionCadenaNumerico) :
        return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else :
        print('Error: Expresión cadena no válida')


def resolver_expreision_logica(expLog, ts) :
    if(expLog.exp2 != None):
        exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)
        if expLog.operador == OPERACION_LOGICA.MAYOR_QUE : return exp1 > exp2
        if expLog.operador == OPERACION_LOGICA.MENOR_QUE : return exp1 < exp2
        if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
        if expLog.operador == OPERACION_LOGICA.DIFERENTE : return exp1 != exp2
    else:
        return ts.obtener(expLog.exp1).valor

def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador) :
        return ts.obtener(expNum.id).valor


def procesar_instrucciones(instrucciones, ts) :
    global s
    ## lista de instrucciones recolectadas
    try:
        for instr in instrucciones :
            if isinstance(instr, Imprimir) : procesar_imprimir(instr, ts)
            elif isinstance(instr, DefinicionEntero) : procesar_definicionEntero(instr, ts)
            elif isinstance(instr, AsignacionEntero) : procesar_asignacionEntero(instr, ts)
            elif isinstance(instr, DefinicionBooleano) : procesar_definicionBooleano(instr, ts)
            elif isinstance(instr, AsignacionBooleano) : procesar_asignacionBooleano(instr, ts)
            elif isinstance(instr, Mientras) : procesar_mientras(instr, ts)
            elif isinstance(instr, HacerMientras) : procesar_hacerMientras(instr, ts)
            elif isinstance(instr, Para) : procesar_para(instr, ts)
            elif isinstance(instr, If) : procesar_if(instr, ts)
            elif isinstance(instr, IfElse) : procesar_if_else(instr, ts)
            else : s+='Error: instrucción no válida'
    except:
        from Interprete.static.Interprete.py.ts import error as error
        from Interprete.static.Interprete.py.gramatica import errorG as errorG
        s = (str(errorG) + "\n" + str(error))
        print(s)


def validar(text):
    g.parse(text)
    global s
    from Interprete.static.Interprete.py.ts import error as error
    from Interprete.static.Interprete.py.gramatica import errorG as errorG
    s = (str(errorG) + "\n" + str(error))
    return (s)
    
def ejecutar(text):
    global s 
    s = ""
    instrucciones = g.parse(text)
    ts_global = TS.TablaDeSimbolos()
    procesar_instrucciones(instrucciones, ts_global)
    return (s)