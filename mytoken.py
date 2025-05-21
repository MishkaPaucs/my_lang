# mytoken.py
NUMBER = 'NUMBER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
BOOL = 'BOOL'
AND = 'AND'
OR = 'OR'
NOT = 'NOT'
EQ = 'EQ'
NEQ = 'NEQ'
LT = 'LT'
GT = 'GT'
STRING = 'STRING'
CONCAT = 'CONCAT'
IDENTIFIER = 'IDENTIFIER'
PRINT = 'PRINT'
ASSIGN = 'ASSIGN'

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'{self.type}:{self.value}'
