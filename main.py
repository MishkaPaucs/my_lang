# main.py
from lexer import Lexer
from interpreter import Interpreter

def run(source, interpreter):
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    interpreter.tokens = tokens
    interpreter.pos = 0
    result = interpreter.statement()
    if result is not None:
        print(result)

if __name__ == '__main__':
    interpreter = Interpreter([])
    while True:
        try:
            source = input(">>> ")
            if source.strip().lower() in ("exit", "quit"):
                break
            run(source, interpreter)
        except Exception as e:
            print("Error:", e)
