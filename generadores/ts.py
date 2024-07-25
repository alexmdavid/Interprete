from enum import Enum

error = ""

class TIPO_DATO(Enum) :
    NUMERO = 1
    BOOLEANO = 2

class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, valor) :
        self.id = id
        self.tipo = tipo
        self.valor = valor

class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos = {}) :
        self.simbolos = simbolos

    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id) :
        if not id in self.simbolos :
            global error
            error = 'Error: variable ', id, ' no definida.'

        return self.simbolos[id]

    def actualizar(self, simbolo) :
        if not simbolo.id in self.simbolos :
            global error
            error = 'Error: variable ', id, ' no definida.'
        else :
            self.simbolos[simbolo.id] = simbolo

    def remover(self, simbolo) :
        del self.simbolos[simbolo.id]