# lexer.py
import re
from mytoken import Token, NUMBER, STRING, BOOL, IDENTIFIER, PRINT, ASSIGN, \
    PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EQ, NEQ, LT, GT, AND, OR, NOT, CONCAT

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []

    def tokenize(self):
        token_specification = [
            (PRINT, r'\bprint\b'),
            (BOOL, r'\btrue\b|\bfalse\b'),
            (NUMBER, r'\d+(\.\d*)?'),
            (STRING, r'"[^"]*"'),
            (EQ, r'=='), (NEQ, r'!='),
            (AND, r'\band\b'), (OR, r'\bor\b'),
            (NOT, r'!'),
            (PLUS, r'\+'), (MINUS, r'-'),
            (MUL, r'\*'), (DIV, r'/'),
            (LT, r'<'), (GT, r'>'),
            (LPAREN, r'\('), (RPAREN, r'\)'),
            (ASSIGN, r'='),
            (IDENTIFIER, r'[a-zA-Z_]\w*')
        ]

        tok_regex = '|'.join(f'(?P<{tok}>{pattern})' for tok, pattern in token_specification)

        for mo in re.finditer(tok_regex, self.text):
            kind = mo.lastgroup
            value = mo.group()

            if kind == NUMBER:
                value = float(value) if '.' in value else int(value)
            elif kind == STRING:
                value = value[1:-1]
            elif kind == BOOL:
                value = True if value == 'true' else False

            self.tokens.append(Token(kind, value))

        return self.tokens
