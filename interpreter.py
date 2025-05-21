# interpreter.py
from mytoken import NUMBER, BOOL, STRING, IDENTIFIER, PRINT, ASSIGN, \
    PLUS, MINUS, MUL, DIV, EQ, NEQ, LT, GT, AND, OR, NOT, CONCAT, LPAREN, RPAREN

class Interpreter:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.globals = {}

    def consume(self):
        if self.pos >= len(self.tokens):
            raise Exception("Unexpected end of input.")
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def match(self, expected_type):
        if self.peek() and self.peek().type == expected_type:
            return self.consume()
        return None

    def statement(self):
        token = self.peek()
        if token and token.type == IDENTIFIER:
            var_token = self.consume()
            if self.match(ASSIGN):
                value = self.expression()
                self.globals[var_token.value] = value
                return value
            else:
                self.pos -= 1
        elif token and token.type == PRINT:
            self.consume()
            value = self.expression()
            print(value)
            return None
        return self.expression()

    def expression(self):
        return self.equality()

    def equality(self):
        left = self.comparison()
        while self.peek() and self.peek().type in (EQ, NEQ):
            op = self.consume()
            right = self.comparison()
            left = self.evaluate(op, left, right)
        return left

    def comparison(self):
        left = self.term()
        while self.peek() and self.peek().type in (LT, GT):
            op = self.consume()
            right = self.term()
            left = self.evaluate(op, left, right)
        return left

    def term(self):
        left = self.factor()
        while self.peek() and self.peek().type in (PLUS, MINUS, CONCAT):
            op = self.consume()
            right = self.factor()
            left = self.evaluate(op, left, right)
        return left

    def factor(self):
        left = self.unary()
        while self.peek() and self.peek().type in (MUL, DIV):
            op = self.consume()
            right = self.unary()
            left = self.evaluate(op, left, right)
        return left

    def unary(self):
        if self.peek() and self.peek().type == NOT:
            self.consume()
            return not self.unary()
        elif self.peek() and self.peek().type == MINUS:
            self.consume()
            return -self.unary()
        else:
            return self.primary()

    def primary(self):
        token = self.peek()
        if token is None:
            raise Exception("Expected value but got end of input.")
        if token.type in (NUMBER, BOOL, STRING):
            return self.consume().value
        elif token.type == IDENTIFIER:
            name = self.consume().value
            if name in self.globals:
                return self.globals[name]
            else:
                raise Exception(f"Undefined variable '{name}'")
        elif token.type == LPAREN:
            self.consume()
            expr = self.expression()
            if not self.match(RPAREN):
                raise Exception("Missing closing parenthesis.")
            return expr
        else:
            raise Exception(f"Unexpected token: {token}")

    def evaluate(self, op, left, right):
        try:
            if op.type == PLUS:
                return left + right
            elif op.type == MINUS:
                return left - right
            elif op.type == MUL:
                return left * right
            elif op.type == DIV:
                return left / right
            elif op.type == EQ:
                return left == right
            elif op.type == NEQ:
                return left != right
            elif op.type == LT:
                return left < right
            elif op.type == GT:
                return left > right
            elif op.type == AND:
                return left and right
            elif op.type == OR:
                return left or right
            elif op.type == CONCAT:
                return str(left) + str(right)
        except Exception as e:
            raise Exception(f"Type error: {e}")
